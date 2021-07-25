# JWT - JSON Web Tokens

JSON Web Tokens son la forma de mandar información del cliente al servidor en el caso de `stateles` con cierto grado de seguridad.


Del lado del servidor un json es generado al loguearse el usuario. Se le agrega una llave `secret key`, la cual es guardada del lado del cliente.

De esta manera podemos trabajar con `single web applications`.

La forma usual de hacer esto era solo usar sessiones y autenticación basada en cookies.

## Ventajas y desvejas de cookies sobre JWT para autenticación.

## Configurando Base  de Datos

En este sentido puede ser una base de datos, MySQL o PostGre, por el momento no recomiendo usar una MSSQL debido a que el soporte de conexiones
de linux a MSSQL no es bueno lo que ha provocado que los conectores disponibles tengan un bajo rendimiento.

Creemos una base de datos

```
psql
create database flask_jwt_auth;
\q
```

para eso cambiemos el nombre de la base de datos en `project/server/config.py`
```
database_name = 'flask_jwt_auth'
```
y setiemos las siguientes variables de ambiente 

```linux
export APP_SETTINGS="project.server.config.DevelopmentConfig"
```
```windows
set APP_SETTINGS="project.server.config.DevelopmentConfig"
```







