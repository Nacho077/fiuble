import math
from numbers import Number # ??
import re
import time
from abc import ABC, abstractmethod
from exceptions.user_not_found import UserNotFoundError
from models.user import User
from repositories import SettingsRepository, UsersRepository, ScoresRepository
from utils import *

class Game(ABC):
    MAX_NUM_ATTEMPTS = 5

    def __init__(self,
            settings_repository: SettingsRepository,
            users_repository: UsersRepository,
            scores_repository: ScoresRepository
            ):
        self._settings_repository = settings_repository
        self._users_repository = users_repository
        self._scores_repository = scores_repository
        self._players: list[User] = []
        self._games_played = 0

    def get_player(self, idx: Number = 0) -> User:
        if idx > self.MAX_PLAYERS_QUANTITY or idx < 0:
            raise UserNotFoundError()
        
        return self._players[idx]
    
    def add_player(self, player: User):
        if len(self._players) >= self.MAX_PLAYERS_QUANTITY:
            raise # add error

        self._players.append(player)

    def get_players_quantity(self):
        return len(self._players)
    
    def player_exists(self, name: str):
        return any(player.name == name for player in self._players)

    @abstractmethod
    def start_game(self) -> None:
        pass

    def initialize_new_game(self):
        self.attempts = []
        self._initial_time = time.time()
        ##########################
        #         CHANGE         #
        ##########################
        self.secret_word = "TESTE"

    def calculate_time(self):
        final_time = time.time()
        played_time = final_time - self._initial_time
        mins = math.floor(played_time / 60)
        segs = round(played_time % 60)

        return mins, segs

    def calculate_points(self, is_winner: bool, mins: int, segs: int) -> int:
        """Calculate total points for user with quantity of attempts, time spend and if user wons or not
        
        if user loses the points are -100
        else calculate points by time and attempts spended
        """
        TOTAL_TIME = 60 * 5
        points_by_time = TOTAL_TIME - ((mins * 60) + segs)

        return -100 if not is_winner else ((self.MAX_NUM_ATTEMPTS + 1 - len(self.attempts)) * 10) + points_by_time
    
    def is_valid_attempt(self, attempt):
        if len(attempt) != self._settings_repository.get_settings()[settings.SECRET_WORD_LENGTH]:
            return False
        
        if re.search("[^A-Z]", attempt): #change !re.search?
            return False
        
        return True

    def proccess_attempt(self, attempt: str):
        attempt = attempt.upper()
        correct_letters, mistakes, missing_letters = self.get_correct_letters(attempt)
        wrong_place, wrong_letter = self.proccess_mistakes(mistakes, missing_letters)

        return correct_letters, wrong_place, wrong_letter

    def get_correct_letters(self, attempt):
        correct_letters = []
        mistakes = []
        missing_letters = []

        for index in range(len(attempt)):
            if self.secret_word[index] == attempt[index]:
                correct_letters.append(index)
            else:
                mistakes.append(attempt[index])
                missing_letters.append(self.secret_word[index])

        return correct_letters, mistakes, missing_letters
    
    def proccess_mistakes(self, mistakes, missing_letters):
        wrong_place = []
        wrong_letter = []
        
        for letter in mistakes:
            if letter in missing_letters:
                wrong_place.append(letter)
                missing_letters.remove(letter)
            else:
                wrong_letter.append(letter)

        return wrong_place, wrong_letter

    def create_user(self, username):
        color = [*statics.COLORS][self.get_players_quantity()]

        try:
            self.add_player(User(color, username))
        except IndexError:
            print("Player limit reached") # Pasar a error