from game_modes.console.console import ConsonsoleGame
from models.user import User
from utils import statics
from utils.utils import change_console_color, clear_console, is_true_option, normalize_word


class MultiPlayer(ConsonsoleGame):
    MAX_PLAYERS_QUANTITY = 2
    MIN_PLAYERS_QUANTITY = 2

    def start_game(self):
        self.read_configs()

        while self.get_players_quantity() < self.MAX_PLAYERS_QUANTITY:
            if self.get_players_quantity() < self.MIN_PLAYERS_QUANTITY or is_true_option("Do you want register other user? (Y/N): ", ("Y", "N")):
                self.login_user()
            else:
                break
        
        initial_player = 0

        while self._is_posible_next_game():
            self.initialize_new_game()
            game_finished = False
            is_winner = False
            initial_player = self.select_next_player(initial_player)
            player_turn = initial_player
            
            while not game_finished:
                player_turn = self.select_next_player(player_turn)
                game_finished, is_winner = self.next_turn(player_turn)

            self.finish_game(is_winner, player_turn)

        for player in self._players:
            self._scores_repository.save_points(player.name, player.points)

        self.show_scores()

    def select_next_player(self, player_turn):
        return player_turn + 1 if player_turn < (self.get_players_quantity() - 1) else 0

    def next_turn(self, player_turn: int):
        clear_console()
        print(f"turn {len(self.attempts) + 1} for {self.get_player(player_turn).formated_name}: ")
        self.print_attempts()
        
        attempt = normalize_word(input("Next attempt: "))

        while not self.is_valid_attempt(attempt):
            print("Please enter a valid word")
            attempt = normalize_word(input("Next attempt: "))
        
        attempt_result, is_winner = self.proccess_attempt(attempt)
        self.attempts.append(attempt_result)

        if is_winner:
            return True, True
        
        if len(self.attempts) == self.MAX_NUM_ATTEMPTS:
            return True, False

        return False, False
    
    def finish_game(self, is_winner: bool, player_winner_index: int):
        clear_console()
        self._games_played += 1
        mins, segs = self.calculate_time()
        points = self.calculate_points(is_winner, mins, segs)

        winner_player = self.get_player(player_winner_index)
        loser_players = list(filter(lambda player: player.name != winner_player.name, self._players))

        winner_player.points += points
        self.update_points(loser_players, points // 2)

        print(self.attempts[-1].center(10))
        if is_winner:
            print(f"""
    {change_console_color('CONGRATULATIONS', statics.GREEN)} {winner_player.formated_name}!  
    You have earned {points} points{"" if self._games_played == 0 else f" and have a total of {winner_player.points} points"}!
    Don't worry {', '.join([player.formated_name for player in loser_players])} you won {points // 2} points!
    It took {mins} mins and {segs} segs
            """)
        else:
            print(f"""
    You couldn't guess the word
    You got {points} point
    It took {mins} mins and {segs} segs
            """)
        
            self.update_points(self._players, points)

    def update_points(self, players: list[User], points: int):
        for player in players:
            player.points += points
