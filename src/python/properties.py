# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:46:36 2023

@author: pepemxl
"""




class A:
    __slots__ = ('_x','_y','_z', 'new_variable')
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.new_variable = 10
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value
        
if __name__ == '__main__':
    a = A(1,2,3)
    print(a.x)
    print(a.y)
    print(a.z)
    a.x = 4
    a.y = 5
    a.z = 6
    print(a.x)
    print(a.y)
    print(a.z)
    a._x = 7
    a._y = 8
    a._z = 9
    print(a.x)
    print(a.y)
    print(a.z)
    try:
        a.new_variable = 10
    except:
        print("Protection")
    try:
        a.new_variable2 = 10
    except:
        print("Protection new_variable2 does not exist")
    try:
        print(a.__dict__)
    except:
        print("Not dict structure in class A")