# GraphQl Underfetching

 El **under-fetching** ocurre cuando una consulta a la API no proporciona toda la información que necesitas en una sola solicitud. Esto significa que debes realizar **múltiples solicitudes adicionales** para completar los datos requeridos, lo que puede ser ineficiente.

---

### **Ejemplo de Under-Fetching**

#### Supongamos una API REST:
- Endpoint: `/user/123`
  ```json
  {
    "id": 123,
    "name": "Juan",
    "email": "juan@example.com"
  }
  ```

Si quieres obtener también los **posts** asociados a este usuario, necesitas hacer otra solicitud:
- Endpoint: `/user/123/posts`
  ```json
  [
    {
      "id": 1,
      "title": "Mi primer post",
      "content": "Contenido del post..."
    },
    {
      "id": 2,
      "title": "Mi segundo post",
      "content": "Contenido del post..."
    }
  ]
  ```

En este caso, tienes **under-fetching** porque debes realizar **dos solicitudes** para obtener toda la información necesaria: una para los datos del usuario y otra para sus posts.

---

### **Cómo GraphQL Soluciona el Under-Fetching**
Con GraphQL, puedes realizar una **sola consulta** para obtener toda la información que necesitas, incluso si los datos están relacionados.

#### Ejemplo en GraphQL:
```graphql
query {
  user(id: 123) {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```

La respuesta incluirá todos los datos en un solo paso:
```json
{
  "data": {
    "user": {
      "id": 123,
      "name": "Juan",
      "email": "juan@example.com",
      "posts": [
        {
          "id": 1,
          "title": "Mi primer post",
          "content": "Contenido del post..."
        },
        {
          "id": 2,
          "title": "Mi segundo post",
          "content": "Contenido del post..."
        }
      ]
    }
  }
}
```

---

### **Ventajas de Evitar Under-Fetching con GraphQL**

1. **Eficiencia**: 
   - Obtienes todos los datos necesarios en una sola solicitud.
2. **Flexibilidad**:
   - El cliente decide qué datos necesita (no está limitado por endpoints predefinidos).
3. **Mejor experiencia para el cliente**:
   - Evita múltiples solicitudes, reduciendo la latencia y simplificando el desarrollo.

