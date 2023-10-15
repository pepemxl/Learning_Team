"""
The inspect module helps in checking the objects present in the code that we have written. 
As Python is an OOP language and all the code that is written is basically an interaction 
between these objects, hence the inspect module becomes very useful in inspecting certain 
modules or certain objects. We can also use it to get a detailed analysis of certain 
function calls or tracebacks so that debugging can be easier.

The inspect module provides a lot of methods, these methods can be classified into two categories i.e. 
- methods to verify the type of token and 
- methods to retrieve the source of token. 

"""
import inspect
import math

class A(object):
    pass

class B(A):
    pass

class C(B):
    pass


if __name__=='__main__':
    print(inspect.getmro(C)) 
    print(inspect.isclass(A))
    for i in (inspect.getclasstree(inspect.getmro(C))):
        print(i)
    print(inspect.getmembers(math))