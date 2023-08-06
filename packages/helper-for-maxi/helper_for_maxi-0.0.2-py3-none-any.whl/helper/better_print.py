import sys
import time


def better_print(text=' ', delay=.1, end='\n'):
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print('', end=end)