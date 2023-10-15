# -*- coding: utf-8 -*-

"""
Anotations dont block code from run, however we can use library: mypy
to check static code anotations.

mypy anotations.py
anotations.py:17: error: Argument 1 to "myFunction" has incompatible type "int"; expected "str"  [arg-type]
anotations.py:17: error: Argument 2 to "myFunction" has incompatible type "int"; expected "str"  [arg-type]
anotations.py:19: error: Argument 1 to "myFunction2" has incompatible type "str"; expected "int"  [arg-type]
anotations.py:19: error: Argument 2 to "myFunction2" has incompatible type "str"; expected "int"  [arg-type]
Found 4 errors in 1 file (checked 1 source file)
"""

def myFunction(name:str, lastname:str)->str:
    return name +lastname


def myFunction2(a:int, b:int)->int:
    return a+b


if __name__=='__main__':
    print(myFunction(1, 2))
    print(myFunction2(1, 2))
    print(myFunction2("1", "2"))
