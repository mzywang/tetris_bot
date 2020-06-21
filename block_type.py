from enum import Enum
import numpy as np
from color import *

class BlockType(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6

    @staticmethod
    def get_block_type_from_color(color):
        return _COLOR_BLOCK_MAP[color]

    @property
    def default_block_array(self):
        return _DEFAULT_BLOCK_ARRAY_MAP[self] 

    @property
    def default_offset(self):
        return _DEFAULT_OFFSET_MAP[self]

_COLOR_BLOCK_MAP = {  
    Color.LIGHT_BLUE: BlockType.I,  
    Color.YELLOW: BlockType.O,  
    Color.PURPLE: BlockType.T,  
    Color.GREEN: BlockType.S,  
    Color.RED: BlockType.Z,  
    Color.BLUE: BlockType.J,  
    Color.ORANGE: BlockType.L,  
} 

_DEFAULT_BLOCK_ARRAY_MAP = {
    BlockType.I: np.array([
        [1, 1, 1, 1]
    ]),
    BlockType.O: np.array([
        [1, 1], 
        [1, 1],
    ]),
    BlockType.T: np.array([
        [0, 1, 0],
        [1, 1, 1],
    ]),
    BlockType.S: np.array([
        [0, 1, 1],
        [1, 1, 0],
    ]),
    BlockType.Z: np.array([
        [1, 1, 0],
        [0, 1, 1],
    ]),
    BlockType.J: np.array([
        [1, 0, 0],
        [1, 1, 1],
    ]),
    BlockType.L: np.array([
        [0, 0, 1],
        [1, 1, 1],
    ]),
}

_DEFAULT_OFFSET_MAP = {
    BlockType.I: 3,
    BlockType.O: 4,
    BlockType.T: 3,
    BlockType.S: 3,
    BlockType.Z: 3,
    BlockType.J: 3,
    BlockType.L: 3,
}
