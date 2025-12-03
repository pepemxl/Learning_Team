from fastapi import FastAPI
from pydantic import BaseModel

# Instanciamos la aplicación de FastAPI
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
    print(item.name, item.price, item.is_offer)
    return item

# Ejecutar: uvicorn main:app --reload