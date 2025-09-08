# Ejemplos en GraphQL

En GraphQL, los conceptos de **Resource Modeling**, **Domain Filtering** y **Business Filtering** se interpretan de manera fundamentalmente diferente a REST, aunque persiguen los mismos objetivos fundamentales.

## Cambio de Paradigma: De Recursos a Grafos

GraphQL cambia el modelo mental de "recursos" a un **grafo de tipos y relaciones**. Aquí te explico cómo se traducen los conceptos:

## 1. Resource Modeling en GraphQL → Schema Definition

En GraphQL, el "Resource Modeling" se convierte en el **diseño del Schema**. En lugar de pensar en endpoints REST, piensas en un grafo de tipos.

### Ejemplo: Schema de E-commerce

```graphql
# REST: /users, /users/{id}, /users/{id}/orders
# GraphQL: Un único endpoint con tipos relacionados

type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!  # ← Relación directa en el schema
}

type Order {
  id: ID!
  status: OrderStatus!
  items: [OrderItem!]!
  user: User!
  totalAmount: Float!
}

type Product {
  id: ID!
  name: String!
  price: Float!
  category: Category!
}

type Query {
  users: [User!]!
  user(id: ID!): User
  products(filter: ProductFilter): [Product!]!
  ordersByUser(userId: ID!): [Order!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateOrderStatus(id: ID!, status: OrderStatus!): Order!
}
```

**Key Difference**: En REST modelas **endpoints**, en GraphQL modelas **tipos y sus relaciones**.

## 2. Domain Filtering en GraphQL

El Domain Filtering en GraphQL se maneja principalmente a través de:

### a) **Resolución de Relaciones (Resolvers)**
```javascript
// Resolver para el tipo User
const resolvers = {
  User: {
    orders: async (user, args, context) => {
      // DOMAIN FILTERING: Obtiene las órdenes de ESTE usuario específico
      return context.db.orders.findMany({
        where: { userId: user.id } // Filtrado natural por la relación
      });
    }
  },
  Query: {
    user: async (_, { id }, context) => {
      // Verifica que el usuario exista (Domain Filtering)
      const user = await context.db.user.findUnique({ where: { id } });
      if (!user) {
        throw new Error('User not found'); // ← Equivalente a 404 en REST
      }
      return user;
    }
  }
};
```

### b) **Validación de Tipos y Esquema**

GraphQL valida automáticamente:
- Que los IDs sean del formato correcto
- Que los tipos de datos coincidan
- Que los campos solicitados existan en el schema


## 3. Business Filtering en GraphQL

El Business Filtering es donde GraphQL brilla, pero también introduce complejidad.

### a) **Autorización a Nivel de Resolver**
```javascript
const resolvers = {
  Query: {
    user: async (_, { id }, context) => {
      // BUSINESS FILTERING: ¿Puede este usuario ver este perfil?
      if (context.user.id !== id && !context.user.isAdmin) {
        throw new Error('Not authorized'); // ← Equivalente a 403 en REST
      }
      
      return context.db.user.findUnique({ where: { id } });
    }
  },
  
  User: {
    email: (user, args, context) => {
      // BUSINESS FILTERING: Regla "Los usuarios solo ven su propio email"
      if (context.user.id !== user.id && !context.user.isAdmin) {
        return null; // o throw new Error('Not authorized')
      }
      return user.email;
    }
  },
  
  Order: {
    items: async (order, args, context) => {
      // BUSINESS FILTERING: Solo mostrar items si pertenece al usuario o es admin
      if (context.user.id !== order.userId && !context.user.isAdmin) {
        return []; // o throw error
      }
      return order.items;
    }
  }
};
```

### b) **Directivas para Autorización**

```graphql
# Schema-first approach con directivas
type Query {
  users: [User!]! @hasRole(role: "ADMIN")
  user(id: ID!): User @isAuthenticated
}

type User {
  id: ID!
  name: String!
  email: String! @ownDataOrAdmin
  orders: [Order!]! @ownData
}
```

## 4. Materialización en GraphQL

La "materialización" sucede en los **resolvers** - cada campo en una query GraphQL puede tener su propia lógica de resolución.

```graphql
# Query del cliente
query GetUserWithOrders($userId: ID!) {
  user(id: $userId) {
    name
    email
    orders {
      id
      status
      items {
        product {
          name
          price
        }
        quantity
      }
    }
  }
}
```

```javascript
// Resolvers que materializan la respuesta
const resolvers = {
  Query: {
    user: (_, { id }) => getUserById(id), // Domain filtering
  },
  User: {
    email: (user, _, context) => {        // Business filtering
      return context.user.isAdmin ? user.email : null;
    },
    orders: (user) => getOrdersByUserId(user.id), // Domain filtering
  },
  Order: {
    items: (order, _, context) => {       // Business filtering
      return context.user.isAdmin ? order.items : filterSensitiveItems(order.items);
    }
  }
};
```

## 5. Consideraciones y Desafíos Únicos en GraphQL

### a) **N+1 Query Problem**

```javascript
// Resolver ingenuo - Problema N+1
User: {
  orders: (user) => {
    return db.orders.findMany({ where: { userId: user.id } });
    // Se ejecuta por CADA usuario en una lista
  }
}
```

**Solución**: DataLoaders para batching

```javascript
// Usando DataLoader para eficiencia
const orderLoader = new DataLoader(async (userIds) => {
  const orders = await db.orders.findMany({
    where: { userId: { in: userIds } }
  });
  return userIds.map(id => orders.filter(o => o.userId === id));
});

User: {
  orders: (user) => orderLoader.load(user.id)
}
```

### b) **Security: Query Depth y Complexity**

```javascript
// Protección contra queries maliciosas
app.use('/graphql', graphqlHTTP({
  schema: schema,
  validationRules: [
    depthLimit(5),          // Máxima profundidad
    complexityLimit(1000),  // Complejidad máxima
  ]
}));
```

### c) **Field-level Authorization**
La autorización a nivel de campo es poderosa pero compleja:
```javascript
// Patrón: Resolver wrapper para autorización
const withAuthorization = (resolver, rule) => {
  return (parent, args, context, info) => {
    if (!rule(context, parent)) {
      throw new Error('Not authorized');
    }
    return resolver(parent, args, context, info);
  };
};
```

## 6. Patrones Recomendados para GraphQL

### a) **Data Layer Separation**

```javascript
// Capa de negocio → Resolvers
// Capa de datos → Servicios/Repositorios

// userService.js - Lógica de dominio
const getUserWithOrders = async (userId, currentUser) => {
  // Domain + Business filtering
  if (!currentUser.isAdmin && currentUser.id !== userId) {
    throw new Error('Not authorized');
  }
  
  return db.user.findUnique({
    where: { id: userId },
    include: { orders: true }
  });
};

// resolvers.js
Query: {
  user: (_, { id }, context) => getUserWithOrders(id, context.user)
}
```

### b) **Directivas para Validación**
```graphql
type Mutation {
  createUser(input: CreateUserInput!): User! 
    @validateInput
    @hasRole(role: "ADMIN")
    @rateLimit(max: 10, window: "60s")
}
```


| Concepto | REST | GraphQL |
|----------|------|---------|
| **Resource Modeling** | Endpoints y verbos HTTP | **Schema con tipos y relaciones** |
| **Domain Filtering** | Parámetros query, URL hierarchy | **Resolvers + validación de schema** |
| **Business Filtering** | Lógica en controllers/middleware | **Autorización en resolvers** |
| **Materialización** | Formateo en controllers/serializers | **Ejecución de resolvers por campo** |
| **Ventaja** | Simple, caching fácil | **Flexibilidad, eficiencia de datos** |
| **Desventaja** | Over-fetching, under-fetching | **Complejidad, caching difícil** |

En GraphQL, el **Resource Modeling** se convierte en el diseño de un schema tipado que representa tu grafo de datos. El **Domain Filtering** ocurre naturalmente a través de las relaciones definidas en el schema y la resolución de datos. El **Business Filtering** se implementa principalmente en los resolvers, donde puedes aplicar reglas de negocio y autorización a nivel de tipo, campo, o incluso registro individual.

La clave en GraphQL es reconocer que **cada campo es un punto potencial de autorización y filtrado**, lo que ofrece granularidad fina pero también requiere una arquitectura cuidadosa para evitar problemas de performance y seguridad.
