import numpy as np
from constants import * 

class Board:
    
    def __init__(self):
        self.state = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))

    def place_block(self, block):
        block_height = block.array.shape[0]
        block_width = block.array.shape[1]
        block_columns = self.state[:, block.offset : block.offset + block_width]
        board_heights = [
            BOARD_HEIGHT - np.where(array == 1)[0][0]
                if len(np.where(array == 1)[0]) > 0 else 0 
                for array in block_columns.T
        ]
        block_heights = [
            np.where(array[::-1] == 1)[0][0]
            for array in block.array.T
        ]
        combined_heights = [board_heights[i] - block_heights[i] for i in range(block_width)]
        placement_height = max(combined_heights)
        for i in range(block_height)[::-1]:
            for j in range(block_width):
                if block.array[i][j]:
                    self.state[BOARD_HEIGHT - (placement_height + block_height - i)][block.offset + j] = 1

        return self.state

    def __repr__(self):
        return "\n".join([" ".join([str(int(val)) for val in self.state[i, :].tolist()]) for i in range(BOARD_HEIGHT)])

    def __str__(self):
        return self.__repr__()
