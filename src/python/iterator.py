# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:12:24 2023

@author: pepemxl
"""

lista = [1,2,3,4,5,6,7,8,9,10]
iterador = lista.__iter__()
print(iterador)
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
try:
    print(iterador.__next__())
except:
    print("End of list")

