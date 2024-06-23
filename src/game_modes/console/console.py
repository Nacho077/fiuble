from models.user import User
from utils import *
from game_modes.game import Game
from getpass import getpass
from exceptions import UserNotFoundError, UserAlreadyExistsError, IncorrectPasswordError

class ConsonsoleGame(Game):
    def read_configs(self):
        if not self._settings_repository.exists_file():
            print("No settings created yet")
            self._settings_repository.save(settings.SETTINGS_DEFAULT)
            print("Settings file created with default values")
        
        print("Reading values from settings file...")

        is_final_settings = False

        while not is_final_settings:
            print("Final settings values:")
            self.print_settings()

            if utils.is_true_option("Do you want to change these settings? (Y/N): ", ("Y", "N")):
                self.set_new_settings()
            else:
                is_final_settings = True

    def set_new_settings(self):
        new_settings = {}

        for config in len(settings.SETTINGS):
            try:
                value = input(f"Enter a value for setting {config}: ")
                casted_value = utils.validate_type(settings.CAST_FUNCTIONS[config], value)
                new_settings[config] = casted_value
            except ValueError:
                print(f"{value} is not a valid value for setting {config}, please enter a valid value: ")

        self._settings_repository.save(new_settings)

    def print_settings(self):
        for config, value in self._settings_repository.get_settings().items():
            print(f"{config}: {value}")

    def proccess_attempt(self, attempt):
        """Process an attempt

        Args:
            attempt (str): attempt to process

        Returns:
            result (str): attempt with letter in colors to print
            is_winner (bool): boolean that declares if user win or not
        """
        correct_letters, wrong_place, wrong_letters = super().proccess_attempt(attempt)
        if len(correct_letters) == self._settings_repository.get_settings()[settings.SECRET_WORD_LENGTH]:
            return utils.change_console_color(attempt, statics.GREEN), True
        
        return self.get_attempt_result(attempt, correct_letters, wrong_place, wrong_letters), False

    def get_attempt_result(self, attempt:str, correct_letters: list[str], wrong_place: list[str], wrong_letters: list[str]):
        result = ""

        for index, letter in enumerate(attempt):
            if index in correct_letters:
                result += utils.change_console_color(letter, statics.GREEN)
            elif letter in wrong_place:
                result += utils.change_console_color(letter, statics.YELLOW)
                wrong_place.remove(letter)
            elif letter in wrong_letters:
                result += utils.change_console_color(letter, statics.GRAY)
                wrong_letters.remove(letter)

        return result
    
    def login_user(self):
        utils.clear_console()
        print(f"Please log in player {self.get_players_quantity() + 1} to play")

        user = input("User: ")
        password = getpass()

        try:
            if self.player_exists(user):
                if utils.is_true_option("This user is already loged, do you want create other user? (Y/N): ", ("Y", "N")):
                    self.register_user()
                else:
                    self.login_user()
            else:
                self._users_repository.login_user(user, password)

                self.create_user(user)
        except UserNotFoundError:
            message = "User not found, do you want create a new user? (Y/N): "
            if utils.is_true_option(message, ("Y", "N")):
                self.register_user()
            else:
                message = "Do you want to try to log in again? (Y/N): "
                if utils.is_true_option(message, ("Y", "N")):
                    self.login_user()
                else:
                    raise RuntimeError() # CHANGE #

    def register_user(self):
        user = input("What do you want your username to be?: ")
        if self._users_repository.user_exists(user):
            print("""This user name already exists.
            Please select another username""")
            return self.register_user()
            
        passwordsEquals = False

        while not passwordsEquals:
            print("What do you want your password to be?:")
            password = getpass()
            print("Please write your password again:")
            passwordRepeated = getpass()

            if password != passwordRepeated:
                print("Please write same passwords")
            else:
                passwordsEquals = True

        self._users_repository.register_user(user, password)
        self.create_user(user)
        # ADD CASE FOR UserAlreadyExistsError

    def _is_posible_next_game(self):
        if self._games_played == 0:
            return True

        if not self._games_played < self._settings_repository.get_settings()[settings.MAX_NUM_GAMES]:
            return False
        
        return utils.is_true_option("Do you want play other game? (Y/N): ", ("Y", "N"))

    def print_attempts(self):
        for attempt in self.attempts:
            print(attempt)

    def show_scores(self):
        TOTAL_LENGTH = 20

        utils.clear_console()
        for player in self._players:
            print(f"Score for {player.formated_name} is {player.points}".center(TOTAL_LENGTH))
        
        print("BEST SCORES".center(TOTAL_LENGTH), end="\n\n")

        scores = f"{'USER'.center(TOTAL_LENGTH // 2)}|{'SCORE'.center(TOTAL_LENGTH // 2)}\n"

        for user, score in self._scores_repository.get_scores():
            scores +=f"{user.center(TOTAL_LENGTH // 2)}|{score.center(TOTAL_LENGTH // 2)}\n"

        print(scores)
