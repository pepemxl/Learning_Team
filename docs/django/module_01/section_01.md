# Django


Podemos descomponer django en los siguientes componentes:

- Solicitudes y Respuestas
- Modelos
- Vistas y Plantillas
- Formularios

## Modelos

Django proporciona una capa de abstracción (los **modelos**) para estructurar y manipular los datos de su aplicación web. 

La capacidad de definir modelos y sus relaciones (como **joins**) antes de que los datos existan en la base de datos se conoce como **"Modelos ORM"** (Object-Relational Mapping, o Mapeo Objeto-Relacional). Más específicamente, esta práctica se refiere a la definición de **esquemas de base de datos** mediante clases de modelos en Django, que permiten estructurar y relacionar datos sin necesidad de que estos existan previamente.

Este enfoque se basa en el **ORM de Django**, que actúa como una capa de abstracción entre el código Python y la base de datos. Los modelos se definen en código Python, especificando campos y relaciones (como `ForeignKey`, `OneToOneField` o `ManyToManyField` para **joins**), y Django genera automáticamente las tablas y las consultas SQL correspondientes cuando se ejecutan las migraciones (`makemigrations` y `migrate`).


## Querysets

En Django, un **QuerySet** es un objeto que representa una consulta a la base de datos, permitiendo interactuar con los datos de los modelos de manera eficiente y expresiva. Es una colección de objetos obtenidos de la base de datos que puedes filtrar, ordenar, modificar o iterar, todo sin escribir SQL directamente, gracias al **ORM** (Object-Relational Mapping) de Django.

### Características principales de los QuerySets

1. **Lazy evaluation**: Un QuerySet no ejecuta la consulta en la base de datos hasta que se "evalúa" (por ejemplo, al iterar, convertir a lista, o acceder a los resultados). Esto permite encadenar filtros y optimizar consultas.
   - Ejemplo: `Usuarios.objects.filter(edad__gt=18)` no ejecuta la consulta hasta que se itera o se accede al resultado.
2. **Encadenables**: Puedes combinar métodos como `.filter()`, `.exclude()`, `.order_by()`, etc., para construir consultas complejas.
   - Ejemplo: `Usuarios.objects.filter(edad__gt=18).order_by('nombre')`.
3. **Métodos comunes**:
   - `filter()`: Filtra objetos según condiciones.
   - `exclude()`: Excluye objetos que cumplan ciertas condiciones.
   - `get()`: Obtiene un único objeto que coincida con los criterios (lanza una excepción si no encuentra uno o encuentra más).
   - `all()`: Devuelve todos los objetos del modelo.
   - `count()`: Cuenta los resultados sin recuperarlos.
   - `first()` / `last()`: Obtiene el primer o último objeto.
4. **Relaciones**: Permiten realizar **joins** implícitos entre modelos relacionados (usando `ForeignKey`, `ManyToManyField`, etc.).
   - Ejemplo: `Libro.objects.filter(autor__nombre="Pepe")` accede a los libros de un autor específico.
5. **Optimización**: Métodos como `select_related()` y `prefetch_related()` optimizan consultas para evitar accesos innecesarios a la base de datos.

```python title="Ejemplo" linenums="1"
from mi_app.models import Usuario

# Crear un QuerySet
queryset = Usuario.objects.filter(edad__gte=18)

# Aplicar más filtros
queryset = queryset.exclude(nombre__startswith='A')

# Iterar sobre los resultados
for usuario in queryset:
    print(usuario.nombre)

# Contar resultados
total = queryset.count()
print(total)
```

Los **QuerySets** son la herramienta principal de Django para consultar y manipular datos de la base de datos de forma programática, aprovechando el poder del ORM para abstraer las operaciones SQL.

## Instancias de modelos

En Django, una **instancia de modelo** es un objeto individual creado a partir de una clase de modelo definida en el ORM (Object-Relational Mapping). Representa una fila específica en la tabla de la base de datos correspondiente al modelo. Cada instancia contiene los datos de los campos definidos en el modelo y permite interactuar con esos datos en Python, como si fueran atributos de un objeto.

### Características clave de las instancias de modelos

1. **Representación de una fila**: Una instancia de modelo corresponde a un registro único en la tabla de la base de datos asociada al modelo.
   - Ejemplo: Si tienes un modelo `Usuario` con campos `nombre` y `edad`, una instancia podría ser un usuario específico, como `nombre="Pepe"` y `edad=41`.
2. **Creación**: Puedes crear una instancia de modelo de varias formas:
   - Directamente: `usuario = Usuario(nombre="Pepe", edad=41)`
   - Desde la base de datos: `usuario = Usuario.objects.get(id=1)`
3. **Manipulación**: Las instancias permiten leer, modificar o guardar datos en la base de datos:
   - Leer: `print(usuario.nombre)` (accede al campo `nombre`).
   - Modificar: `usuario.edad = 42`
   - Guardar: `usuario.save()` (actualiza o inserta el registro en la base de datos).
   - Eliminar: `usuario.delete()` (elimina el registro de la base de datos).
4. **Relaciones**: Si el modelo tiene relaciones (como `ForeignKey` o `ManyToManyField`), la instancia puede acceder a los objetos relacionados.
   - Ejemplo: Si `Usuario` tiene una relación `ForeignKey` con `Perfil`, puedes acceder con `usuario.perfil`.

```python title="Ejemplo" linenums="1"
from mi_app.models import Usuario

# Crear una instancia de modelo
usuario = Usuario(nombre="Pepe", edad=41)
usuario.save()  # Guardar en la base de datos

# Recuperar una instancia desde la base de datos
usuario_recuperado = Usuario.objects.get(nombre="Pepe")

# Modificar la instancia
usuario_recuperado.edad = 42
usuario_recuperado.save()

# Acceder a los datos
print(usuario_recuperado.nombre)  # Imprime: Pepe
```

### Diferencia con QuerySets

- Un **QuerySet** es una colección de instancias de modelo (o una consulta que puede devolver múltiples instancias).
- Una **instancia de modelo** es un solo objeto que representa un registro específico.

Las **instancias de modelos** son objetos Python que representan filas individuales en la base de datos, creados a partir de las clases de modelo de Django, y permiten manipular los datos de forma intuitiva y orientada a objetos.


## Migraciones

Las **migraciones** son un mecanismo del ORM (Object-Relational Mapping) que permite gestionar los cambios en la estructura de la base de datos de forma automática y controlada. Cuando defines o modificas modelos en Django (por ejemplo, añadiendo campos, creando nuevas tablas o alterando relaciones), las migraciones traducen esos cambios en el código Python a comandos SQL que actualizan el esquema de la base de datos sin perder datos.

Las migraciones son archivos generados por Django que describen las modificaciones necesarias en la base de datos, como crear tablas, añadir columnas, modificar tipos de datos o establecer índices. Estos archivos se generan con el comando `makemigrations` y se aplican con el comando `migrate`.

### Proceso de migraciones

1. **Definir o modificar modelos**: Cambias las clases de modelo en tus archivos `models.py` (por ejemplo, añades un campo `email` a un modelo `Usuario`).
2. **Generar migraciones**: Ejecutas `python manage.py makemigrations`, y Django analiza los cambios en los modelos para crear un archivo de migración (normalmente en la carpeta `migrations/` de la app). Este archivo contiene instrucciones en Python para aplicar o revertir los cambios.
3. **Aplicar migraciones**: Ejecutas `python manage.py migrate`, y Django aplica las migraciones pendientes, ejecutando los comandos SQL necesarios para actualizar la base de datos.
4. **Control de versiones**: Los archivos de migración se versionan (por ejemplo, `0001_initial.py`, `0002_add_email.py`), lo que permite rastrear y revertir cambios.

### Características clave

- **Automatización**: Django detecta automáticamente los cambios en los modelos y genera las migraciones necesarias.
- **Portabilidad**: Las migraciones funcionan con diferentes bases de datos (PostgreSQL, MySQL, SQLite, etc.) sin necesidad de escribir SQL específico.
- **Reversibilidad**: Puedes deshacer migraciones con `python manage.py migrate <app> <migration_name>` para volver a un estado anterior.
- **Dependencias**: Las migraciones pueden depender de otras migraciones, asegurando que los cambios se apliquen en el orden correcto.
- **Datos iniciales**: Puedes incluir migraciones para cargar datos iniciales en la base de datos (usando `RunPython` en los archivos de migración).

Supongamos que tienes un modelo `Usuario`

```python title="Ejemplo" linenums="1"
# mi_app/models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
```


```python title="Si añades un nuevo campo" 
    email = models.EmailField(unique=True)
```

1. Ejecutas:
   ```bash
   python manage.py makemigrations
   ```
   Esto genera un archivo de migración (por ejemplo, `0002_usuario_email.py`) con instrucciones para añadir el campo `email`.
2. Luego aplicas los cambios:
   ```bash
   python manage.py migrate
   ```
   Django crea o modifica la tabla en la base de datos para incluir el campo `email`.

### Comandos útiles

- `python manage.py makemigrations`: Genera archivos de migración basados en cambios en los modelos.
- `python manage.py migrate`: Aplica las migraciones pendientes a la base de datos.
- `python manage.py showmigrations`: Muestra el estado de las migraciones (aplicadas o no).
- `python manage.py sqlmigrate <app> <migration_name>`: Muestra el SQL que generaría una migración específica.

### Beneficios

- Sincroniza los modelos con la base de datos sin intervención manual.
- Facilita la colaboración en equipo al mantener los cambios en el esquema bajo control de versiones.
- Permite evolucionar la base de datos sin perder datos existentes (en la mayoría de los casos).

Las **migraciones** son una herramienta esencial para gestionar y aplicar cambios en el esquema de la base de datos de forma automática, segura y reversible, manteniendo la coherencia entre los modelos de Django y la base de datos subyacente.

