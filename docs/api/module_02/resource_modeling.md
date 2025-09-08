# Modelado de los Recursos

**Resource Modeling** o **Mapeo de Dominio** es un concepto fundamental en el diseño de APIs RESTful que consiste en mapear los conceptos de tu dominio de negocio a recursos HTTP que pueden ser manipulados mediante operaciones estándar.

## ¿Qué es Resource Modeling?

Es el proceso de identificar y definir los **recursos** (entidades, conceptos) de tu dominio y representarlos como endpoints en tu API, siguiendo los principios REST.

## Principios Clave del Resource Modeling

### 1. **Todo es un Recurso**

- Los recursos son entidades o conceptos del dominio
- Cada recurso tiene un identificador único (URI)
- Ejemplos: `users`, `products`, `orders`, `payments`

### 2. **Operaciones mediante HTTP Verbs**

- `GET` - Recuperar recursos
- `POST` - Crear nuevos recursos  
- `PUT`/`PATCH` - Actualizar recursos
- `DELETE` - Eliminar recursos

### 3. **Stateless**

- Cada request contiene toda la información necesaria
- No hay sesiones almacenadas en el servidor

## Proceso de Resource Modeling

### Paso 1: Identificar Entidades del Dominio

```python
# Dominio de E-commerce
- User
- Product
- Order
- OrderItem
- Category
- Review
- Payment
- ShippingAddress
```

### Paso 2: Mapear a Recursos REST

```python
# Mapeo a recursos HTTP
/users              # Colección de usuarios
/users/{id}         # Usuario específico
/products           # Colección de productos  
/products/{id}      # Producto específico
/orders             # Órdenes
/orders/{id}        # Orden específica
/orders/{id}/items  # Items de una orden
```

### Paso 3: Definir Relaciones entre Recursos

```python
# Relaciones jerárquicas
/users/{userId}/orders          # Órdenes de un usuario
/users/{userId}/orders/{orderId} # Orden específica de un usuario

# Relaciones directas  
/orders/{orderId}/items         # Items de una orden
/products/{productId}/reviews   # Reviews de un producto
```

## Ejemplo Completo: API de E-commerce

### Modelado de Recursos

```python
# RECURSOS PRINCIPALES
GET    /users                   # Listar usuarios
POST   /users                   # Crear usuario
GET    /users/{id}              # Obtener usuario
PUT    /users/{id}              # Actualizar usuario
DELETE /users/{id}              # Eliminar usuario

# SUB-RECURSOS Y RELACIONES
GET    /users/{id}/orders              # Órdenes del usuario
POST   /users/{id}/orders              # Crear orden para el usuario
GET    /users/{id}/orders/{orderId}    # Orden específica

# RECURSOS INDEPENDIENTES
GET    /products                # Listar productos
GET    /products/{id}           # Obtener producto
GET    /categories              # Listar categorías
```

### Ejemplo de Implementación en Flask

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Modelado de Recurso User
class User(Resource):
    def get(self, user_id=None):
        if user_id:
            # Obtener usuario específico
            return jsonify({"user": {"id": user_id, "name": "John Doe"}})
        else:
            # Listar todos los usuarios
            return jsonify({"users": [{"id": 1, "name": "John Doe"}]})
    
    def post(self):
        # Crear nuevo usuario
        data = request.get_json()
        return jsonify({"user": data}), 201

# Modelado de Recurso Order con relación a User
class UserOrders(Resource):
    def get(self, user_id):
        # Obtener órdenes de un usuario
        return jsonify({"orders": [{"id": 1, "user_id": user_id}]})
    
    def post(self, user_id):
        # Crear orden para un usuario
        data = request.get_json()
        return jsonify({"order": {**data, "user_id": user_id}}), 201

# Definición de endpoints
api.add_resource(User, '/users', '/users/<string:user_id>')
api.add_resource(UserOrders, '/users/<string:user_id>/orders')

if __name__ == '__main__':
    app.run(debug=True)
```

## Mejores Prácticas en Resource Modeling

### 1. **Nombrado Consistente**

```python
# ✅ Bien
/users
/user-preferences
/order-items

# ❌ Mal
/getUsers
/user_preferences
/OrderItems
```

### 2. **Versión de API**

```python
# Incluir versión en el path
/api/v1/users
/api/v2/products
```

### 3. **Filtros, Paginación y Sorting**

```python
# Parámetros de query para operaciones complejas
GET /products?category=electronics&price_min=100
GET /users?page=2&limit=50&sort=name
```

### 4. **Estado como Recurso**

```python
# Modelar estados como sub-recursos
POST /orders/{id}/cancel    # Cancelar orden
POST /orders/{id}/complete  # Completar orden
```

### 5. **Acciones como Sub-recursos**

```python
# Acciones complejas como endpoints
POST /users/{id}/activate
POST /users/{id}/deactivate
POST /users/{id}/reset-password
```

## Patrones Comunes de Modelado

### 1. **Singleton Resources**

```python
# Recursos únicos (no tienen ID)
GET /configuration
PUT /settings
```

### 2. **Composite Resources**

```python
# Recursos que agrupan múltiples entidades
GET /dashboard  # Devuelve users, orders, stats
```

### 3. **Process Resources**

```python
# Recursos que representan procesos
POST /imports    # Iniciar proceso de importación
GET /imports/{id} # Estado del import
```

## Ejemplo de Modelado para Diferentes Dominios

### Dominio: Red Social

```python
/users/{id}/followers       # Seguidores de un usuario
/users/{id}/following       # Usuarios que sigue
/posts/{id}/likes          # Likes de un post
/posts/{id}/comments       # Comentarios de un post
/messages                  # Mensajes privados
```

### Dominio: Sistema de Blog

```python
/authors/{id}/posts        # Posts de un autor
/posts/{id}/tags           # Tags de un post
/categories/{id}/posts     # Posts de una categoría
/comments/{id}/replies     # Respuestas a un comentario
```

## Errores Comunes a Evitar

1. **Verbosity in URLs**: No usar verbos en las URLs
   - ❌ `GET /getUsers`
   - ✅ `GET /users`

2. **Ignoring HTTP Semantics**: No usar los métodos HTTP correctamente
   - ❌ `POST /users/delete`
   - ✅ `DELETE /users/{id}`

3. **Over-nesting**: Evitar anidamiento excesivo
   - ❌ `GET /users/1/orders/5/items/3/product/2`
   - ✅ `GET /order-items/3`


El **Resource Modeling** es la columna vertebral de una API RESTful bien diseñada. Se trata de:

1. **Identificar** las entidades clave de tu dominio
2. **Mapear** estas entidades a recursos HTTP
3. **Definir** relaciones jerárquicas entre recursos
4. **Utilizar** correctamente los verbos HTTP
5. **Mantener** consistencia en el nombrado y estructura

Un buen modelado de recursos resulta en una API que es:
- ✅ **Intuitiva** para los desarrolladores
- ✅ **Escalable** para futuras features
- ✅ **Mantenible** a largo plazo
- ✅ **Consistente** en su diseño

