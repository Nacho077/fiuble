from .singleton import Singleton
import os
from utils.utils import read_line, validate_type


class ScoresRepository(metaclass=Singleton):
    
    def __init__(self, file_direction: str) -> None:
        self._file = file_direction

    def _exists_file(self):
        return os.path.isfile(self._file)

    def get_scores(self):
        scores = []

        try:
            with open(self._file) as file:
                user, points = read_line(file)
                while user:
                    scores.append((user, points))
                    user, points = read_line(file)
        except FileNotFoundError:
            file = open(self._file, "w")
            file.close()
        finally:
            return scores

    def save_points(self, user: str, points: int, need_restart: bool = False) -> None:
        if need_restart or not self._exists_file():
            with open(self._file, "w") as file:
                file.write(f"{user},{points}\n")
        else:
            self._write_file(user, points)

    def _write_file(self, user: str, points: int):
        scores = ""
        score_writed = False

        with open(self._file, "r") as file:
            username, score = read_line(file)

            while username:
                if validate_type(int, score) < points and not score_writed:
                    scores += f"{user},{points}\n"
                    score_writed = True

                scores += f"{username},{score}\n"
                username, score = read_line(file)

            if not score_writed:
                scores += f"{user},{points}\n"

        with open(self._file, "w") as file:
            file.write(scores)
