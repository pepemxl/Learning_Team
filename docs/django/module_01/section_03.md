# Active Record


Los modelos deberían encapsular todos los aspectos de un objeto, siguiendo el patrón de diseño ActiveRecord de Martin Fowler, esto es, Active Record es un principio de diseño en el desarrollo de software, particularmente en el contexto del **ORM** (Object-Relational Mapping) de frameworks como Django, y está basada en el patrón **Active Record** descrito por Martin Fowler en su libro **Patterns of Enterprise Application Architecture**.


1. **"Los modelos deberían encapsular todos los aspectos de un objeto"**:
   - En Django, un **modelo** es una clase que representa una entidad (como un usuario, un producto, etc.) y define su estructura (campos) y comportamiento. "Encapsular todos los aspectos" significa que el modelo debe contener no solo los datos (atributos como `nombre`, `edad`, etc.), sino también la lógica relacionada con ese objeto, como métodos para manipularlo o realizar operaciones específicas.
   - Por ejemplo, un modelo `Usuario` no solo debería almacenar `nombre` y `edad`, sino también métodos como `calcular_edad_en_dias()` o `es_mayor_de_edad()` si son relevantes para el objeto.
   - La idea es que el modelo sea una representación completa y autónoma del objeto, agrupando datos y comportamiento en un solo lugar, siguiendo el principio de **encapsulación** de la programación orientada a objetos.

2. **"Siguiendo el patrón de diseño ActiveRecord de Martin Fowler"**:
   - El **patrón Active Record** es un diseño descrito por Martin Fowler que propone una forma de conectar objetos en el código con registros en una base de datos. En este patrón:
        - Cada instancia de un modelo representa una fila en una tabla de la base de datos.
        - La clase del modelo define la estructura de la tabla (campos, tipos de datos, relaciones) y contiene métodos para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) directamente.
        - El modelo "sabe" cómo guardarse, actualizarse o eliminarse en la base de datos, lo que simplifica las interacciones entre el código y la base de datos.
   - En Django, el ORM sigue este patrón: los modelos heredan de `django.db.models.Model`, lo que les da capacidades para interactuar con la base de datos (por ejemplo, `save()`, `delete()`, o consultas con `objects.filter()`).
   - Ejemplo: Si tienes un modelo `Usuario`, puedes crear una instancia (`usuario = Usuario(nombre="Pepe")`), guardarla (`usuario.save()`), o buscarla (`Usuario.objects.get(id=1)`), todo desde el propio modelo, sin escribir SQL manualmente.



```python title="Ejemplo" linenums="1"
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
```

- **Encapsulación**: El modelo `Usuario` no solo almacena `nombre` y `edad`, sino que también incluye métodos como `es_mayor_de_edad()` y `presentarse()`, que encapsulan el comportamiento del objeto.
- **Active Record**: Puedes interactuar con la base de datos directamente desde la instancia (`usuario.save()`, `usuario.delete()`) o la clase (`Usuario.objects.filter()`), siguiendo el patrón Active Record.

