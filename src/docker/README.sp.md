# Volumenes en Docker Compose

Los volúmenes en Docker Compose son contenedores persistentes que se utilizan para almacenar datos generados por contenedores Docker. Los volúmenes se crean y se montan en los contenedores de Docker de forma que se pueda acceder a los datos desde ellos, y se mantienen aún cuando el contenedor que los utiliza se elimina o se desmonta.

Para utilizar volúmenes en Docker Compose, debes especificarlos en el archivo `docker-compose.yml` de tu aplicación. Por ejemplo, si quieres crear un volumen que se monta en un contenedor llamado `app`, puedes añadir la siguiente línea a tu archivo `docker-compose.yml`:

```docker
volumes:
  app-data:
```

Esto creará un volumen llamado `app-data` que se puede utilizar en el contenedor `app`. Luego, puedes montar el volumen en el contenedor `app` en el archivo `docker-compose.yml` de la siguiente manera:

```docker
services:
  app:
    volumes:
      - app-data:/var/lib/app
```

En este ejemplo, se monta el volumen `app-data` en la ruta `/var/lib/app` del contenedor.



