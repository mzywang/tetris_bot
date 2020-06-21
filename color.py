from enum import Enum

class Color(Enum):
    PURPLE = (161, 56, 135, 255)
    RED = (198, 46, 61, 255)
    LIGHT_BLUE = (68, 154, 210, 255)
    BLUE = (37, 70, 191, 255)
    GREEN = (112, 174, 52, 255)
    YELLOW = (218, 161, 55, 255)
    ORANGE = (212, 99, 40, 255)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

COLORS = [
    Color.PURPLE, 
    Color.RED, 
    Color.LIGHT_BLUE, 
    Color.BLUE,
    Color.GREEN,
    Color.YELLOW,
    Color.ORANGE
]

