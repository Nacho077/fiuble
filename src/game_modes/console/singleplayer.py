from game_modes.console.console import ConsonsoleGame
from utils import statics
from utils.utils import clear_console, normalize_word, change_console_color

class SinglePlayer(ConsonsoleGame):
    MAX_PLAYERS_QUANTITY = 1
    MIN_PLAYERS_QUANTITY = 1

    def start_game(self):
        self.read_configs()
        self.login_user()

        while self._is_posible_next_game():
            self.initialize_new_game()
            game_finished = False
            is_winner = False

            while not game_finished:
                game_finished, is_winner = self.next_turn()

            self.finish_game(is_winner)

        player = self.get_player()
        self._scores_repository.save_points(player.name, player.points)
        self.show_scores()

    def next_turn(self):
        clear_console()
        print(f"{'welcome' if len(self.attempts) == 0 else f'turn {len(self.attempts) + 1}'} {self.get_player().formated_name}: ")
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

    def finish_game(self, is_winner):
        clear_console()
        self._games_played += 1
        mins, segs = self.calculate_time()
        points = self.calculate_points(is_winner, mins, segs)
        self.get_player().points += points

        print(self.attempts[-1].center(10))
        if is_winner:
            print(f"""
    {change_console_color('CONGRATULATIONS', statics.GREEN)}!
    You have earned {points} points{"" if self._games_played == 1 else f" and have a total of {self.get_player().points} points"}!
    It took tou {mins} mins and {segs} segs
            """)
        else:
            print(f"""
    You couldn't guess the word
    You got {points} points
    It took you {mins} mins and {segs} segs
            """)
