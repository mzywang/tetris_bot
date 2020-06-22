import numpy as np
import pyautogui
from config import * 

class Board:
    
    def __init__(self):
        self.state = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)

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

        # Tell pyautogui to place the block
        if KEYBOARD_ACTIVE:
            pyautogui.write([HARD_DROP_KEY])

        # Clear lines in board state 
        for i in range(BOARD_HEIGHT):
            if min(self.state[i, :]) == 1:
                self.state = np.concatenate((np.zeros((1, BOARD_WIDTH), dtype=int), self.state[0:i, :], self.state[i + 1:, :]))
        return self.state

    def __repr__(self):
        return "\nCurrent Board:\n" + "\n".join([" ".join([str(val) for val in self.state[i, :].tolist()]) for i in range(BOARD_HEIGHT)])

    def __str__(self):
        return self.__repr__()
