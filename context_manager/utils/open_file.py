# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:44:28 2019

@author: chitt
"""

class open_file():
    def __init__(self,file,mode):
        self.file = file
        self.mode = mode
        
    def __enter__(self):
        self.f = open(self.file,self.mode)
        return self.f
    
    def __exit__(self,exc_type,exc_val,traceback):
        self.f.close()