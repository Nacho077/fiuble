SECRET_WORD_LENGTH = "Secret word length"
MAX_NUM_GAMES = "max num of games"
RESET_GAME_FILE = "Reset game file"

SETTINGS = {
    SECRET_WORD_LENGTH: 5,
    MAX_NUM_GAMES: 5,
    RESET_GAME_FILE: False
}

CAST_FUNCTIONS = {
    SECRET_WORD_LENGTH: int,
    MAX_NUM_GAMES: int,
    RESET_GAME_FILE: lambda val: val == 'True'
}

MAX_NUM_ATTEMPTS = 5

WORDS_FILE = "../files/texts"
SCORES_FILE = "../files/scores.csv"
USERS_FILE = "../files/user.csv"
SETTINGS_FILE = "./files/settings.csv"

POINTS = {
    1: 50,
    2: 40,
    3: 30,
    4: 20,
    5: 10
}

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