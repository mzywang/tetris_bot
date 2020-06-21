import logging
from datetime import datetime

def init_logger():
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)s]  %(message)s")
    rootLogger = logging.getLogger()

    dt_string = datetime.now().strftime("%d%m%Y%H%M%S")
    fileHandler = logging.FileHandler(f"logs/{dt_string}.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

