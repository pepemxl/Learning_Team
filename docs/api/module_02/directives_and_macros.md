# Directivas y Macros


En el contexto de GraphQL, las **directivas** y las **macros** son conceptos distintos, pero ambos se utilizan para extender o personalizar el comportamiento de los esquemas y consultas en GraphQL. A continuación, te explico qué son, cómo se relacionan y sus diferencias, con un enfoque claro y conciso:

## **1. Directivas en GraphQL**
- **Definición**: Las directivas son instrucciones especiales en el lenguaje de GraphQL que modifican el comportamiento de un campo, tipo o consulta en un esquema. Se denotan con el símbolo `@` y se aplican en tiempo de ejecución o durante la validación del esquema.
- **Uso principal**: Personalizar la lógica de resolución de campos, controlar el acceso, o añadir metadatos.
- **Ejemplos comunes**:
  - `@include`: Incluye un campo solo si una condición es verdadera.
  - `@skip`: Omite un campo si una condición es verdadera.
  - `@deprecated`: Marca un campo o tipo como obsoleto.
  - Directivas personalizadas: Puedes crear directivas propias (por ejemplo, `@auth` para manejar autenticación).
- **Ejemplo**:
  ```graphql
  type Query {
    user(id: ID!): User @auth(role: "admin")
  }
  ```
  Aquí, `@auth` podría ser una directiva personalizada que verifica si el usuario tiene el rol de administrador antes de resolver el campo `user`.

- **Características**:
  - Son parte del estándar de GraphQL (definidas en la especificación oficial).
  - Se aplican en el esquema (SDL - Schema Definition Language) o en las consultas.
  - Se procesan en el servidor, generalmente en el código de los resolvers o en middleware.

## **2. Macros en GraphQL**
- **Definición**: Las macros no son un concepto estándar de GraphQL, sino una herramienta o abstracción que algunos frameworks o bibliotecas (como Apollo o herramientas de generación de código) implementan para simplificar la creación o manipulación de esquemas y consultas. En este contexto, una "macro" suele ser una función o plantilla que genera fragmentos de código GraphQL o automatiza tareas repetitivas.
- **Uso principal**: Generar consultas, fragmentos o esquemas de forma programática, reduciendo la escritura manual de código.
- **Ejemplo**: En un entorno como Apollo Client, una macro podría ser una función que genera consultas GraphQL dinámicamente:
  ```javascript
  // Ejemplo ficticio de una macro en JavaScript
  const createQuery = (fieldName) => gql`
    query Get${fieldName}($id: ID!) {
      ${fieldName}(id: $id) {
        id
        name
      }
    }
  `;
  ```
  Esta "macro" genera una consulta GraphQL para cualquier campo dado (`fieldName`).

- **Características**:
  - No son parte del estándar de GraphQL; dependen de herramientas específicas.
  - Se ejecutan en tiempo de desarrollo o compilación, no en tiempo de ejecución.
  - Son comunes en entornos que usan GraphQL con lenguajes como JavaScript, TypeScript o Python.

## **3. Relación entre directivas y macros**
Aunque directivas y macros tienen propósitos distintos, su relación radica en que ambas buscan **extender o simplificar** el uso de GraphQL. Aquí algunos puntos clave sobre cómo se relacionan:

- **Complementariedad**:
  - Las **directivas** se centran en modificar el comportamiento del esquema o las consultas en el servidor o cliente en tiempo de ejecución. Por ejemplo, una directiva `@cacheControl` puede controlar cómo se cachean los resultados.
  - Las **macros** suelen usarse en el lado del desarrollo para generar o manipular código GraphQL (como consultas o esquemas) antes de que se ejecute. Por ejemplo, una macro podría generar un esquema que incluye directivas automáticamente.

- **Uso conjunto**:
  - Puedes usar macros para generar consultas o fragmentos que incluyan directivas. Por ejemplo, una macro podría generar una consulta con `@include` basado en ciertas condiciones:
    ```javascript
    const queryWithDirective = (condition) => gql`
      query GetUser($id: ID!, $withDetails: Boolean!) {
        user(id: $id) {
          id
          name
          details @include(if: $withDetails) {
            email
          }
        }
      }
    `;
    ```
    Aquí, una macro genera una consulta que usa la directiva `@include`.

- **Diferencias en el ámbito**:
  - **Directivas**: Operan dentro del ecosistema GraphQL y son procesadas por el servidor o cliente GraphQL.
  - **Macros**: Operan fuera del núcleo de GraphQL, en herramientas de desarrollo (como preprocesadores, generadores de código, o CLI).

- **Ejemplo práctico de interacción**:
  Supongamos que estás usando Apollo Server y defines una directiva personalizada `@uppercase` para convertir el resultado de un campo a mayúsculas. Podrías usar una macro en tu entorno de desarrollo para generar automáticamente consultas que apliquen esta directiva a ciertos campos:
  ```graphql
  # Esquema con directiva personalizada
  directive @uppercase on FIELD
  type Query {
    greeting: String @uppercase
  }
  ```
  ```javascript
  // Macro para generar consultas
  const createQueryWithUppercase = (field) => gql`
    query Get${field} {
      ${field} @uppercase
    }
  `;
  ```

## **4. Diferencias clave**
| **Aspecto**         | **Directivas**                              | **Macros**                                  |
|---------------------|---------------------------------------------|---------------------------------------------|
| **Estándar**        | Parte de la especificación de GraphQL       | No estándar, depende de herramientas        |
| **Uso**             | Modifica comportamiento en tiempo de ejecución | Genera código en tiempo de desarrollo       |
| **Ejemplo**         | `@include`, `@skip`, `@deprecated`          | Funciones que generan consultas/esquemas    |
| **Procesamiento**   | Servidor o cliente GraphQL                 | Herramientas de desarrollo (Apollo, CLI)    |
| **Ejemplo práctico**| `@auth` para restringir acceso             | Generar consultas dinámicas con `gql`       |

## **5. Recursos para profundizar**
- **Directivas**:
  - Documentación oficial: [https://graphql.org/learn/directives/](https://graphql.org/learn/directives/)
  - Tutorial de Apollo sobre directivas personalizadas: [https://www.apollographql.com/docs/apollo-server/schema/directives/](https://www.apollographql.com/docs/apollo-server/schema/directives/)
- **Macros**:
  - Apollo Client y `gql` tag: [https://www.apollographql.com/docs/react/data/queries/](https://www.apollographql.com/docs/react/data/queries/)
  - GraphQL Code Generator (para macros automatizadas): [https://the-guild.dev/graphql/codegen](https://the-guild.dev/graphql/codegen)


Las **directivas** son un mecanismo estándar de GraphQL para modificar el comportamiento de los esquemas y consultas en tiempo de ejecución, mientras que las **macros** son herramientas no estándar que simplifican la generación de código GraphQL en tiempo de desarrollo. Se relacionan porque ambas permiten personalizar y optimizar el trabajo con GraphQL, y puedes usar macros para generar consultas o esquemas que incluyan directivas.

