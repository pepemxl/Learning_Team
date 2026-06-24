# Models


El **Model API** de Django es una interfaz que permite interactuar con la base de datos de manera programática utilizando los modelos definidos en una aplicación Django. Los modelos en Django son clases de Python que representan tablas en la base de datos, y el Model API proporciona métodos para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y consultas complejas sobre esos modelos.

## Características principales del Model API

1. **Creación de objetos (Create)**:
   Puedes crear y guardar nuevos registros en la base de datos utilizando el método `create()` o instanciando un objeto del modelo y llamando al método `save()`.

   ```python
   from myapp.models import MiModelo

   # Crear y guardar un nuevo objeto
   nuevo_objeto = MiModelo(campo1='valor1', campo2='valor2')
   nuevo_objeto.save()

   # O usar create()
   MiModelo.objects.create(campo1='valor1', campo2='valor2')
   ```

2. **Lectura de objetos (Read)**:
   El Model API proporciona métodos para consultar la base de datos, como `all()`, `filter()`, `exclude()`, `get()`, entre otros.

   ```python
   # Obtener todos los objetos
   todos = MiModelo.objects.all()

   # Filtrar objetos
   filtrados = MiModelo.objects.filter(campo1='valor1')

   # Obtener un único objeto (lanza una excepción si no existe o hay múltiples)
   unico = MiModelo.objects.get(id=1)
   ```

3. **Actualización de objetos (Update)**:
   Puedes actualizar objetos existentes modificando sus atributos y llamando a `save()`, o usar el método `update()` para actualizar múltiples objetos de una vez.

   ```python
   # Actualizar un objeto
   objeto = MiModelo.objects.get(id=1)
   objeto.campo1 = 'nuevo_valor'
   objeto.save()

   # Actualizar múltiples objetos
   MiModelo.objects.filter(campo1='valor1').update(campo1='nuevo_valor')
   ```

4. **Eliminación de objetos (Delete)**:
   Puedes eliminar objetos individuales o múltiples objetos usando el método `delete()`.

   ```python
   # Eliminar un objeto
   objeto = MiModelo.objects.get(id=1)
   objeto.delete()

   # Eliminar múltiples objetos
   MiModelo.objects.filter(campo1='valor1').delete()
   ```

5. **Consultas complejas**:
   El Model API permite realizar consultas complejas utilizando métodos como `annotate()`, `aggregate()`, `Q objects`, `F expressions`, entre otros.

   ```python
   from django.db.models import Q, F

   # Consulta con condiciones OR
   resultados = MiModelo.objects.filter(Q(campo1='valor1') | Q(campo2='valor2'))

   # Usar F() para comparar campos
   resultados = MiModelo.objects.filter(campo1=F('campo2'))
   ```

6. **Relaciones entre modelos**:
   El Model API también maneja relaciones entre modelos, como `ForeignKey`, `OneToOneField`, y `ManyToManyField`, permitiendo acceder a objetos relacionados de manera sencilla.

   ```python
   # Acceder a objetos relacionados
   objeto = MiModelo.objects.get(id=1)
   relacionados = objeto.related_model_set.all()
   ```

### Ejemplo completo

Supongamos que tienes un modelo `Libro`:

```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicado = models.DateField()
```

Puedes usar el Model API para interactuar con la base de datos:

```python
# Crear un nuevo libro
Libro.objects.create(titulo='Cien años de soledad', autor='Gabriel García Márquez', publicado='1967-05-30')

# Obtener todos los libros
libros = Libro.objects.all()

# Filtrar libros por autor
libros_gabo = Libro.objects.filter(autor='Gabriel García Márquez')

# Actualizar un libro
libro = Libro.objects.get(titulo='Cien años de soledad')
libro.titulo = 'Cien años de soledad (Edición Especial)'
libro.save()

# Eliminar un libro
libro.delete()
```

En resumen, el **Model API** de Django es una herramienta poderosa que abstrae la interacción con la base de datos, permitiéndote trabajar con datos de manera intuitiva y eficiente.