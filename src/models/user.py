from utils.utils import change_console_color

class User:
    
    def __init__(self, color: str, name: str):
        self._name = name
        self._points = 0
        self._formated_name = change_console_color(name, color)

    @property
    def name(self):
        return self._name
    
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, new_val):
        self._points = new_val
    
    @property
    def formated_name(self):
        return self._formated_name