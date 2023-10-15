# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:24:10 2023

@author: pepem
"""

class A:
    def speak(self):
        return 'A'
    
    def other_method(self):
        return 'Other Method'


class B(A):
    def speak(self):
        return super().speak()

class C:
    def speak(self):
        return 'C'
    
    def other_method(self):
        return 'Other Method'


class D(C):
    def speak(self):
        return super().speak()


# Pattern mixin permit us create child classes in an easier way
class SPEAK:
    def speak(self):
        return super().speak()

class E(SPEAK, A):
    pass

class F(SPEAK, C):
    pass


if __name__=='__main__':
    a = A()
    b = B()
    c = C()
    d = D()
    print(a.speak())
    print(b.speak())
    print(c.speak())
    print(d.speak())
    e = E()
    f = F()
    print(e.speak())
    print(f.speak())

