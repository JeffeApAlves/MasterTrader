# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:31:16 2017

@author: Jefferson
"""

import pika

class RabbitMQConfig(object):
    
    EXCHANGE_MT = "mt5"
    EXCHANGE_MT_STATUS = "mt5.status"
    
    ROUTING_TICK = "tick"
    ROUTING_BOOK = "book"
    ROUTING_HISTORY = "history"
    ROUTING_ERROR = "error"

    EXCHANGE_TYPE_DIRECT = "direct"
    EXCHANGE_TYPE_FANOUT = "fanout"
    EXCHANGE_TYPE_TOPIC = "topic"
    
    HOST = "localhost"
#    HOST = '192.168.0.104'
    USER = "rna"
    PW = "rna@1981"
    VHOST = "/"
    PORT = 5672
 
    @staticmethod    
    def getConnectionParameters():    

        credentials = pika.PlainCredentials(RabbitMQConfig.USER, RabbitMQConfig.PW)
        params = pika.ConnectionParameters(RabbitMQConfig.HOST,RabbitMQConfig.PORT,RabbitMQConfig.VHOST,credentials,socket_timeout=1000,heartbeat_interval=200)
      
        return params

    