# Ejemplo de Multi Stage Build con Ubuntu


Dockerfile multi-stage usando Ubuntu 24.04 como imagen base, con Python 3.11 y una aplicación Flask. Este ejemplo optimiza el tamaño de la imagen y el tiempo de construcción para pipelines de CI/CD.

```docker title="Ejemplo de Docker" linenums="1"
# Etapa de construcción
FROM ubuntu:24.04 AS builder

# Instalar Python 3.11 y pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3.11 python3-pip python3.11-venv && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar solo el archivo de requisitos para aprovechar el cache
COPY requirements.txt .
RUN python3.11 -m pip install --user -r requirements.txt

# Etapa final
FROM ubuntu:24.04

# Instalar solo el runtime de Python 3.11
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3.11 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar los binarios instalados desde la etapa builder
COPY --from=builder /root/.local /root/.local

# Copiar el código de la aplicación
COPY app.py .

# Configurar el PATH para usar los paquetes instalados
ENV PATH=/root/.local/bin:$PATH

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3.11", "app.py"]
```

```python title="Ejemplo de Aplicación" linenums="1"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde Flask en Ubuntu 24.04 con Python 3.11!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```


```yaml title="requirements.txt"
flask==2.0.1
```

### Explicación del enfoque multi-stage con Ubuntu 24.04 y Python 3.11:

1. **Etapa de construcción (builder)**:
   - Usa `ubuntu:24.04` como base para un entorno limpio y actualizado.
   - Instala Python 3.11, pip y venv, necesarios para la instalación de dependencias.
   - Limpia la lista de paquetes (`rm -rf /var/lib/apt/lists/*`) para reducir el tamaño de la capa.
   - Copia solo `requirements.txt` para aprovechar el cache de Docker y acelerar reconstrucciones.
   - Instala las dependencias en el directorio de usuario (`--user`) para facilitar la copia en la etapa final.

2. **Etapa final**:
   - Usa nuevamente `ubuntu:24.04` para mantener consistencia.
   - Instala solo el runtime de Python 3.11, omitiendo herramientas de desarrollo como pip o venv para minimizar el tamaño.
   - Copia los binarios preinstalados desde la etapa `builder` (`/root/.local`).
   - Copia el código de la aplicación (`app.py`).
   - Configura el `PATH` para usar los binarios instalados.
   - Resulta en una imagen final más ligera (~200MB frente a ~1GB si se usara una imagen completa con herramientas de desarrollo).

3. **Beneficios para CI/CD**:
   - **Cache eficiente**: Copiar solo `requirements.txt` en la etapa de construcción permite reutilizar capas si las dependencias no cambian.
   - **Tamaño reducido**: La etapa final excluye herramientas innecesarias, reduciendo el tamaño de la imagen y los tiempos de push/pull en registries.
   - **Construcciones rápidas**: La limpieza de listas de paquetes y la separación de etapas minimizan el trabajo en cada build.
   - **Despliegues optimizados**: Menor tamaño de imagen acelera las transferencias y despliegues en entornos CI/CD.

### Instrucciones para usar:
1. Coloca los tres archivos (`Dockerfile`, `app.py`, `requirements.txt`) en el mismo directorio.
2. Construye la imagen: `docker build -t flask-ubuntu-multistage .`
3. Ejecuta el contenedor: `docker run -p 5000:5000 flask-ubuntu-multistage`
4. Accede a `http://localhost:5000` para ver la aplicación.

Este enfoque multi-stage con Ubuntu 24.04 y Python 3.11 optimiza los tiempos de construcción y despliegue, ideal para pipelines de CI/CD con múltiples iteraciones diarias.
