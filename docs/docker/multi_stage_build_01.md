# Multi Stage Build

Ejemplo de Dockerfile usando Flask con un enfoque multi-stage para optimizar el tamaño de la imagen y reducir el tiempo de construcción en pipelines de CI/CD:

```docker title="Ejemplo de Docker" linenums="1"
# Etapa de construcción
FROM python:3.9-slim AS builder

WORKDIR /app

# Copiar solo los archivos necesarios para instalar dependencias
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Etapa final
FROM python:3.9-slim

WORKDIR /app

# Copiar solo los binarios instalados desde la etapa builder
COPY --from=builder /root/.local /root/.local

# Copiar el código de la aplicación
COPY app.py .

# Configurar el PATH para usar los paquetes instalados
ENV PATH=/root/.local/bin:$PATH

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
```

```python title="Ejemplo de Aplicación" linenums="1"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde Flask en Docker Multi-stage!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```yaml title="requirements.txt"
flask==2.0.1
```

Este ejemplo demuestra cómo el enfoque multi-stage reduce el tiempo de CI/CD:

1. **Etapa de construcción (builder)**:
   - Usa `python:3.9-slim` como base para mantener la imagen ligera
   - Instala las dependencias en un directorio de usuario específico
   - Solo copia `requirements.txt` para aprovechar el cache de Docker

2. **Etapa final**:
   - Usa la misma base `python:3.9-slim` para consistencia
   - Copia solo los binarios preinstalados desde la etapa builder
   - Resulta en una imagen final más pequeña (~150MB vs ~900MB con una imagen python completa)
   - Menor tamaño = tiempos más rápidos de push/pull en registries

3. **Beneficios para CI/CD**:
   - Construcciones más rápidas debido al cache de capas
   - Menor tiempo de transferencia de imágenes
   - Despliegues más rápidos por el tamaño reducido
   - Menor uso de almacenamiento en registries

Para usar estos archivos:
1. Coloca los tres archivos en el mismo directorio
2. Construye la imagen: `docker build -t flask-multistage .`
3. Ejecuta el contenedor: `docker run -p 5000:5000 flask-multistage`
4. Accede a http://localhost:5000 para ver la aplicación

La optimización multi-stage reduce significativamente los tiempos de construcción y despliegue en pipelines CI/CD, especialmente en entornos con múltiples builds diarios.
