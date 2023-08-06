from .messages import raw_error
from contextlib import contextmanager
import sys

@contextmanager
def except_handler():
    """Sets a custom exception handler with the 'with' keyword"""
    
    def custom_excepthook(type, value, traceback) -> None:
        print(value)
    sys.excepthook = custom_excepthook
    
    yield
    sys.excepthook = sys.__excepthook__

class ThemeNotFound(Exception):
    """The theme has not found in the themes directory"""

    def __str__(self) -> str:
        return raw_error('The theme has not found in the themes directory')

class ThemeAlreadyExists(Exception):
    """The theme already exist in the themes directory"""
    
    def __str__(self) -> str:
        return raw_error('The theme already exist in the themes directory')

class DuplicatedThemeName(Exception):
    """Already exist a theme with the same name"""
    
    def __str__(self) -> str:
        return raw_error('Already exist a theme with the same name')

class ConfigBodyIsEmpty(Exception):
    """The theme config body is empty"""
    
    def __str__(self) -> str:
        return raw_error('The theme config body is empty')

class SavedConfigNotFound(Exception):
    """The selected configuration does not exist"""
    def __str__(self) -> str:
        return raw_error('The selected configuration does not exist')

class DestNotFound(Exception):
    """The destination directory does not exist"""
    def __str__(self) -> str:
        return raw_error('The destination directory does not exist')
