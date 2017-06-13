# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:24:44 2017

@author: Jefferson
"""

class Ibovespa(object):
    
    CARTEIRA_NAME = ["ABEV3","BBAS3","BBDC3","BBDC4","BBSE3","BRAP4","BRFS3","BRKM5","BRML3","BVMF3","CCRO3","CIEL3",
"CMIG4","CPFE3","CPLE6","CSAN3","CSNA3","CYRE3","ECOR3","EGIE3","ELET3","ELET6","EMBR3","ENBR3","EQTL3","ESTC3",
"FIBR3","GGBR4","GOAU4","HYPE3","ITSA4","ITUB4","JBSS3","KLBN11","KROT3","LAME4","LREN3","MRFG3","MRVE3","MULT3",
"NATU3","PCAR4","PETR3","PETR4","QUAL3","RADL3","RAIL3","RENT3","SANB11","SBSP3","SMLE3","SUZB5","TIMP3","UGPA3",
"USIM5","VALE3","VALE5","VIVT4","WEGE3","WINM17","IBOV"]

   
    @staticmethod
    def getSymbol(index):
        return Ibovespa.CARTEIRA_NAME[index]
    
    @staticmethod
    def getSize():
        return len(Ibovespa.CARTEIRA_NAME)
        