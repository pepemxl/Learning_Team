# Patrones Creacionales

## Factory Method

Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán.

Siempre buscamos responder:

- ¿De qué clases se compone?
- ¿Qué papeles juegan esas clases?
- ¿De qué forma se relacionan los elementos del patrón?


### Ventajas

- Podemos agregar fácilmente nuevos tipos de productos sin alterar el código del cliente existente.
- En general, se evita un acoplamiento estrecho entre los productos y las clases y objetos creadores.

### Desventajas

- Para crear un objeto de producto concreto en particular, es posible que el cliente tenga que subclasificar la clase creadora.
- Terminas con una gran cantidad de archivos pequeños, es decir, abarrotando los archivos.



Puedes declarar el patrón Factory Method como abstracto para forzar a todas las subclases a implementar sus propias versiones del método. Como alternativa, el método fábrica base puede devolver algún tipo por defecto.

El patrón Factory Method ayuda a desacoplar esta lógica de las clases concretas.

```python title="Ejemplo código normal" linenums="1"
class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_presentation(self):
        return f"{self.get_name()} es una Persona"

class Student(Person):
    student_id: int
    group_id: int

    def get_presentation(self):
        return f"{self.get_name()} es un estudiante"

class Teacher(Person):
    teacher_id: int
    subject_id: int

    def get_presentation(self):
        return f"{self.get_name()} es un profesor"

def main():
    persona1 = Person("Pepe", 41)
    student1 = Student("Jose", 7)
    teacher1 = Teacher("Luis", 35)
    print(f"{persona1.get_name()} tiene {persona1.get_age()} años")
    print(f"{student1.get_name()} tiene {student1.get_age()} años")
    print(f"{teacher1.get_name()} tiene {teacher1.get_age()} años")
    print(persona1.get_presentation())
    print(student1.get_presentation())
    print(teacher1.get_presentation())

if __name__ == '__main__':
    main()
```

Todos las clases que heredan pueden accesar a los metodos de la clase padre.

```bash title="Salida"
Pepe tiene 41 años
Jose tiene 7 años
Luis tiene 35 años
Pepe es una Persona
Jose es un estudiante
Luis es un profesor
```


```python title="Ejemplo código con factory" linenums="1"
class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_presentation(self):
        return f"{self.get_name()} es una Persona"

class Student(Person):
    student_id: int
    group_id: int

    def get_presentation(self):
        return f"{self.get_name()} es un estudiante"

class Teacher(Person):
    teacher_id: int
    subject_id: int

    def get_presentation(self):
        return f"{self.get_name()} es un profesor"


def Factory(person_type: str = "Persona"):
    """factory method"""
    tipos_de_persona = {
        "Persona": Person,
        "Estudiante": Student,
        "Profesor": Teacher
    }
    return tipos_de_persona[person_type]

def main():
    persona1 = Factory("Persona")("Pepe", 41)
    student1 = Factory("Estudiante")("Jose", 7)
    teacher1 = Factory("Profesor")("Luis", 35)
    print(f"{persona1.get_name()} tiene {persona1.get_age()} años")
    print(f"{student1.get_name()} tiene {student1.get_age()} años")
    print(f"{teacher1.get_name()} tiene {teacher1.get_age()} años")
    print(persona1.get_presentation())
    print(student1.get_presentation())
    print(teacher1.get_presentation())

if __name__ == '__main__':
    main()
```

```bash title="Salida"
Pepe tiene 41 años
Jose tiene 7 años
Luis tiene 35 años
Pepe es una Persona
Jose es un estudiante
Luis es un profesor
```

El patrón Factory Method define un método que debe utilizarse para crear objetos, en lugar de una llamada directa al constructor (usualmente operador new). Las subclases pueden sobrescribir este método para cambiar las clases de los objetos que se crearán.



## Asbtract Factory


## Builder


## Prototype


## Singleton



