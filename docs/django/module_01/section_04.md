# Modelos matemáticos subyacentes


El patrón de diseño **Active Record**, descrito por Martin Fowler, **no está basado directamente en un modelo matemático** en el sentido de una teoría formal o un constructo matemático riguroso, como podría ser un modelo basado en álgebra relacional o teoría de conjuntos. En cambio, es un **patrón de diseño de software** que surge de necesidades prácticas en el desarrollo de aplicaciones, específicamente para mapear objetos de un programa a tablas en una base de datos relacional.

## Contexto y fundamentos del patrón Active Record

El patrón Active Record se enfoca en simplificar la interacción entre objetos en el código (programación orientada a objetos) y registros en una base de datos relacional. Cada instancia de un objeto representa una fila en una tabla, y la clase del objeto define la estructura de la tabla (campos, relaciones, etc.). Aunque no está basado en un modelo matemático explícito, tiene conexiones con conceptos de bases de datos relacionales, que sí tienen fundamentos matemáticos.

#### Relación con conceptos matemáticos

1. **Álgebra relacional**:
   - Las bases de datos relacionales, en las que se basa Active Record, tienen su fundamento en el **álgebra relacional**, un modelo matemático desarrollado por Edgar F. Codd. Este modelo utiliza conceptos como **tuplas** (filas), **relaciones** (tablas) y operaciones como **selección**, **proyección** y **unión** (joins).
   - En Active Record, las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y las consultas a través del ORM (como `filter()` o `get()` en Django) se traducen internamente a operaciones de álgebra relacional. Por ejemplo, un método como `Usuario.objects.filter(edad__gt=18)` se corresponde con una operación de selección (`σ`) en álgebra relacional.
   - Aunque los desarrolladores no interactúan directamente con el álgebra relacional, el ORM de frameworks como Django abstrae estas operaciones, y Active Record aprovecha esta base matemática implícitamente.

2. **Mapeo objeto-relacional**:
   - Active Record establece un mapeo directo entre objetos (en programación orientada a objetos) y registros en una base de datos relacional. Este mapeo puede considerarse una relación funcional entre dos dominios: el dominio de los objetos en el código y el dominio de las tuplas en la base de datos.
   - Matemáticamente, esto puede interpretarse como una función biyectiva (o casi biyectiva) entre las instancias de un modelo y las filas de una tabla, donde cada objeto tiene un identificador único (como una clave primaria) que asegura correspondencia uno a uno.

3. **Encapsulación y cohesión**:
   - Aunque no es un concepto matemático, la idea de encapsulación en Active Record (donde un modelo contiene tanto datos como comportamiento) se alinea con principios de diseño que buscan minimizar la complejidad y maximizar la modularidad. Esto no es un modelo matemático, pero podría relacionarse con conceptos de teoría de sistemas o modularidad en matemáticas aplicadas al diseño de software.

### ¿Por qué no es un modelo matemático directo?

- **Origen práctico**: Active Record es un patrón pragmático, diseñado para resolver problemas de ingeniería de software, como la necesidad de simplificar el acceso a bases de datos sin escribir consultas SQL manualmente. No se deriva de un formalismo matemático, sino de la experiencia práctica en desarrollo.
- **Abstracción del ORM**: El patrón depende del ORM, que actúa como una capa de abstracción sobre el álgebra relacional de las bases de datos. Los desarrolladores no necesitan entender los fundamentos matemáticos del álgebra relacional para usar Active Record, ya que el framework maneja esas complejidades.
- **Flexibilidad sobre formalismo**: Active Record prioriza la usabilidad y la simplicidad sobre un rigor matemático estricto. Por ejemplo, permite ciertas prácticas (como consultas no optimizadas) que podrían no alinearse con un modelo matemático puro.

### Conexión con otros patrones y matemáticas

Otros patrones de diseño, como **Data Mapper** (también descrito por Fowler), podrían considerarse más "formales" en su separación de responsabilidades, pero incluso estos no están basados en un modelo matemático explícito. Sin embargo, la teoría de bases de datos relacionales, que subyace a Active Record, tiene raíces profundas en matemáticas, particularmente en:
- **Teoría de conjuntos**: Las tablas se modelan como conjuntos de tuplas.
- **Lógica de predicados**: Las consultas SQL se pueden expresar como expresiones lógicas.
- **Funciones y relaciones**: Las claves primarias y foráneas establecen relaciones funcionales entre tablas.

