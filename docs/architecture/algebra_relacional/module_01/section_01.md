# **Álgebra Relacional**

Vamos a empezar a diseñar APIs, Base de datos y sistemas los sistemas que los conectan adaptando algunos conceptos matemáticos que nos ayuden a justificar algunas decisiones técnicas. Para ellos repasaremos algunos conceptos algebra moderna, lo cual nos permitirá entender algunos nuevos conceptos en API como lo es el tema de funtores que pertenece a la teoría de categorías.


## **Fundamentos Básicos**

###  ¿Qué es el Álgebra Relacional?

Comprende que es un **lenguaje de consulta procedural**. Tu describes el "cómo" (los pasos) para obtener el resultado, a diferencia de SQL que es más declarativo ("qué" quieres).

### Vocabulario Clave (¡Aprende esto como tu ABC!)

-   **Relación (Relation):** Una tabla con filas y columnas. Ej: `Estudiantes`.
-   **Tupla (Tuple):** Una fila o registro dentro de una relación.
-   **Atributo (Attribute):** Una columna o campo de una relación. Ej: `Nombre`, `Edad`.
-   **Grado (Degree):** El número de atributos de una relación.
-   **Cardinalidad (Cardinality):** El número de tuplas de una relación.
-   **Esquema (Schema):** La estructura de la relación (su nombre y la lista de sus atributos). Ej: `Estudiantes(Nombre, Edad, Carrera)`.

**Recurso Recomendado:** Lee los primeros capítulos de cualquier libro de "Fundamentos de Bases de Datos" (como el de Elmasri & Navathe) o mira videos introductorios en YouTube buscando "Modelo Relacional introducción".


#### **Fase 2: Las Operaciones Fundamentales**

**Objetivo:** Dominar las 6 operaciones primitivas del álgebra relacional. Practica cada una hasta entenderla a la perfección.

Usaremos estas tablas de ejemplo en todos los ejercicios:
**Clientes**
| ID | Nombre | Ciudad |
| :-- | :--- | :--- |
| 1 | Ana | Monterrey |
| 2 | Carlos | Guadalajara |
| 3 | Beatriz | Monterrey |

**Pedidos**
| ID_Pedido | Cliente_ID | Producto | Total |
| :--- | :--- | :--- | :--- |
| 101 | 1 | Laptop | 15000 |
| 102 | 1 | Mouse | 500 |
| 103 | 3 | Teclado | 800 |

1.  **Selección (Sigma - σ)**
    *   **Qué hace:** Filtra **filas** based on a condition.
    *   **Sintaxis:** σ<sub>condición</sub>(Relación)
    *   **Ejemplo:** σ<sub>Ciudad='Monterrey'</sub>(Clientes) → Devuelve los clientes Ana y Beatriz.
    *   **Práctica:** Escribe consultas para: "Clientes que se llaman 'Ana'", "Pedidos con un Total mayor a 1000".

2.  **Proyección (Pi - π)**
    *   **Qué hace:** Selecciona **columnas** específicas, eliminando duplicados.
    *   **Sintaxis:** π<sub>atributo1, atributo2, ...</sub>(Relación)
    *   **Ejemplo:** π<sub>Nombre, Ciudad</sub>(Clientes) → Devuelve una lista de nombres y ciudades.
    *   **Práctica:** "Obtener solo los IDs y Productos de todos los pedidos".

3.  **Unión (Union - ∪)**
    *   **Qué hace:** Combina las tuplas de dos relaciones compatibles (mismo número y tipo de atributos).
    *   **Sintaxis:** Relación1 ∪ Relación2
    *   **Ejemplo:** (σ<sub>Ciudad='Monterrey'</sub>(Clientes)) ∪ (σ<sub>Ciudad='Guadalajara'</sub>(Clientes)) → Todos los clientes de ambas ciudades.
    *   **Práctica:** Crea una pequeña tabla `Empleados` con la misma estructura de `Clientes` y practica la unión.

4.  **Diferencia (Difference - -)**
    *   **Qué hace:** Encuentra las tuplas que están en la primera relación pero no en la segunda.
    *   **Sintaxis:** Relación1 - Relación2
    *   **Ejemplo:** π<sub>ID</sub>(Clientes) - π<sub>Cliente_ID</sub>(Pedidos) → Encuentra los IDs de clientes que **no** han hecho ningún pedido (en este caso, el ID 2, Carlos).

5.  **Producto Cartesiano (Cartesian Product - ×)**
    *   **Qué hace:** Combina cada tupla de la primera relación con cada tupla de la segunda. **¡Cuidado! Genera muchos datos.**
    *   **Sintaxis:** Relación1 × Relación2
    *   **Ejemplo:** Clientes × Pedidos → Combina a Ana con el pedido 101, 102, 103; a Carlos con 101, 102, 103; etc.

6.  **Renombramiento (Rho - ρ)**
    *   **Qué hace:** Cambia el nombre de una relación o de sus atributos. Es crucial para evitar ambigüedades, especially después de un producto cartesiano.
    *   **Sintaxis:** ρ<sub>NuevoNombre(Atributo1, Atributo2...)</sub>(Relación)
    *   **Ejemplo:** ρ<sub>C(ID_C, Nombre_C, Ciudad)</sub>(Clientes)

**Recurso Recomendado:** Usa **DB Fiddle** o un software como **DBeaver** para crear las tablas de ejemplo y escribir las consultas equivalentes en SQL. Esto te ayudará a ver la aplicación práctica.


#### **Fase 3: Operaciones Derivadas y Avanzadas (Semana 4)**

**Objetivo:** Aprender operaciones más complejas que se construyen a partir de las fundamentales.

1.  **Intersección (Intersection - ∩)**
    *   **Qué hace:** Encuentra las tuplas comunes a dos relaciones compatibles.
    *   **Cómo se deriva:** R ∩ S = R - (R - S)
    *   **Ejemplo:** "Encontrar clientes que son también empleados".

2.  **Join (⨝) - ¡La más importante!**
    *   **Qué hace:** Combina tuplas de dos relaciones based on a join condition. Es un **producto cartesiano + una selección**.
    *   **Sintaxis:** Relación1 ⨝<sub>condición</sub> Relación2
    *   **Tipos principales:**
        *   **Theta-Join:** Cualquier condición (>, <, =, etc.). Ej: `Clientes ⨝ Clientes.ID < Pedidos.ID_Pedido Pedidos`
        *   **Equijoin:** La condición es una igualdad. Es el más común.
        *   **Natural Join (⨝):** Un equijoin automático sobre atributos con el mismo nombre. No necesita condición. Ej: `Clientes ⨝ Pedidos` (asumiendo que `ID` y `Cliente_ID` se renombran para que coincidan).

3.  **División (Division - /)**
    *   **Qué hace:** Responde preguntas de "para todo" o "para todos". Es la operación más compleja.
    *   **Ejemplo clásico:** "Encontrar los clientes que han comprado **todos** los productos".
    *   **Cómo se explica:** Dadas R(A, B) y S(B), el resultado de R / S es todos los valores de A que están asociados con **todos** los valores de B en S.

**Recurso Recomendado:** Busca ejercicios resueltos de "división álgebra relacional" para entender bien este último concepto. Es un tema clásico de exámenes.

#### **Fase 4: Integración y Práctica (Semana 5 en adelante)**

**Objetivo:** Unir todas las operaciones para resolver problemas del mundo real.

1.  **Aprende a "Leer" y "Escribir" consultas:**
    *   **De Álgebra a Español:** Dada una expresión, escribe en palabras qué está preguntando.
        *   Ej: π<sub>Nombre</sub>( σ<sub>Total>1000</sub>(Clientes ⨝ Pedidos) ) → "Nombres de clientes que han hecho un pedido por más de 1000 pesos".
    *   **De Español a Álgebra:** Dada una pregunta, construye la expresión paso a paso.
        *   Ej: "Productos comprados por clientes de Monterrey".
        *   Pasos:
            1.  Unir Clientesy Pedidos: `ClientesPedidos ← Clientes ⨝ Clientes.ID = Pedidos.Cliente_ID Pedidos`
            2.  Filtrar por ciudad: `MonterreyPedidos ← σ Ciudad='Monterrey' (ClientesPedidos)`
            3.  Project el nombre del producto: `Resultado ← π Producto (MonterreyPedidos)`

2.  **Herramientas de Práctica:**
    *   **Lápiz y Papel:** Dibuja las tablas y sigue las operaciones mentalmente. Es la mejor manera de internalizar los conceptos.
    *   **Software:** Usa un diagrama E-R para visualizar las relaciones entre tablas antes de escribir el álgebra.
    *   **Traductor a SQL:** Practica escribiendo la consulta SQL equivalente a tu expresión de álgebra relacional. Te confirmará si tu lógica es correcta.

3.  **Ejercicios de Práctica Integradores:**
    *   "Encuentra los nombres de los clientes que no han realizado ningún pedido."
    *   "Obtén los IDs de pedidos para pedidos que incluyen un producto comprado por alguien de Guadalajara." (¡Cuidado con los joins y subconsultas!).
    *   "Lista todas las posibles combinaciones de clientes y productos." (Producto Cartesiano).

**Recurso Recomendado:** Los ejercicios de libros clásicos y los exámenes de cursos universitarios (que suelen estar disponibles online) son el mejor recurso para esta fase.

El Álgebra Relacional es la base fundamental que te permitirá:
*   **Entender cómo se ejecuta una consulta SQL** en su nivel más bajo.
*   **Escribir consultas SQL más eficientes y correctas.**
*   **Aprender otros temas avanzados** como la normalización y la optimización de consultas.
