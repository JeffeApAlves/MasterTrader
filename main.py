# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:17:08 2017

@author: Jefferson
"""

from Controller import Controller
import os

def main():
    clearConsole()
    controller = Controller()
    controller.startConsume()
    waitData()
    controller.stopConsume()
    clearConsole()

def waitData():
    while True:
        resp = input("Digite 'f' para finalizar ...")
        if resp in('f'):
            break
        
def clearConsole():
#    os.system('cls')    
    print(chr(27) + "[2J")
        
if __name__ == '__main__':
    main()
        
    