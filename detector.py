import pyautogui
import logging
from block import *
from color import *
from constants import *

def _get_pixel(image, row, col):
    return image.getdata()[row * image.size[0] + col]

def _get_image_dim(image):
    return (image.size[1], image.size[0])

def _find_first_pixel(image, color, ignore_list):
    image_dim = _get_image_dim(image)
    for i in range(0, image_dim[0], GRAN):
        for j in range(0, image_dim[1], GRAN):
            if (i, j) not in ignore_list and _get_pixel(image, i, j) == color.value:
                return(i, j)
    return (-1, -1)

def _expand_and_track_helper(image, color, source, tracked):
    for i in ADJ_OFFSET:
        for j in ADJ_OFFSET:
            new_source = (source[0] + i, source[1] + j)
            new_pixel = _get_pixel(image, new_source[0], new_source[1])
            if new_source not in tracked and new_pixel == color.value:
                tracked.append(new_source)
                _expand_and_track_helper(image, color, new_source, tracked)
    return tracked

def _expand_and_track(image, color, source):
    tracked = [source]
    for i in ADJ_OFFSET:
        for j in ADJ_OFFSET:
            new_source = (source[0] + i, source[1] + j)
            new_pixel = _get_pixel(image, new_source[0], new_source[1])
            if new_source not in tracked and new_pixel == color.value:
                tracked.append(new_source)
                tracked = _expand_and_track_helper(image, color, new_source, tracked)
    return tracked

def _get_blocks_with_color(image, color):
    ignore_list = []
    blocks = {}
    block_loc = (0, 0)
    while block_loc != (-1, -1):
        block_loc = _find_first_pixel(image, color, ignore_list)
        block = _expand_and_track(image, color, block_loc)
        blocks[block_loc] = block
        ignore_list = ignore_list + block
    del blocks[(-1, -1)]
    return blocks

def get_next_blocks():
    ss = pyautogui.screenshot()
    all_blocks = {}
    for color in COLORS:
        blocks_by_color = _get_blocks_with_color(ss, color)
        for block in blocks_by_color:
            all_blocks[block] = {
                'color': color,
            }
    if all_blocks == {}:
        logging.warning("No blocks detected.")
        return (None, None)
    block_keys = list(all_blocks.keys())
    block_keys_by_width = sorted(block_keys, key=lambda tup: tup[1])
    if len(block_keys_by_width) <= LOOKAHEAD:
        logging.warning("Not enough blocks detected.")
        return (None, None)
    next_block_keys = sorted(block_keys_by_width[-LOOKAHEAD:], key=lambda tup: tup[0])
    current_block_key = sorted(block_keys_by_width[:-LOOKAHEAD], key=lambda tup: tup[0])[0]
    return (
        Block(all_blocks[current_block_key]['color']),
        [Block(all_blocks[block_key]['color']) for block_key in next_block_keys] 
    )

