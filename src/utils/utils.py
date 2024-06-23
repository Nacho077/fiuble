from io import TextIOWrapper
from utils.statics import LETTERS_TO_NORMALIZE, COLORS, DEFAULT_COLOR
from os import system, name

def read_line(file: TextIOWrapper):
    line = file.readline()
    return line.rstrip('\n').split(",") if line else ("", "")

def select_choise(message: str, options: tuple[str, ...]) -> str:
    """Select choise in option

    Show message and options while user doesn't choise a correct option

    Args:
        message (str): Message to show
        options (tuple[str, ...]): Options to show

    Returns:
        response: Option selected

    Example:
        >>> select_choise("message", ("Y", "N"))
    """
    res = input(message)

    while not res.upper() in options:
        print("Please select a valid option")
        res = input(message)

    return res

def is_true_option(message: str, options: tuple[str, ...]) -> bool:
    """Returns if choise selected it's first"""
    return select_choise(message, options).upper() == options[0]

def validate_type(type_needed, value):
    """Function fot cast to specific type

    Args:
        type_needed: function to cast value
        value: Value for be casted

    Returns:
        Value casted

    Example:
        >>> validate_type(int, "2") -> 2
        >>> validate_type(lambda: v: v.upper(), "test") -> "TEST"
        >>> validate_type(lambda: v: v.upper() === "TRUE", "True") -> True
    """
    return type_needed(value)
    
def normalize_word(word: str) -> str:
    """Normalize word

    Replace all unrecognized characters and returns word without them and upper

    Args:
        word (str): Word to be normalized

    Example:
        >>> normalize_word("test") -> "TEST"
        >>> normalize_word("tÉsÁót") -> "TESAOT"
    """
    word = word.upper()

    for accented_letter, unaccented_letter in LETTERS_TO_NORMALIZE:
        word = word.replace(accented_letter, unaccented_letter)

    return word

def change_console_color(text, color) -> str:
    return COLORS[color] + text + COLORS[DEFAULT_COLOR] if text != "" else ""

def clear_console():
    if name == "nt":
        system("cls")
    else:
        system("clear")