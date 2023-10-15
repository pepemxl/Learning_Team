# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:18:48 2023

@author: pepemxl
"""
class StaticVar:
    var1 = 10
    def __init__(self):
        self.var2 = 11

    #@staticmethod
    @classmethod
    def print_text(cls, text):
        print("This class will print text: '{0}'.".format(text))

StaticVar.print_text("Static Method")
print(StaticVar.var1)
try:
    print(StaticVar.var2)
except AttributeError:
    print("EXception: var2 is not static")
SV = StaticVar()
print("Value in instance object: {0}".format(SV.var2))


class StaticVar2:
    
    @classmethod
    def print_text(self, text):
        print("This class will print text '{0}'.".format(text))
        
StaticVar2.print_text("Sample text")



