# JWT - JSON Web Tokens

JSON Web Tokens son la forma de mandar información del cliente al servidor en el caso de `stateles` con cierto grado de seguridad.


Del lado del servidor un json es generado al loguearse el usuario. Se le agrega una llave `secret key`, la cual es guardada del lado del cliente.

De esta manera podemos trabajar con `single web applications`.

La forma usual de hacer esto era solo usar sessiones y autenticación basada en cookies.

## Ventajas y desventajas de cookies sobre JWT para autenticación.

## Configurando Base de Datos

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




# OAuth2

**OAuth2** es un framework de autorización que permite a aplicaciones como Facebook, GitHub, Google obtener acceso a cuentas de un usuario sobre un servicio **HTTP**. 

Este framwork funciona delegando la autenticación del usuario al servicio que aloja una cuenta del usuario y autorizando a las aplicaciones de terceros(third-party) para acceder a la cuenta del usuario. OAuth 2 proporciona flujos de autorización para aplicaciones web y de escritorio, así como para dispositivos móviles. 

Esto permite a los usuarios compartir información de su cuenta con otras cuentas sin realmente compartir su `username` y `password`. 



## Roles en OAuth

- Resource Owner: El el propietario/usuario que autoriza a una aplicación acceso a su cuenta. Está aplicación puede contar con cierto alcance definido por el ususario.
- Client: El cliente aqui es la aplicación que desea acceso a la cuenta del usuario, el usuario debe autorizar este acceso mediante una API.
- Resource Server: El servidor de recursos protegidos.
- Authorization Server: El servidor de autorización  que verifica la identidad del usuario, y después emite tokens de acceso. Es decir, un servicio API.






