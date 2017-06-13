# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:53:24 2017

@author: Jefferson
"""

import logging
import threading
from Ibovespa import Ibovespa
from Consume import Consume


class Controller(threading.Thread):
    
    count = 0
    
    listSymbols = []

    def __init__(self):
        threading.Thread.__init__(self)        
        self.threadID = self.count
        self.count+=1
        self.name = "Consuming"

    
    def createConsume(self):
        for i in range(0,Ibovespa.getSize()):
            self.listSymbols.append(Consume(Ibovespa.getSymbol(i)))
            
    def startConsume(self):
        self.start()

        
    def stopConsume(self):
        Consume.stop_consuming()
            
    def run (self):
        print("Start thread %r. Creating consumes" % self.name)        
        self.createConsume()
        print("Esperando dados")
        Consume.start_consuming()
        
        
        
          
