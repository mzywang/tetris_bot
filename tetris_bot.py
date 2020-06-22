import pyautogui
import logging
import time
from datetime import datetime
import detector
import utils
from board import *


def decide_and_place(block, board):
    return


def main():
    utils.init_logger()
    board = Board()
    is_active = True

    while is_active:
        current_block, next_blocks = detector.get_next_blocks()
        print(f"Current block falling: {current_block}")
        print(board)
        if current_block is None:
            is_active = False
        else: 
            decide_and_place(current_block, board)

if __name__ == '__main__':
    main()
