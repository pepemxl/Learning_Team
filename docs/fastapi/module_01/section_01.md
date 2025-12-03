# FastAPI

**FastAPI** es un **framework web moderno, rápido (de alto rendimiento) y fácil de usar** para crear **APIs** con Python 3.7+ basado en **type hints**, usualmente llamado **annotations**, lo cual es una excelente practica en favor del performance y mantenimiento de sistemas basados en python.


## 1. **Rápido y de alto rendimiento**

- Uno de los frameworks más rápidos disponibles
- Comparable en velocidad con Node.js y Go
- Basado en **Starlette** (para web) y **Pydantic** (para validación de datos)

## 2. **Fácil de usar**

- Sintaxis clara e intuitiva
- Autocompletado en editores de código
- Menos código repetitivo

## 3. **Documentación automática**

- Genera automáticamente documentación interactiva:
    - **Swagger UI** (`/docs`)
    - **ReDoc** (`/redoc`)
- No necesitas escribir documentación manualmente

## 4. **Basado en estándares**

- Compatible con **OpenAPI** y **JSON Schema**
- Sigue especificaciones como OpenAPI, JSON Schema, OAuth2, etc.

## 5. **Validación automática**

- Valida automáticamente los datos de entrada usando Pydantic
- Devuelve errores descriptivos cuando los datos son inválidos

## Ejemplo básico

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Crear aplicación
app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Endpoint GET
@app.get("/")
def read_root():
    return {"Hello": "Pepe"}

# Endpoint GET con parámetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Endpoint POST
@app.post("/items/")
def create_item(item: Item):
    return item

# Ejecutar: uvicorn main:app --reload
```

```bash title="GET localhost:8000/"
{
  "Hello": "Pepe"
}
```

```bash title="GET http://localhost:8000/items/54?q=hola mundo"
GET 'http://localhost:8000/items/54?q=hola mundo'
```

```bash title="GET http://localhost:8000/items/54?q=hola mundo"
{
    "item_id": 54,
    "q": "hola mundo"
}
```

```bash
 POST 'localhost:8000/items/' \
  --header 'Content-Type: application/json' \
  --body '{
    "name": "Juguete",
    "price": "1000",
    "is_offer": false
}'
```

```bash title="Salida"
{
    "name": "Juguete",
    "price": "1000",
    "is_offer": false
}
```


```bash
# Instalación
pip install fastapi uvicorn

# Ejecución
uvicorn main:app --reload
```
