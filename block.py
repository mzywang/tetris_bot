from block_type import * 
from board import *

class Block:

    def __init__(self, color):
        self.color = color
        self.block_type = BlockType.get_block_type_from_color(color)
        self.block_array = self.block_type.default_block_array
        self.rotation_angle = 0
        self.offset = self.block_type.default_offset

    def set_offset(self, offset):
        # Sets the offset while forcing it to be on the board.
        self.offset = min((max(offset, 0)), BOARD_WIDTH - self.block_array.shape[1])

    def set_block_array(self, block_array):
        self.block_array = block_array

    def set_rotation_angle(self, rotation_angle):
        self.rotation_angle = rotation_angle % 360

    def _get_rotation_offset(self, current_angle, next_angle):
        current_offset = _COLOR_ROTATION_OFFSET_MAP[self.color][current_angle]
        next_offset = _COLOR_ROTATION_OFFSET_MAP[self.color][next_angle]
        return next_offset - current_offset

    def _rotate_right(self, times):
        times = times % 4
        rotation = times * 90
        last_rotation_angle = self.rotation_angle
        self.set_rotation_angle(
            rotation_angle = self.rotation_angle + rotation
        )
        self.set_block_array(
            block_array = np.rot90(self.block_array, times)
        )
        self.set_offset(
            offset = self.offset + self._get_rotation_offset(last_rotation_angle, self.rotation_angle)
        )

    def rotate_right(self):
        self._rotate_right(1)

    def rotate_180(self):
        self._rotate_right(2)

    def rotate_left(self):
        self._rotate_right(3)

    def _move(self, move_offset):
        self.set_offset(
            offset = self.offset + move_offset
        )

    def move_left(self):
        self.offset = self._move(-1)

    def move_right(self):
        self.offset = self._move(1)

    def __repr__(self):
        return f"""Block Type: {self.block_type.name}, 
Color: {self.color.name}, 
Rotation: {self.rotation_angle},
Block Array: 
{self.block_array}, 
Offset: {self.offset}"""
    
    def __str__(self):
        return self.__repr__()

_COLOR_ROTATION_OFFSET_MAP = {
	Color.LIGHT_BLUE: {
        0: 0,
        90: 2,
        180: 0,
        270: 1,
	},
	Color.YELLOW:  {
        0: 0,
        90: 0,
        180: 0,
        270: 0,
	},
	Color.PURPLE:  {
        0: 0,
        90: 1,
        180: 0,
        270: 0,
	},
	Color.GREEN:  {
        0: 0,
        90: 1,
        180: 0,
        270: 0,
	},
	Color.RED:  {
        0: 0,
        90: 1,
        180: 0,
        270: 0,
	},
	Color.BLUE:  {
        0: 0,
        90: 1,
        180: 0,
        270: 0,
	},
	Color.ORANGE:  {
        0: 0,
        90: 1,
        180: 0,
        270: 0,
	}, 
}
