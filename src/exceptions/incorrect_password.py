class IncorrectPasswordError(Exception):
    """Exception raised for errors in the validation of password for user.

    Attributes:
        message: explanation of the error
    """

    def __init__(self, message="Incorrect password"):
        self.message = message
        super().__init__(self.message)