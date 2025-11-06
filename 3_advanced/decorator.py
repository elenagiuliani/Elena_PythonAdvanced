# ADVANCED ***************************************************************************
# content = assignment
#
# modified by = Elena Giuliani
#
# date    = 2025-10-31
# email   = contact@alexanderrichtertd.com
#************************************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""

import time
import logging
#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        print(f'\nSTART - {func.__name__} **********')
        func(*args)                  # main_function

        if __name__ == "__main__":
            format = "%(message)s %(asctime)s *****************"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            logging.info("END -")

    return wrapper

#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)

@print_process
def mid_sleeping(name):
    time.sleep(2)
    print(name)

@print_process
def long_sleeping(name):
    time.sleep(4)
    print(name)


short_sleeping("so sleepy")

mid_sleeping("goodnight")

long_sleeping("I'm dreaming")
















#******************************************************************************************************************************
#******************************************************************************************************************************
# from Alex
import time
#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        func(arg)                  # main_function
    return wrapper

#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)

def mid_sleeping():
    time.sleep(2)

def long_sleeping():
    time.sleep(4)

#short_sleeping("so sleepy")

