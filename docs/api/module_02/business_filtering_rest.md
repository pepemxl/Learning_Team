# Filtros de Dominio (también conocidos como filtros de negocio)


Los filtros que se aplican a los modelos después de la materialización de los parámetros, y que dependen sustancialmente del tipo del modelo, suelen conocerse como **filtros de dominio** o **filtros de negocio**. 

Estos filtros están relacionados con la lógica específica del dominio del modelo y se aplican una vez que los datos han sido validados y materializados (por ejemplo, convertidos en objetos o entidades del modelo).

## Características de estos filtros

- **Dependencia del modelo**: Están diseñados para operar sobre las propiedades o atributos específicos del modelo, por ejemplo: 
    - filtrar usuarios por roles,
    - productos por categoría,
    - etc.
- **Post-materialización**: Se aplican después de que los parámetros de la solicitud han sido validados y convertidos en instancias del modelo.
- **Lógica de negocio**: Incorporan reglas específicas del dominio, como: 
    - restricciones de acceso, 
    - condiciones de visibilidad o 
    - transformaciones basadas en el contexto del modelo.
- **Ejemplo**: En una API de comercio electrónico, un filtro de dominio podría limitar los productos devueltos según la región del usuario o el estado de inventario, después de que los parámetros de la solicitud (como categoría o precio) ya han sido procesados.

En algunos frameworks o contextos, también se les puede llamar **filtros de modelo** o **filtros contextuales**, dependiendo de la terminología adoptada. Por ejemplo, en Django (Python) se asemejan a los filtros aplicados en los `QuerySets` después de la validación inicial, mientras que en otros entornos podrían estar embebidos en la lógica de los handlers o servicios de negocio.


