# Introducción a Dockers

Docker es una plataforma abierta para desarrollar, enviar y ejecutar aplicaciones. Docker le permite separar sus aplicaciones de su infraestructura para que pueda entregar software rápidamente. Con Docker, puede administrar su infraestructura de la misma manera que administra sus aplicaciones.

La tecnología Docker utiliza el kernel de Linux y sus funciones, como los grupos de control y los espacios de nombre, para dividir los procesos y ejecutarlos de manera independiente. El propósito de los contenedores es ejecutar varios procesos y aplicaciones por separado para que se pueda aprovechar mejor la infraestructura y, al mismo tiempo, conservar la seguridad que se obtendría con los sistemas individuales.

**Docker mantiene todo organizado**  aislando cada cosa en un contenedor e imagen.

Alguno de los componentes clásicos de docker son:

- **Base images** son imagenes que no tienen imagen padre, usualmente son OS como Ubuntu o Debian.
- **Images** Los blueprints de nuestra aplicación que forman la base de los contenedores. 
- **Containers** Creados apartir de las imagenes de Docker donde se corren las aplicaciones. Creamos un contenedor usando `docker run`.
- **Docker Daemon** Un background service que maneja los builds.
- **Docker Client** Una herramienta de linea de comando que nos permite interactuar con Docker.
- **Docker Hub** -  Un registro de imagenes de docker. 

## Recursos Aislados

Los contenedores que Docker crea son aislados respecto a:

1. `PID` namespace Process identifiers and capabilities
2. `UTS` namespace Host and domain name
3. `MNT` namespace File system access and structure
4. `IPC` namespace Process communication over shared memory
5. `NET` namespace Network access and structure
6. `USR` namespace User names and identifiers
7. `chroot()` Controls the location of the file system root
8. `cgroups` Resource protection

## Comandos usuales

```yaml title=" Example in src/docker/example_01/flash-app/Dockerfile"
FROM python:3.7-alpine
# The FLASK_APP environment variable is the name of the module to import at flask run
ENV FLASK_APP app.py
# "development" is equal to "debug mode", the server will automatically reload if code changes
ENV FLASK_ENV development
# make the server publicly available simply by adding --host=0.0.0.0 to the command line
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 5000

CMD [ "flask", "run" ]
```

```yaml title="src/docker/example_01/flask-app/app.py"
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World in Example 01 Container!'
```


- `docker build -t docker:example_01`  # example_01/docker_build.bat
    - `--tag , -t 		Name and optionally a tag in the 'name:tag' format`
- `docker ps` to list containers running
- `docker images` to list images locally available.
- `docker pull <image_name>` to retrieve remote images.
- `docker start <container_name>` start container.
- `docker stop <container_name>` stop container.
- `--rm` option tells Docker to remove the intermediate images.


## Creación de la imagen base

El primer paso es construir un contenedor donde le indicamos cuales son los paquetes que necesitará.

```docker
FROM ubuntu
RUN apt-get update && apt-get install gcc git -y
```

Para crear la imagen basta correr:

```bash title="Crear una imagen"
docker build .
```

El `.` le dice a Docker buscar en el directorio actual por un Dockerile.

## Data

Por defecto todos los archivos creados en un contenedor son guardados en una capa contenedor escribible (writable layer).

Lo cual quiere decir que esta data desaparece al terminar el contenedor.

Escriabir en una capa requiere un driver de manejo de datos, lo cual hace un tanto lenta la escritura/lectura de datos, por lo cual es recomendable agregar un volumen que utilizará directamente el filesystem del host.


Docker nos da dos opciones:

1. volumes y 
2. bind mounts.

### Volumes

Los contenedores de Docker corren aplicaciones aisladas del sistema.
Sin embargo para persistir data es necesario usar Docker volumes o bind mounts.

### Como manejar Volumes

Docker permite manejar volumenes, los cuales podemos nombrar o usar de manera anonima.

#### Creando Volumenes

```bash title="Crear Volumen"
docker volume create data_volume
data_volume
```

## Tambien podemos usar el Python SDK

```bash title="Install Docker"
pip install docker
```

Los componentes clásicos de Docker se pueden dividir en dos categorías principales: **Docker Engine** (el núcleo) y **herramientas del ecosistema**.

## Componentes Fundamentales del Docker Engine

### **Docker Daemon (`dockerd`)**

- **Qué es**: El servicio background que gestiona los contenedores
- **Función**: Escucha peticiones de la API de Docker y gestiona imágenes, contenedores, redes y volúmenes
- **Ejemplo**: `dockerd --log-level=debug`

### **Docker Client (`docker`)**

- **Qué es**: La CLI que los usuarios usan para interactuar con el Daemon
- **Función**: Envía comandos al Daemon y muestra los resultados
- **Ejemplo**: `docker run hello-world`

### **Docker API**

- **Qué es**: API REST que permite la comunicación entre Client y Daemon
- **Función**: Expone endpoints para gestionar todos los recursos de Docker
- **Ejemplo**: `curl --unix-socket /var/run/docker.sock http://v1.42/containers/json`

### **Containerd**

- **Qué es**: Runtime de containers que Docker utiliza internamente
- **Función**: Gestiona el ciclo de vida completo de los contenedores
- **Relación**: Docker Daemon → containerd → runc

### **Runc**

- **Qué es**: Herramienta CLI para crear y ejecutar containers según OCI
- **Función**: Implementación de bajo nivel que realmente ejecuta los contenedores
- **Estándar**: Cumple con Open Container Initiative (OCI)

## Componentes de Almacenamiento y Empaquetado

### **Docker Images**

- **Qué es**: Plantillas de solo lectura para crear contenedores
- **Ejemplo**: `ubuntu:20.04`, `nginx:alpine`
- **Estructura**: Capas unidas mediante Union File System

### **Dockerfile**

- **Qué es**: Archivo de texto con instrucciones para construir imágenes
- **Ejemplo**:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### **Docker Registry**

- **Qué es**: Repositorio para almacenar y distribuir imágenes
- **Público**: Docker Hub (`docker.io`)
- **Privado**: Docker Trusted Registry, Amazon ECR, Google Container Registry

### **Docker Hub**

- **Qué es**: Registry público por defecto de Docker
- **Función**: Compartir y descubrir imágenes oficiales y de comunidad
- **URL**: https://hub.docker.com

## Componentes de Networking

### **Docker Networking**

- **Tipos**:
  - `bridge`: Red por defecto para contenedores aislados
  - `host`: Comparte el network stack del host
  - `overlay`: Para comunicación entre múltiples hosts (Docker Swarm)
  - `macvlan`: Asigna dirección MAC a contenedores

### **DNS embebido**

- **Qué es**: Resolución DNS automática entre contenedores
- **Función**: Los contenedores pueden resolverse por nombre de servicio

## Componentes de Persistencia

### **Docker Volumes**

- **Qué es**: Mecanismo preferido para persistir datos
- **Ventaja**: Gestionado por Docker, independiente del filesystem del host
- **Ejemplo**: `docker volume create my_volume`

### **Bind Mounts**

- **Qué es**: Montar directorios específicos del host en contenedores
- **Uso**: Desarrollo y configuraciones específicas
- **Ejemplo**: `-v /home/user/app:/app`

### **tmpfs mounts**
- **Qué es**: Montajes en memoria RAM
- **Uso**: Datos temporales que no deben persistir
- **Ejemplo**: `--tmpfs /tmp`

## Herramientas

### **Docker Compose**

- **Qué es**: Herramienta para definir y ejecutar aplicaciones multi-contenedor
- **Archivo**: `docker-compose.yml`
- **Uso**: Desarrollo local y testing

### **Docker Swarm**

- **Qué es**: Herramienta de orquestación nativa de Docker
- **Función**: Clustering y gestión de servicios distribuidos
- **Alternativa**: Kubernetes (más popular actualmente)

### **Docker Machine**

- **Qué es**: Herramienta para provisionar hosts Docker
- **Uso**: Crear máquinas virtuales con Docker instalado
- **Ejemplo**: `docker-machine create my-vm`

## Ejemplo de Flujo de Trabajo Clásico

```bash
# 1. Construir imagen desde Dockerfile
docker build -t mi-app:1.0 .

# 2. Subir imagen al registry
docker tag mi-app:1.0 mi-registry.com/mi-app:1.0
docker push mi-registry.com/mi-app:1.0

# 3. Ejecutar contenedor
docker run -d -p 80:5000 --name mi-contenedor mi-app:1.0

# 4. Gestionar con Docker Compose
docker-compose up -d

# 5. Inspeccionar recursos
docker ps
docker logs mi-contenedor
docker inspect mi-contenedor
```

## Evolución Reciente

Los componentes han evolucionado, pero estos son los **clásicos** que forman la base de Docker.

- **Kubernetes** en lugar de Docker Swarm
- **containerd** directamente sin Docker Daemon
- **Podman** como alternativa a Docker Client


