import numpy as np
from constants import * 

class Board:
    
    def __init__(self):
        self.state = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
        self.state[19, 4] = 1

    def place_block(self, block_orientation, block_offset):
        block_height = block_orientation.shape[0]
        block_width = block_orientation.shape[1]
        block_columns = self.state[:, block_offset : block_offset + block_width]
        board_heights = [
            BOARD_HEIGHT - np.where(array == 1)[0][0]
                if len(np.where(array == 1)[0]) > 0 else 0 
                for array in block_columns.T
        ]
        block_heights = [
            np.where(array[::-1] == 1)[0][0]
            for array in block_orientation.T
        ]
        combined_heights = [board_heights[i] - block_heights[i] for i in range(block_width)]
        placement_height = max(combined_heights)
        for i in range(block_height)[::-1]:
            for j in range(block_width):
                if block_orientation[i][j]:
                    self.state[BOARD_HEIGHT - (placement_height + block_height - i)][block_offset + j] = 1

        return self.state
