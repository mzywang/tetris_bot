import pyautogui
import logging
import time
from datetime import datetime
import detector
import utils
from board import *
from block import *
from color import *
from config import *

def decide_and_place(block, board):
    """
    Blocks have the following attributes:
     - color: color of the block (blue, green, etc.)
     - block_type: type of block (J, Z, etc.) which corresponds to the color
     - array: a mxn array where 1's space the block occupies and 0's represent empty space
     - rotation_angle: 0, 90, 180, 270 depending on the rotation of the block
     - offset: number of empty blocks from the LHS of the board to the RHS of the block
    """

    # moves the block left one space
    # block.move_left() 

    # moves the block right one space
    # block.move_right() 

    # rotates the block right by 90 degrees
    # block.rotate_left()

    # rotates the block left by 90 degrees
    # block.rotate_right()

    # place (hard drop) the block
    # board.place_block(block)

    # Example: If the block is I shaped, put it on the right, else put it on the left
    if block.color == Color.LIGHT_BLUE:
        block.move_right(5)
        board.place_block(block)
    else:
        block.move_left(5)
        board.place_block(block)

    return

def main():
    utils.init_logger()
    board = Board()
    is_active = True 
    has_started = False
    time.sleep(START_DELAY)

    while is_active:
        current_block, next_blocks = detector.get_next_blocks()
        logging.info(f"Current block falling: {current_block}")
        logging.debug(board)
        if current_block is None and not has_started:
            logger.info("Waiting for game to start.")
            time.sleep(START_DELAY)
        elif current_block is None and has_started: 
            logger.info("Game has ended.")
            is_active = False
        else:
            has_started = True
            decide_and_place(current_block, board)
            time.sleep(ACTION_DELAY)

if __name__ == '__main__':
    main()
