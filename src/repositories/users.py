from .singleton import Singleton
from utils.utils import read_line
from exceptions import UserNotFoundError, IncorrectPasswordError, UserAlreadyExistsError

class UsersRepository(metaclass=Singleton):
    def __init__(self, file_direction):
        self._file = file_direction

    def get_user(self, user: str):
        """Get username and Password for a user

        Args:
            user (str): userName for search

        Returns:
            username (str)
            password (str)

        Raises:
            UserNotFoundError: If user's file or username doesn't exists
        """
        try:
            with open(self._file) as file:
                registered_user, registered_password = read_line(file)
                while registered_user:
                    if registered_user == user:
                        return registered_user, registered_password
                    
                    
                    registered_user, registered_password = read_line(file)
                    
            raise UserNotFoundError()
        except FileNotFoundError:
            file = open(self._file, "w")
            file.close()

            raise UserNotFoundError()
        
    def user_exists(self, user) -> bool:
        try:
            self.get_user(user)

            return True
        except UserNotFoundError:
            return False

    def login_user(self, user, password):
        _, registered_password = self.get_user(user)
        if not password == registered_password:
            raise IncorrectPasswordError()
        else:
            return True

        
    def register_user(self, user: str, password: str) -> None:
        """Register a new user
        
        Raises:
            UserAlreadyExistsError: If user already exists
        """
        try:
            self.get_user(user)

            raise UserAlreadyExistsError()
        except UserNotFoundError:
            with open(self._file, "a") as file:
                file.write("{},{}\n".format(user, password))
        