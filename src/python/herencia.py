# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:03:05 2023

@author: pepem
"""

class A: 
    pass

class B(A): 
    pass

class C(A): 
    pass

class D(B): 
    pass

class E(D): 
    pass

if __name__=='__main__':
    print("E.__base__:", E.__base__)
    print("E.__bases__:", E.__bases__)
    print("E.__dict__:", E.__dict__)
    print("E.__mro__:", E.__mro__)
    print("E.__class__:", E.__class__)
