# Clase Abstracta

En Python, `abc.ABC` es una clase base que se utiliza para definir clases abstractas. El módulo `abc` (que significa "Abstract Base Classes") proporciona herramientas para crear clases abstractas, que son clases que no pueden ser instanciadas directamente y están diseñadas para ser subclasificadas.

### ¿Qué es una clase abstracta?

Una clase abstracta es una clase que puede definir métodos abstractos, que son métodos que no tienen una implementación en la clase abstracta, pero que deben ser implementados por cualquier subclase concreta que herede de ella. Esto es útil para definir una interfaz común que todas las subclases deben seguir.

### Uso de `abc.ABC`

La clase `ABC` es una clase base que puedes heredar para crear tus propias clases abstractas. Aquí tienes un ejemplo básico de cómo usarla:

```python
from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):

    @abstractmethod
    def metodo_abstracto(self):
        pass

    def metodo_concreto(self):
        print("Este es un método concreto.")

class MiClaseConcreta(MiClaseAbstracta):

    def metodo_abstracto(self):
        print("Implementación del método abstracto.")

# Intentar instanciar la clase abstracta directamente generará un error
# obj = MiClaseAbstracta()  # Esto lanzará un TypeError

# Instanciar la clase concreta es válido
obj = MiClaseConcreta()
obj.metodo_abstracto()  # Output: Implementación del método abstracto.
obj.metodo_concreto()   # Output: Este es un método concreto.
```

1. **`ABC`**: Es la clase base que se utiliza para definir una clase abstracta.
2. **`@abstractmethod`**: Es un decorador que se utiliza para marcar un método como abstracto. Las subclases deben implementar este método.
3. **Métodos concretos**: Una clase abstracta también puede tener métodos concretos (con implementación), que pueden ser heredados y utilizados por las subclases.


