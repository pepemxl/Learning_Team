# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:29:57 2023

@author: pepem
"""
import time
#import datetime

NUMERO_DE_ELEMENTOS = 1000000
NUMERO_DE_REPETICIONES = 20
LISTA_INICIAL = [x for x in range(NUMERO_DE_ELEMENTOS)]

def f(x):
    return x*x+2*x+1


list_times = []

for i in range(NUMERO_DE_REPETICIONES):
    start = time.process_time()
    lista = [f(x) for x in LISTA_INICIAL]
    sum(lista)
    end = time.process_time()
    elapsed_time =  end - start
    list_times.append(elapsed_time)
print(sum(list_times)/float(NUMERO_DE_REPETICIONES))


list_times = []

for i in range(NUMERO_DE_REPETICIONES):
    start = time.process_time()
    conjunto = (f(x) for x in LISTA_INICIAL)
    sum(conjunto)
    end = time.process_time()
    elapsed_time =  end - start
    list_times.append(elapsed_time)
print(sum(list_times)/float(NUMERO_DE_REPETICIONES))
