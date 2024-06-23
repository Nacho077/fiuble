class UserNotFoundError(Exception):
    """Exception raised for errors in the search of users.

    Attributes:
        message: explanation of the error
    """

    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)