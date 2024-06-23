import os.path
from .singleton import Singleton
from utils.utils import read_line, validate_type
from utils.settings import SETTINGS as VALID_SETTINGS, CAST_FUNCTIONS

class SettingsRepository(metaclass=Singleton):
    _cached_settings = None
    
    def __init__(self, file_direction: str) -> None:
        self._file = file_direction

    def exists_file(self) -> bool:
        return os.path.isfile(self._file)

    def get_settings(self):
        if not self._cached_settings:
            self._get_settings_from_csv()

        return self._cached_settings

    def save(self, new_settings: dict[str, any]):
        """Save configurations

        Args:
            new_settings (dic[str, any]): A dictionary containing settings.
                The keys represents the names of the settings,
                and the values represents the values that will be saved.
        
        Example:
            >>> settingsRepository.save({'max_num_of_games': 1, 'reset_game_file': False})
        """
        new_valid_settings = {}

        with open(self._file, "w") as file:
            for config, value in new_settings.items():
                if config in VALID_SETTINGS:
                    file.write("{},{}\n".format(config, value))
                    new_valid_settings[config] = value

        self._cached_settings = new_valid_settings

    def _get_settings_from_csv(self):
        settings = {}

        with open(self._file) as file:
            config, value = read_line(file)
            while config in VALID_SETTINGS:
                casted_value = validate_type(CAST_FUNCTIONS[config], value)
                settings[config] = casted_value
                config, value = read_line(file)

        self._cached_settings = settings
