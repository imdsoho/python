class Error(Exception):
    """Base-class for all exceptions raised by this module."""

class InvalidDesityError(Error):
    """Three was a problem with a provided density value."""

def determine_weight(volume, density):
    if density <= 0:
        raise ValueError('Density must be positive')

