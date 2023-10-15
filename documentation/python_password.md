# Como guardaremos contraseñas de usuarios sin temor a que estas sean filtradas (leaking) por nuestros sistema


Evitar el almacenamiento de contraseñas en texto sin formato es una buena práctica conocida. Con el software, por lo general, solo necesitamos verificar si la contraseña proporcionada por el usuario es correcta y para ello utilizamos el hash de la contraseña, la cual podemos almacenar y comparar con el hash de la contraseña proporcionada al momento de loguearse. Si los dos hashes coinciden, las contraseñas son iguales; si no lo hacen, la contraseña proporcionada es incorrecta.

Almacenar contraseñas es una práctica bastante estándar. Usualmente una cadena generada semi-aleatoriamente se une con la contraseña antes del hash. Al generarse semi-aleatoriamente, garantiza que incluso los hashes de contraseñas iguales obtengan resultados diferentes.

La biblioteca estándar de Python proporciona un conjunto bastante completo de funciones hash, algunas de ellas muy adecuadas para almacenar contraseñas.

Python 3 introduce funciones especialmente utiles para almacenar contraseñas. Se proporcionan tanto `pbkdf2` como `scrypt`. Si bien `scrypt` es más resistente contra los ataques, ya que requiere mucha memoria y CPU, solo funciona en sistemas que proporcionan OpenSSL 1.1+, mientras que `pbkdf2` funciona en cualquier sistema, en el peor de los casos, se utiliza un respaldo proporcionado por Python.



```python
import hashlib, binascii, os

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  password.encode('utf-8'), 
                                  salt, 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

if __name__ == '__main__':
    #stored_password = hash_password("Hola Mundo")
    stored_password = "6dd77d6cd1d268f64ad8c98d100dbb59b504d6315255a3d11e6a5e146f79904a215c9ba84a102800a4a98e2cd3493d4e1a180010272f2209aaadd2cd61cf6b733ea93338fd41748ed6f58895c7f3f95816872adb078a63d94ef4419c1d1f5ff3"
    provided_password = "Hola Mundo"
    print(verify_password(stored_password, provided_password))
```

```python
True
```


## Qué brujeria es esta?


- `hash_password`: Codifica una contraseña proporcionada de una manera segura para almacenar en una base de datos o archivo
- `verify_password`: dada una contraseña codificada y una de texto sin formato proporcionada por el usuario, verifica si la contraseña proporcionada coincide con la codificada

`hash_password` en realidad hace varias cosas; no solo codifica la contraseña. Lo primero que hace es generar algo de sal aleatoria que debe agregarse a la contraseña. Eso es solo el hash sha256 de algunos bytes aleatorios leídos de os.urandom. Luego extrae una representación de cadena de la sal hash como un conjunto de números hexadecimales (hexdigest).

Luego, la sal se proporciona a pbkdf2_hmac junto con la contraseña para codificar la contraseña de forma aleatoria. Como pbkdf2_hmac requiere bytes como entrada, las dos cadenas (contraseña y sal) se codifican previamente en bytes puros. El salt está codificado como ASCII simple, ya que la representación hexadecimal de un hash solo contendrá los caracteres 0-9 y A-F. Si bien la contraseña está codificada como utf-8, podría contener cualquier carácter. (¿Hay alguien con emojis en sus contraseñas?)

El pbkdf2 resultante es un montón de bytes, ya que desea almacenarlo en una base de datos; usa binascii.hexlify para convertir el grupo de bytes en su representación hexadecimal en un formato de cadena. Hexlify es una forma conveniente de convertir bytes en cadenas sin perder datos. Simplemente imprime todos los bytes como dos dígitos hexadecimales, por lo que los datos resultantes serán el doble de grandes que los datos originales, pero aparte de esto, son exactamente iguales a los datos convertidos.

Al final, la función une el hash con su sal. Como sabe que el resumen hexadecimal de un hash sha256 (la sal) siempre tiene 64 caracteres, al unirlos, puede recuperar la sal leyendo los primeros 64 caracteres de la cadena resultante. Esto permitirá verificar_contraseña para verificar la contraseña y verificar si se requiere la sal utilizada para codificarla.

Una vez que tenga su contraseña, verificar_contraseña se puede usar para verificar las contraseñas proporcionadas. Por lo tanto, toma dos argumentos: la contraseña codificada y la nueva contraseña que debe verificarse. Lo primero que hace verificar_contraseña es extraer la sal de la contraseña cifrada (recuerde, la colocó como los primeros 64 caracteres de la cadena resultante de hash_contraseña).

La sal extraída y la contraseña candidata luego se proporcionan a pbkdf2_hmac para calcular su hash y luego convertirlo en una cadena con binascii.hexlify. Si el hash resultante coincide con la parte hash de la contraseña previamente almacenada (los caracteres después de la sal), significa que las dos contraseñas coinciden.

Si el hash resultante no coincide, significa que la contraseña proporcionada es incorrecta. Como puede ver, es muy importante que haga que el salt y la contraseña estén disponibles juntos, porque los necesitará para poder verificar la contraseña y un salt diferente daría como resultado un hash diferente y, por lo tanto, nunca podría para verificar la contraseña.



