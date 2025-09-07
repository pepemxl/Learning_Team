# Multiprocesos en Docker

Para ejecutar múltiples instancias de una aplicación Flask en puertos diferentes (del 6001 al 6010) usando Docker, hay varias estrategias. 

## Opción 1: Usando Docker con puertos mapeados individualmente

Podemos ejecutar múltiples contenedores manualmente mapeando cada puerto:

```bash
for port in {6001..6010}; do
    docker run -d -p $port:5000 --name flask-app-$port <imagen-de-flask>
done
```


- `-p $port:5000`: Mapea el puerto `$port` del host al puerto 5000 del contenedor
- `-d`: Ejecuta en segundo plano (detached mode)
- `--name flask-app-$port`: Asigna un nombre único a cada contenedor

## Opción 2: Usando Docker Compose 

Creamos un archivo `docker-compose.yml`:

```yaml
version: '3.8'
services:
  flask-app:
    image: imagen-de-flask
    ports:
      - "6001:5000"
      - "6002:5000"
      - "6003:5000"
      - "6004:5000"
      - "6005:5000"
      - "6006:5000"
      - "6007:5000"
      - "6008:5000"
      - "6009:5000"
      - "6010:5000"
    deploy:
      replicas: 10
```

```bash title="Ejecutamos"
docker-compose up -d
```

## Opción 3: Usando un script de despliegue escalable

Creamos un script `deploy-my-flask.sh`:

```bash
#!/bin/bash
IMAGE_NAME="imagen-de-flask"
BASE_PORT=6001
INSTANCES=10

for ((i=0; i<$INSTANCES; i++)); do
    PORT=$(($BASE_PORT + $i))
    docker run -d \
        --name flask-instance-$PORT \
        -p $PORT:5000 \
        -e FLASK_PORT=5000 \
        $IMAGE_NAME
    echo "Instancia ejecutándose en puerto $PORT"
done
```

## Opción 4: Usando un reverse proxy + múltiples instancias

Para producción, es mejor usar un approach con Nginx:

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - flask-app

  flask-app:
    image: imagen-de-flask
    deploy:
      replicas: 10
    environment:
      - FLASK_PORT=5000

  load-balancer:
    image: nginx:alpine
    ports:
      - "6000:80"
    volumes:
      - ./load-balancer.conf:/etc/nginx/nginx.conf
    depends_on:
      - flask-app
```

**nginx.conf para load balancing:**
```nginx
events {}
http {
    upstream flask_servers {
        server flask-app:5000;
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://flask_servers;
        }
    }
}
```

## Algunas consideraciones importantes

1. **Debemos asegurarnos que la aplicación Flask escucha en todas las interfaces (bind 0.0.0.0):**

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

2. **Para entornos de producción**, usar:
   - Gunicorn como WSGI server
   - Un load balancer como Nginx
   - Orquestación con Kubernetes o Docker Swarm

3. **Debemos verificar que las instancias estén corriendo**
    - podemos hacer un curl o agregar un hearth beat.

```bash
docker ps
curl http://localhost:6001
```

4. **No es conveniente ni recomendable ejecutar múltiples procesos de la aplicación en un solo contenedor Docker para producción.** 

## Por qué NO debes hacer múltiples procesos en un contenedor:

1. **Violación del principio de un proceso por contenedor**: Docker está diseñado para ejecutar un proceso principal por contenedor.

2. **Problemas con señales y shutdown**: Docker envía señales (como SIGTERM) al proceso principal (PID 1). Si tienes múltiples procesos, el shutdown no se maneja correctamente.

3. **Dificultad para escalar**: No puedes escalar individualmente los procesos dentro del mismo contenedor.

4. **Problemas de logging**: Los logs de múltiples procesos se mezclan, haciendo difícil el debugging.

5. **Mayor complejidad en monitoreo**: Es difícil monitorear la salud de procesos individuales.

6. **Menor confiabilidad**: Si un proceso falla, puede afectar a los otros procesos en el mismo contenedor.

### Opción 1: Un contenedor por proceso + Orquestador
```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  flask-app:
    image: tu-app-flask:prod
    deploy:
      replicas: 10
    ports:
      - "5000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - flask-app
```

### Opción 2: Usar Gunicorn para múltiples workers EN UN SOLO CONTENEDOR

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt gunicorn
COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

```bash
# Ejecutar con múltiples workers en un contenedor
docker run -d -p 5000:5000 --name flask-app tu-imagen-flask
```

### Opción 3: Kubernetes Deployment
```yaml
# flask-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 10
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-app
        image: imagen-de-flask:prod
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  selector:
    app: flask-app
  ports:
  - port: 80
    targetPort: 5000
```

## Herramientas específicas para múltiples procesos (si es NECESARIO):

Si realmente necesitamos múltiples procesos, usamos un init process manager:

```dockerfile
# Usando supervisord (NO recomendado para producción)
FROM python:3.9-slim

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
```

## Comparación de enfoques

| Enfoque | Escalabilidad | Mantenibilidad | Performance | Recomendado |
|---------|---------------|----------------|-------------|-------------|
| Múltiples contenedores | ✅ Excelente | ✅ Excelente | ✅ Excelente | **SÍ** |
| Gunicorn workers | ✅ Buena | ✅ Buena | ✅ Buena | **SÍ** |
| Múltiples procesos en contenedor | ❌ Mala | ❌ Mala | ⚠️ Regular | **NO** |

## **Para producción**
1. **Usa un contenedor por proceso** con un orquestador (Kubernetes, Docker Swarm)
2. **Emplea Gunicorn/Uvicorn** para manejar múltiples workers dentro del mismo proceso
3. **Nunca** ejecutes múltiples procesos de aplicación en el mismo contenedor





