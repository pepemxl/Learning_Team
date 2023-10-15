# Celery

Celery es una herramienta de programación en cola para Python que se utiliza para ejecutar tareas en segundo plano y programar trabajos en el futuro. Flask es un marco web para Python que se utiliza para desarrollar aplicaciones web de forma rápida y sencilla.

Para utilizar Celery con Flask, primero debes instalar Celery y Flask en tu sistema, junto con cualquier otro módulo o dependencia que necesiten. Una vez instalados, puedes utilizar Celery en una aplicación Flask de la siguiente manera:

1. Crea una instancia de Flask y configúrala para que use Celery. Esto puede hacerse en el archivo app.py de la aplicación Flask:

```python
from flask import Flask
from celery import Celery

app = Flask(__name__)

# Configura Celery con la aplicación Flask
celery = Celery(app.name, broker='redis://localhost:6379/0')
```

2. Define una tarea en Celery. Las tareas son funciones que se ejecutan en segundo plano y que pueden ser invocadas desde Flask. Puedes definir una tarea en Celery en un archivo separado, como tasks.py:

```python
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def long_task():
    # Realiza una tarea larga y compleja en segundo plano
    # ...
    return result


```

La tarea se define con la función @celery.task, que indica a Celery que esta función se ejecutará en segundo plano cuando se invoque. La tarea puede realizar cualquier cómputo largo y complejo que necesites, y puede devolver un resultado al finalizar.


3. Invoca la tarea desde Flask. Una vez que hayas definido una tarea en Celery, puedes invocarla desde Flask en cualquier momento en tu código. Por ejemplo, puedes crear una ruta en Flask que invoque la tarea cuando se acceda a ella mediante una solicitud HTTP:

```python
from flask import Flask
from tasks import long_task

app = Flask(__name__)

@app.route('/start_task')
def start_task():
    # Inicia la tarea en segundo plano
    result = long_task.delay()
    return 'Tarea en curso'
```
En este ejemplo, la ruta /start_task invoca la tarea long_task cuando se accede a ella mediante una solicitud HTTP. La tarea se ejecutará en segundo plano, lo que permite que Flask maneje otras solicitudes mientras la tarea se está ejecutando.

Esta es una forma básica de utilizar Celery con Flask. Puedes utilizar Celery de muchas otras formas en una aplicación Flask, como programar trabajos en el futuro o recibir notificaciones cuando una tarea se complete.



