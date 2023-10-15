# Librerías en  Python

Uno de los problemas comunes cuando un proyecto crece es tener en nuestro código base librerías que caen en desuso por muchas razones, una de las tareas a realizar para un buen mantenimiento del código es limpiarlas de nuestro código base.

Una libreria util para examinar las dependencias es `pipdeptree`

```bash
pip install pipdeptree
pipdeptree
```

## Vulture 

- [https://github.com/jendrikseipp/vulture](https://github.com/jendrikseipp/vulture)

`pip install vulture`

```bash
vulture myscript.py  # or
python3 -m vulture myscript.py
vulture myscript.py mypackage/
vulture myscript.py --min-confidence 100  # Only report 100% dead code.
```





The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.


Lets do some experiment with similar libraries boto and boto 3

- Successfully installed 
    - boto-2.49.0
- Successfully installed 
    - boto3-1.28.53 
    - botocore-1.31.53 
    - jmespath-1.0.1 
    - python-dateutil-2.8.2 
    - s3transfer-0.6.2 
    - six-1.16.0 
    - urllib3-1.26.16
- Successfully installed 
    - Jinja2-3.1.2 
    - MarkupSafe-2.1.3 
    - Werkzeug-2.3.7 
    - blinker-1.6.2 
    - click-8.1.7 
    - colorama-0.4.6 
    - flask-2.3.3 
    - importlib-metadata-6.8.0 
    - itsdangerous-2.1.2 
    - zipp-3.17.0


## Going to the 
/app # pip list
Package            Version
------------------ -------
boto               2.49.0
boto3              1.28.53
botocore           1.31.53
click              8.1.7
Flask              2.2.5
importlib-metadata 6.7.0
itsdangerous       2.1.2
Jinja2             3.1.2
jmespath           1.0.1
MarkupSafe         2.1.3
pip                23.0.1
python-dateutil    2.8.2
s3transfer         0.6.2
setuptools         57.5.0
six                1.16.0
typing_extensions  4.7.1
urllib3            1.26.16
Werkzeug           2.2.3
wheel              0.41.1
zipp               3.15.0


## Working with Modules

`sys.path`` is a built-in variable within the sys module that returns the list of directories that the interpreter will search for the required module. 

When a module is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories defined by sys.path.

Note: sys.path is an ordinary list and can be manipulated.


### Reference Count

`sys.getrefcount()` method is used to get the reference count for any given object. This value is used by Python as when this value becomes 0, the memory for that particular value is deleted.





|Function|Description|
|---|---|
|sys.setrecursionlimit()|	sys.setrecursionlimit() method is used to set the maximum depth of the Python interpreter stack to the required limit.|
|sys.getrecursionlimit()| method	sys.getrecursionlimit() method is used to find the current recursion limit of the interpreter or to find the maximum depth of the Python interpreter stack.|
|sys.settrace()|	It is used for implementing debuggers, profilers and coverage tools. This is thread-specific and must register the trace using threading.settrace(). On a higher level, sys.settrace() registers the traceback to the Python interpreter|
|sys.setswitchinterval()| method	sys.setswitchinterval() method is used to set the interpreter’s thread switch interval (in seconds).|
|sys.maxsize()|	It fetches the largest value a variable of data type Py_ssize_t can store.|
|sys.maxint|	maxint/INT_MAX denotes the highest value that can be represented by an integer.|
|sys.getdefaultencoding()| method	sys.getdefaultencoding() method is used to get the current default string encoding used by the Unicode implementation.|




## Python – sys.settrace()


Python sys module provides some of the powerful functions but they are complex to understand. One of which is the sys.settrace() which is used for implementing debuggers, profilers and coverage tools. This is thread-specific and must register the trace using threading.settrace().

Knowing how the function works internally is really important in case you are planning to create your own debugger.

On a higher level, sys.settrace() registers the traceback to the Python interpreter. A traceback is basically the information that is returned when an event happens in the code. You might have seen traceback when your code has some error or an exception is raised.

The registered traceback is invoked when one of the following four events occur :




Function is called
Function returns
Execution of a line
Exception is raised
Syntax: sys.settrace(frame, event, arg.frame)

Parameters:
frame: frame is the current stack frame
event: A string which be either 'call', 'line', 'return', 'exception' or 'opcode'
arg: Depends on the event type

Returns: Reference to the local trace function which then returns reference to itself.


```python
# program to display the functioning of
# settrace()
from sys import settrace


# local trace function which returns itself
def my_tracer(frame, event, arg = None):
	# extracts frame code
	code = frame.f_code

	# extracts calling function name
	func_name = code.co_name

	# extracts the line number
	line_no = frame.f_lineno

	print(f"A {event} encountered in \
	{func_name}() at line number {line_no} ")

	return my_tracer


# global trace function is invoked here and
# local trace function is set for fun()
def fun():
	return "GFG"


# global trace function is invoked here and
# local trace function is set for check()
def check():
	return fun()


# returns reference to local
# trace function (my_tracer)
settrace(my_tracer)

check()

```


A call encountered in check() at line number 30 
A line encountered in check() at line number 31 
A call encountered in fun() at line number 24 
A line encountered in fun() at line number 25 
A return encountered in fun() at line number 25 
A return encountered in check() at line number 31 
You might be wondering why does the local function my_code returns itself?
The reason is hidden in the functioning of sys.settrace(). What sys.settrace does is that it first registers a global trace which is called whenever a frame is created which returns our local trace function my_trace whenever any one of the above mentioned event occurs. For better understanding look at the image shown below:



If we don’t want our scope to be traced then None should be returned but if that is not the case we might want to do the same with our local trace function then it should return None else if there is an error then settrace(None) is automatically called.

Note : There is a function named gettrace available in sys module to get the trace set by sys.settrace()

