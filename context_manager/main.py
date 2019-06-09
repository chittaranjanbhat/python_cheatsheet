# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:03:04 2019

@author: chitt
"""

from contextlib import contextmanager
from utils import open_file as of

@contextmanager
def open_file(file,mode):
    f = open(file,mode)
    yield f
    f.close()

if __name__ == "__main__":
    #------Using function for contex management----------
    for i in range(10):
        with open_file('test.txt','a+') as f:
            f.write(f'Writing using contextmanager : {i}\n')
        
        print(f.closed)
        
    #-----Using Class for contex management----------

    for i in range(10):
        with of.open_file('test.txt','a+') as f:
            f.write(f'wrting using class as context manager : {i}\n')
            
        print(f.closed)
         