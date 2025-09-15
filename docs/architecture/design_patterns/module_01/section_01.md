# Patrones de diseño en la industria

El libro **Patterns of Enterprise Application Architecture** de Martin Fowler, publicado en 2002, es una referencia clave en el diseño de software empresarial. En él, Fowler describe un conjunto de patrones de diseño que abordan problemas comunes en la construcción de aplicaciones empresariales, especialmente aquellas que involucran bases de datos, lógica de negocio y arquitectura distribuida. 

## Principales patrones por categorías

### **1. Patrones de Organización de la Lógica de Dominio**
Estos patrones describen cómo estructurar la lógica de negocio en una aplicación.

- **Transaction Script (Script de Transacción)**: Organiza la lógica de negocio en procedimientos que manejan una solicitud específica. Cada script encapsula una transacción completa, ideal para aplicaciones simples.
  - Ejemplo: Un procedimiento que procesa un pedido en un sistema de comercio electrónico.
- **Domain Model (Modelo de Dominio)**: Representa la lógica de negocio como un modelo orientado a objetos, donde los objetos encapsulan datos y comportamiento. Más complejo pero flexible para dominios ricos.
  - Ejemplo: Clases como `Cliente` o `Pedido` con métodos para calcular descuentos o validar estados.
- **Table Module (Módulo de Tabla)**: Organiza la lógica de negocio en torno a una tabla de la base de datos, con una clase que maneja todas las operaciones de una tabla específica.
  - Ejemplo: Una clase `ClienteModule` que maneja todas las operaciones CRUD para la tabla de clientes.
- **Service Layer (Capa de Servicio)**: Define una capa que encapsula la lógica de negocio y coordina operaciones entre el modelo de dominio y otros componentes.
  - Ejemplo: Un servicio `OrderService` que coordina la creación de un pedido y la actualización del inventario.

### **2. Patrones de Mapeo de Datos (Object-Relational Mapping)**
Estos patrones abordan cómo conectar objetos en el código con una base de datos relacional.

- **Active Record (Registro Activo)**: Un objeto representa una fila en una tabla de la base de datos, encapsulando datos y comportamiento, con métodos para operaciones CRUD.
  - Ejemplo: En Django, un modelo como `Usuario` con métodos como `save()` o `delete()`.
- **Data Mapper (Mapeador de Datos)**: Separa la lógica del dominio de la base de datos mediante una capa que mapea objetos a tablas, manteniendo los objetos libres de lógica de persistencia.
  - Ejemplo: Un mapeador que traduce un objeto `Cliente` a la tabla `clientes` sin que el objeto sepa cómo se persiste.
- **Unit of Work (Unidad de Trabajo)**: Rastrea los cambios en los objetos durante una transacción y coordina su persistencia en la base de datos.
  - Ejemplo: Un objeto que registra cambios en múltiples instancias y los guarda en una sola transacción.
- **Repository (Repositorio)**: Actúa como una colección en memoria para objetos de dominio, proporcionando métodos para acceder y persistir objetos sin exponer detalles de la base de datos.
  - Ejemplo: Un `ClienteRepository` con métodos como `findById()` o `save()`.
- **Identity Map (Mapa de Identidad)**: Asegura que cada objeto se cargue solo una vez, manteniendo una referencia única por ID para evitar duplicados.
  - Ejemplo: Un caché que asegura que el mismo `Cliente` con `id=1` no se cargue dos veces.

### **3. Patrones de Acceso a Datos**
Estos patrones describen cómo interactuar con la base de datos.

- **Table Data Gateway (Puerta de Enlace de Tabla)**: Un objeto que actúa como intermediario para todas las operaciones SQL de una tabla específica.
  - Ejemplo: Una clase `ClienteGateway` con métodos como `insert()` o `find()`.
- **Row Data Gateway (Puerta de Enlace de Fila)**: Un objeto que representa una fila específica en una tabla, con métodos para acceder a sus datos.
  - Ejemplo: Un objeto `ClienteRow` que contiene los datos de una fila de la tabla `clientes`.
- **Query Object (Objeto de Consulta)**: Representa una consulta a la base de datos como un objeto, permitiendo construir consultas de manera programática.
  - Ejemplo: Un objeto que encapsula una consulta SQL como `SELECT * FROM clientes WHERE edad > 18`.

### **4. Patrones de Comportamiento de Objetos**
Estos patrones abordan cómo los objetos interactúan y manejan relaciones.

- **Foreign Key Mapping (Mapeo de Clave Foránea)**: Mapea relaciones entre objetos utilizando claves foráneas en la base de datos.
  - Ejemplo: Un objeto `Pedido` con un atributo que referencia el `id` de un `Cliente`.
- **Association Table Mapping (Mapeo de Tabla de Asociación)**: Mapea relaciones muchos-a-muchos usando una tabla intermedia.
  - Ejemplo: Una tabla `pedido_productos` que conecta `Pedidos` y `Productos`.
- **Dependent Mapping (Mapeo Dependiente)**: Mapea objetos que dependen completamente de otro objeto, como componentes de un objeto principal.
  - Ejemplo: Líneas de un pedido que solo existen como parte del `Pedido`.
- **Embedded Value (Valor Embebido)**: Mapea un objeto pequeño como parte de otro objeto en la misma tabla.
  - Ejemplo: Una dirección (calle, ciudad) embebida como columnas en la tabla de `Cliente`.
- **Inheritance Mappers (Mapeadores de Herencia)**: Patrones para mapear jerarquías de herencia de objetos a bases de datos:
  - **Single Table Inheritance (Herencia en Tabla Única)**: Una tabla contiene todas las clases de una jerarquía, con columnas para todos los atributos.
  - **Class Table Inheritance (Herencia en Tabla por Clase)**: Cada clase en la jerarquía tiene su propia tabla.
  - **Concrete Table Inheritance (Herencia en Tabla Concreta)**: Cada clase concreta tiene su propia tabla con todos los atributos.

### **5. Patrones de Arquitectura de Presentación**
Estos patrones se centran en la capa de presentación o interfaz de usuario.

- **Model-View-Controller (MVC)**: Separa la lógica de presentación (vista), la lógica de negocio (modelo) y la coordinación entre ambas (controlador).
  - Ejemplo: En Django, los modelos son el "modelo", las plantillas son la "vista" y las vistas son el "controlador".
- **Page Controller (Controlador de Página)**: Un controlador maneja todas las solicitudes de una página específica.
  - Ejemplo: Una vista en Django que maneja una URL específica.
- **Front Controller (Controlador Frontal)**: Un único controlador central maneja todas las solicitudes, dirigiendo a los manejadores apropiados.
  - Ejemplo: Un sistema de enrutamiento centralizado que procesa todas las solicitudes HTTP.

### **6. Patrones de Distribución**
Estos patrones abordan sistemas distribuidos y comunicación entre componentes.

- **Remote Facade (Fachada Remota)**: Proporciona una interfaz simplificada para acceder a un sistema remoto, escondiendo la complejidad de la comunicación.
  - Ejemplo: Una API REST que expone métodos simples para interactuar con un sistema complejo.
- **Data Transfer Object (DTO, Objeto de Transferencia de Datos)**: Un objeto que transporta datos entre procesos o sistemas, minimizando las llamadas remotas.
  - Ejemplo: Un objeto JSON que contiene los datos de un `Cliente` enviados a través de una API.

### **7. Patrones de Optimización y Sesión**
Estos patrones mejoran el rendimiento y la gestión de estado.

- **Lazy Load (Carga Perezosa)**: Retrasa la carga de datos relacionados hasta que se necesitan.
  - Ejemplo: Cargar los pedidos de un cliente solo cuando se accede a ellos.
- **Session State (Estado de Sesión)**: Gestiona el estado de un usuario entre múltiples solicitudes.
  - Ejemplo: Almacenar el carrito de compras en una sesión HTTP.
- **Optimistic Locking (Bloqueo Optimista)**: Permite actualizaciones concurrentes asumiendo que los conflictos son raros, verificando colisiones antes de guardar.
- **Pessimistic Locking (Bloqueo Pesimista)**: Bloquea recursos para evitar conflictos durante las transacciones.

### **8. Otros Patrones**
- **Gateway (Puerta de Enlace)**: Un objeto que encapsula el acceso a un sistema externo, como una base de datos o un servicio web.
- **Mapper (Mapeador)**: Generaliza la idea de mapear datos entre objetos y la base de datos, base para patrones como Data Mapper.
- **Metadata Mapping (Mapeo de Metadatos)**: Usa metadatos (como configuraciones o esquemas) para definir cómo mapear objetos a la base de datos.
- **Separated Interface (Interfaz Separada)**: Define interfaces separadas para componentes que necesitan ser independientes de su implementación.


### **Contexto y relevancia**
- **Active Record en Django**: Como se mencionó en tus preguntas anteriores, el patrón **Active Record** es uno de los más utilizados en frameworks como Django, donde los modelos encapsulan datos, comportamiento y operaciones de base de datos.
- **Aplicación práctica**: Los patrones de Fowler son soluciones probadas para problemas recurrentes en aplicaciones empresariales. Por ejemplo, Django usa **Active Record** para sus modelos, **MVC** para su arquitectura MTV (Model-Template-View), y conceptos como **Lazy Load** en consultas ORM con `select_related()` o `prefetch_related()`.
- **Flexibilidad**: No todos los patrones son aplicables a todos los proyectos. La elección depende de la complejidad del dominio, los requisitos de rendimiento y la arquitectura del sistema.


El libro de Martin Fowler presenta una colección de patrones organizados en categorías como lógica de dominio, mapeo de datos, acceso a datos, presentación, distribución y optimización. Cada patrón aborda un problema específico en el diseño de aplicaciones empresariales, ofreciendo soluciones reutilizables y bien estructuradas. En el contexto de Django, patrones como **Active Record**, **MVC** y **Repository** son particularmente relevantes, mientras que otros, como **Data Mapper**, pueden usarse en proyectos que requieren mayor separación entre lógica de negocio y persistencia.

