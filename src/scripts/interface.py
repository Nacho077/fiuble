from game_modes.interface.interface import InterfaceGame
from repositories import *
from utils.statics import SETTINGS_FILE, USERS_FILE, SCORES_FILE

def main():
    settingsRepository = SettingsRepository(SETTINGS_FILE)
    usersRepository = UsersRepository(USERS_FILE)
    scoresRepository = ScoresRepository(SCORES_FILE)

    game = InterfaceGame(settingsRepository, usersRepository, scoresRepository)
    game.start_game()

if __name__ == '__main__':
    main()
