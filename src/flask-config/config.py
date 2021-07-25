# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:22:48 2021

@author: Pepe
"""


class Config(object): 
    pass 
 
class ProdConfig(Config): 
    pass 
 
class DevConfig(Config): 
    DEBUG = True
