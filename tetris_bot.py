import pyautogui
import logging
import time
from datetime import datetime
import detector
import utils
from board import *
from block import *
from color import *

def decide_and_place(block, board):
    """
    Blocks have the following attributes:
     - color: color of the block (blue, green, etc.)
     - block_type: type of block (J, Z, etc.) which corresponds to the color
     - array: a mxn array where 1's space the block occupies and 0's represent empty space
     - rotation_angle: 0, 90, 180, 270 depending on the rotation of the block
     - offset: number of empty blocks from the LHS of the board to the RHS of the block
    """
    return

def main():
    utils.init_logger()
    board = Board()
    is_active = False 

    while is_active:
        current_block, next_blocks = detector.get_next_blocks()
        logging.info(f"Current block falling: {current_block}")
        logging.debug(board)
        if current_block is None:
            is_active = False
        else: 
            decide_and_place(current_block, board)

if __name__ == '__main__':
    main()
