USERS_FILE = "../files/users.csv"
SETTINGS_FILE = "../files/settings.csv"
SCORES_FILE = "../files/scores.csv"

LETTERS_TO_NORMALIZE = (
    ("Á", "A"),
    ("É", "E"),
    ("Í", "I"),
    ("Ó", "O"),
    ("Ú", "U"),
    ("À", "A"),
    ("È", "E"),
    ("Ì", "I"),
    ("Ò", "O"),
    ("Ù", "U"),
)

GREEN = "GREEN"
YELLOW = "YELLOW"
GRAY = "GRAY"
RED = "RED"
BLUE = "BLUE"
DEFAULT_COLOR = "DEFAULT_COLOR"

COLORS = {
    BLUE: "\33[34m",
    RED: "\033[91m",
    GREEN: "\x1b[32m",
    YELLOW: "\x1b[33m",
    GRAY: "\x1b[90m",
    DEFAULT_COLOR: "\x1b[39m",
}
