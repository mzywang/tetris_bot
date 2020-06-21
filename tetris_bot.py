import pyautogui
import logging
import time
from datetime import datetime
from detector import *
from utils import *

init_logger()
current_block, next_blocks = get_next_blocks()
print(f"Current block falling: {current_block}")
print(f"Next blocks: {next_blocks}")


