from enum import Enum
import numpy as np
from color import *

class Block(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6

    @property
    def get_default_orientation(self):
        return _DEFAULT_ORIENTATION_MAP[self] 

    @classmethod
    def get_block_from_color(cls, color):
        return _COLOR_BLOCK_MAP[color]

_COLOR_BLOCK_MAP = {
    Color.LIGHT_BLUE: Block.I,
    Color.YELLOW: Block.O,
    Color.PURPLE: Block.T,
    Color.GREEN: Block.S,
    Color.RED: Block.Z,
    Color.BLUE: Block.J,
    Color.ORANGE: Block.L,
}

_DEFAULT_ORIENTATION_MAP = {
    Block.I: np.array([
        [1, 1, 1, 1]
    ]),
    Block.O: np.array([
        [1, 1], 
        [1, 1],
    ]),
    Block.T: np.array([
        [0, 1, 0],
        [1, 1, 1],
    ]),
    Block.S: np.array([
        [0, 1, 1],
        [1, 1, 0],
    ]),
    Block.Z: np.array([
        [1, 1, 0],
        [0, 1, 1],
    ]),
    Block.J: np.array([
        [1, 0, 0],
        [1, 1, 1],
    ]),
    Block.L: np.array([
        [0, 0, 1],
        [1, 1, 1],
    ]),
}
