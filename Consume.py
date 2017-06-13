# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:56:55 2017

@author: Jefferson
"""

from pymongo import MongoClient
import pika
import logging
import json
from MongoDBConfig import MongoDBConfig
from RabbitMQConfig import RabbitMQConfig

class Consume(object):
    
    connection = pika.BlockingConnection(parameters=RabbitMQConfig.getConnectionParameters())    
    channel = connection.channel()
    client = MongoClient(MongoDBConfig.HOST,MongoDBConfig.PORT)
    collection_status = client.TradeDB.Status
    
    def __init__(self,symbol):
        self.symbol = symbol.lower()
        self.BasicConsume();
        self.collection_tick = Consume.client.TradeDB["Tick_"+self.symbol]
        self.collection_dom = Consume.client.TradeDB["DOM_"+self.symbol] 
        self.collection_history = Consume.client.TradeDB["HISTORY_"+self.symbol] 
        self.collection_trade = Consume.client.TradeDB["TradeSales_"+self.symbol] 

       
    def BasicConsume(self):
        Consume.channel.basic_consume(self.callbackTick,queue=self.getTickQueueName())
        Consume.channel.basic_consume(self.callbackBook,queue=self.getBookQueueName())
        Consume.channel.basic_consume(self.callbackHistory,queue=self.getHistoryQueueName())
        Consume.channel.basic_consume(self.callbackStatus,queue=self.getStatusQueueName())
        Consume.channel.basic_consume(self.callbackTrade,queue=self.getTradeQueueName())
        
    @staticmethod        
    def stop_consuming():
        Consume.channel.stop_consuming()
        Consume.channel.close()
        Consume.connection.close()

    @staticmethod        
    def start_consuming():
        Consume.channel.start_consuming()
        
    def getTickQueueName(self):
        return "tick."+ self.symbol
    
    def getBookQueueName(self):
        return "book."+ self.symbol
    
    def getHistoryQueueName(self):
        return "history."+ self.symbol
    
    def getStatusQueueName(self):
        return "status"
    
    def getTradeQueueName(self):
        return "trade."+ self.symbol

    def callbackTrade(self,ch, method, properties, body):
        print("[%r]:" % self.getTradeQueueName(),"%r" % body)        
        trade = json.loads(body.decode('utf-8'))       
        self.collection_trade.insert(trade)
        Consume.channel.basic_ack(delivery_tag = method.delivery_tag)
    
    def callbackTick(self,ch, method, properties, body):
        print("[%r]:" % self.getTickQueueName(),"%r" % body)        
        tick = json.loads(body.decode('utf-8'))       
        self.collection_tick.insert(tick)
        Consume.channel.basic_ack(delivery_tag = method.delivery_tag)

    def callbackHistory(self,ch, method, properties, body):
        print("[%r]:" % self.getHistoryQueueName(),"%r" % body)        
        history = json.loads(body.decode('utf-8'))       
        self.collection_history.insert(history)
        Consume.channel.basic_ack(delivery_tag = method.delivery_tag)
        
    def callbackBook(self,ch, method, properties, body):
        print("[%r]:" % self.getBookQueueName(),"%r" % body)
        book = json.loads(body.decode('utf-8'))
        self.collection_dom.insert(book)
        Consume.channel.basic_ack(delivery_tag = method.delivery_tag)

    def callbackStatus(self,ch, method, properties, body):
        print("[%r]:" % self.getStatusQueueName(),"%r" % body)
        status = json.loads(body.decode('utf-8'))
        self.collection_status.insert(status)
        Consume.channel.basic_ack(delivery_tag = method.delivery_tag)