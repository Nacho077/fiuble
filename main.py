from src.game_modes.game import Game
from src.game_modes.console import *
from src.utils import *
from src.repositories import *
from src.utils.statics import SETTINGS_FILE, USERS_FILE, SCORES_FILE

def select_game_mode() -> Game:
    settingsRepository = SettingsRepository(SETTINGS_FILE)
    usersRepository = UsersRepository(USERS_FILE)
    scoresRepository = ScoresRepository(SCORES_FILE)

    message_quantity_players = "Select the number of players (1/2): "

    SINGLE_PLAYER_MODE = "1"
    MULTI_PLAYER_MODE = "2"
    quantity_players = utils.select_choise(message_quantity_players, (SINGLE_PLAYER_MODE, MULTI_PLAYER_MODE))

    game_modes = {
        SINGLE_PLAYER_MODE: ConsoleSinglePayer,
        MULTI_PLAYER_MODE: ConsoleMultiPlayer
    }

    return game_modes[quantity_players](settingsRepository, usersRepository, scoresRepository)

if __name__ == "__main__":
    try:
        game = select_game_mode()
        game.start_game()
    except Exception as exception:
       print("END GAME", exception)
