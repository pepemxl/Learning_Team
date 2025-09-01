# Filtros de Dominio en GraphQL

En las implementaciones de GraphQL, los filtros que se aplican a los modelos después de la materialización de los parámetros y que dependen del tipo del modelo suelen conocerse como **filtros de resolución** o **filtros de datos** (data filters). En GraphQL se les llama **filtros en resolvers** o simplemente **lógica de filtrado en resolvers**, ya que estos filtros suelen implementarse dentro de los **resolvers**.


- **Resolvers**: En GraphQL, los resolvers son responsables de obtener y procesar los datos para cada campo de una consulta. Los filtros que dependen del tipo de modelo se aplican típicamente dentro de estos resolvers, después de que los argumentos de la consulta han sido validados y procesados.
- **Ubicación**: Estos filtros se implementan después de la validación inicial de los argumentos (por ejemplo, usando el esquema de GraphQL para validar tipos y estructuras) y después de la materialización de los datos en objetos o entidades del modelo.
- **Dependencia del modelo**: Los filtros están diseñados para operar sobre las propiedades específicas del tipo de dato definido en el esquema GraphQL (por ejemplo, un tipo `User` o `Product`) y suelen incorporar lógica de negocio o restricciones de dominio.

## Términos específicos

- **Filtros en resolvers**: En la práctica, no hay un término estandarizado universal en GraphQL para estos filtros, pero se les suele referir como parte de la lógica de los resolvers. Por ejemplo, en implementaciones como Apollo Server o GraphQL Yoga, podrías verlos como condiciones aplicadas dentro de la función resolver para un campo.
- **Filtros de dominio**: En contextos más orientados al negocio, se les puede llamar filtros de dominio, similar a las APIs REST, ya que reflejan reglas específicas del modelo o del contexto de la aplicación.


```graphql title="Ejemplo"
query {
    products(category: "electronics", inStock: true) {
        id
        name
    }
}
```

Los argumentos `category` y `inStock` se validan primero (en la capa de esquema). Luego, en el resolver del campo `products`, se aplican filtros adicionales basados en el modelo (por ejemplo, verificar si el producto está disponible en la región del usuario o si cumple con otras reglas de negocio). Esta lógica de filtrado dentro del resolver es lo que corresponde a los "filtros de modelo".

## Ejemplo en Apollo Server

```javascript
const resolvers = {
  Query: {
    products: async (parent, { category, inStock }, context) => {
      // Validación inicial de argumentos ya hecha por el esquema
      let query = ProductModel.find({ category });

      // Filtros de dominio/modelo aplicados después de materialización
      if (inStock) {
        query = query.where({ stock: { $gt: 0 } });
      }
      if (context.user.region) {
        query = query.where({ availableIn: context.user.region });
      }

      return await query.exec();
    },
  },
};
```

En este caso, los filtros como `stock: { $gt: 0 }` o `availableIn: context.user.region` serían los equivalentes a los filtros de modelo que se aplican tras la materialización.




