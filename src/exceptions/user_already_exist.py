class UserAlreadyExistsError(Exception):
    """Exception raised for errors in the creation of a new user.

    Attributes:
        message: explanation of the error
    """

    def __init__(self, message="User already exists"):
        self.message = message
        super().__init__(self.message)