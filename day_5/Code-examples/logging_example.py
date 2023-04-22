''' The basics of logging and debugging in Python'''

# This was broken during class because I broke a cardinal rule of python naming conventions. I named a file logging.py and then tried to import logging.
# In doing so I overwrote the logging module with my own file. This is why I had to rename the file to logging_example.py

import logging, datetime
from logging import handlers

# several levels of logging
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create two functions one to create a file handler and another to create a rotating file handler

def create_file_handler():
    '''Create a file handler for the logger'''
    file_handler = logging.FileHandler('./logs/file.txt')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
    return file_handler

def create_rotating_file_handler():
    '''Create a rotating file handler for the logger'''
    rotating_file_handler = handlers.RotatingFileHandler('./logs/rotating_file.txt', maxBytes=2000, backupCount=5)
    rotating_file_handler.setLevel(logging.WARNING)
    rotating_file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
    return rotating_file_handler

# Add the handlers to the logger
logger.addHandler(create_file_handler())
logger.addHandler(create_rotating_file_handler())

# Create a function to get the nth fibonacci number
def fibonacci(n):
    '''Returns the nth fibonacci number'''
    logger.debug(f'Calculating the {n} fibonacci number')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# output the first 10 fibonacci numbers to the log file
for i in range(10):
    logger.debug(f'The {i} fibonacci number is {fibonacci(i)}')
    logger.error(f'The {i} fibonacci number is {fibonacci(i)}')
    logger.warning(f'The {i} fibonacci number is {fibonacci(i)}')
    logger.info(f'The {i} fibonacci number is {fibonacci(i)}')
    logger.critical(f'The {i} fibonacci number is {fibonacci(i)}')