# Contexto de Aplicación y de Request

## El Contexto de la Aplicación

El contexto de la aplicación mantiene un seguimiento de los datos a nivel de aplicación durante una solicitud, comando CLI u otra actividad. En lugar de pasar la aplicación a cada función, se accede a los proxies **current_app** y **g**.

Esto es similar a **el contexto de la solicitud (Request)**, que mantiene un seguimiento de los datos a nivel de solicitud durante una petición. Un contexto de aplicación correspondiente se empuja cuando se empuja un contexto de solicitud.

### Proposito del contexto

El objeto de aplicación Flask tiene atributos, como config, que son útiles para acceder dentro de las vistas y los comandos CLI. Sin embargo, la importación de la instancia app dentro de los módulos de tu proyecto es propensa a problemas de importación circular. Cuando se utiliza el patrón app factory o se escriben blueprints o extensions no habrá ninguna instancia de app para importar.

Flask resuelve este problema con el contexto de aplicación. En lugar de referirse a una app directamente, se utiliza el proxy current_app, que apunta a la aplicación que maneja la actividad actual.

Flask automáticamente empuja un contexto de aplicación cuando maneja una solicitud. Las funciones de vista, los manejadores de errores y otras funciones que se ejecutan durante una solicitud tendrán acceso a current_app.

Flask también empujará automáticamente un contexto de aplicación cuando ejecute comandos CLI registrados con Flask.cli usando @app.cli.command().


- Cómo se manejan los objetos de request?
- Qué es el aplicacion context y request context?
- Qué información o data guarda cada uno?
- Cómo utilizamos `current_app`, `test_request_context` y `test_client` con los correctos contextos ?

 
A diferencia de Django y otros marcos web, las funciones de vista de Flask no 
aceptan un objeto de solicitud que contenga metadatos sobre la solicitud HTTP.


Ejemplo de Django


```python
def users(request):
    if request.method == 'POST':
         # Save the form data to the database
         # Send response
   else:
         # Get all users from the database
         # Send response
```

En Flask

```python
from flask import request

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
         # Save the form data to the database
         # Send response
    else:
         # Get all users from the database
         # Send response
```

En el ejemplo de Flask, 
el objeto de solicitud se ve, se siente y actúa como una variable global, pero NO lo es.

Si el objeto de solicitud(request) fuera una variable global, 
no podría ejecutar una aplicación Flask multiproceso 
ya que las variables globales no son seguras para subprocesos.


En cambio, Flask utiliza contextos para hacer que 
una serie de objetos "actúen" como globales solo 
para el contexto particular 
(un subproceso, un proceso o una corrutina) 
que se esté utilizando. 

En Flask, esto se denomina **contexto local**.


Las **variables locales de contexto** son similares, 
pero en última instancia diferentes, 
a la implementación local de subprocesos de Python 
para almacenar datos específicos de un subproceso. 
La implementación de Flask es más genérica 
para permitir que los trabajadores sean subprocesos,
 procesos o corrutinas.

## Datos almacenados en contextos de Flask


Cuando se recibe request(una solicitud), Flask proporciona dos contextos:

- **Aplicación**: Realiza un seguimiento de los datos a 
nivel de aplicación (variables de configuración, registrador, conexión a la base de datos)
    - `current_app`
    - `g`
- **Request o solicitud**
    - `request`
    - `session`

A estos objetos se les suele llamar `proxies`.



Flask se encarga de la creación de estos contextos 
cuando se recibe una solicitud. 
Pueden causar confusión, ya que no siempre se tiene 
acceso a un objeto en particular según el estado en 
el que se encuentre la aplicación.


## Ejemplo de contexto de aplicación


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido!'

if __name__ == '__main__':
    app.run()
```



