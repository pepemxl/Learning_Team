#import ctypes
#import sys

# Cargar ambas librerías dinámicas
#math_lib = ctypes.CDLL('libmath_operations.so')
#string_lib = ctypes.CDLL('libstring_operations.so')
import ctypes
import os
#from ctypes.util import find_library

# Configurar la ruta de búsqueda de librerías
os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib:' + os.environ.get('LD_LIBRARY_PATH', '')

# Intentar cargar las librerías de múltiples ubicaciones posibles
try:
    math_lib = ctypes.CDLL('math_operations.so')
except OSError:
    # Si falla, intentar con la ruta completa
    math_lib = ctypes.CDLL('/usr/local/lib/math_operations.so')

try:
    string_lib = ctypes.CDLL('string_operations.so')
except OSError:
    string_lib = ctypes.CDLL('/usr/local/lib/libstring_operations.so')


# Definir los tipos de argumentos y retorno para las funciones de math_lib
math_lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
math_lib.add.restype = ctypes.c_int
math_lib.subtract.argtypes = [ctypes.c_int, ctypes.c_int]
math_lib.subtract.restype = ctypes.c_int

# Definir los tipos para las funciones de string_lib
string_lib.reverse_string.argtypes = [ctypes.c_char_p]
string_lib.reverse_string.restype = None
string_lib.to_uppercase.argtypes = [ctypes.c_char_p]
string_lib.to_uppercase.restype = None

# Usar las funciones de math_operations
print("=== Math Operations ===")
a, b = 10, 5
print(f"{a} + {b} = {math_lib.add(a, b)}")
print(f"{a} - {b} = {math_lib.subtract(a, b)}")

# Usar las funciones de string_operations
print("\n=== String Operations ===")
original_str = "Hello World!".encode('utf-8')
buffer = ctypes.create_string_buffer(original_str)

print(f"Original: {buffer.value.decode('utf-8')}")

string_lib.reverse_string(buffer)
print(f"Reversed: {buffer.value.decode('utf-8')}")

string_lib.to_uppercase(buffer)
print(f"Uppercase: {buffer.value.decode('utf-8')}")