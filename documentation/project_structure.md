# Como manejaremos la estructura de nuestros proyectos.

Tendremos un docker-compose.yml en la raiz de todos los subproyectos, y cada subproyecto contendrá a su vez el Dockerfile necesario para crear el servicio
```
myproject/
  - auth/
    - Dockerfile
  - marketing/
    - Dockerfile
  - billing/
    - Dockerfile
  - contact/
    - Dockerfile
  - user/
    - Dockerfile
  - docker-compose.yml
```

De esta manera cada servicio contiene su propio `Dockerfile`, pero todos ellos estan en el mismo proyecto. Y cada proyecto estar escrito en su propio lenguaje!!!