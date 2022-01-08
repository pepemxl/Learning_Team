# Primer ejemplo con un servidor Node.js
Usaremos el modulo `http` y su funci&oacute;n `createServer` para crear un peque&ntilde;o servidor.

Aqui configuramos un hostname y un puerto el cual al escuchar cualquier tipo request(petici&oacute;n) mandar&aacute; llamar la funci&oacute;n que designemos, que este caso es un simple console.log, 

En este evento request dos objetos ser&aacute;n creados:
- request - http.IncommingMessage
- response - http.ServerResponse

Estos dos objetos son los que nos permiten la comunicaci&oacute;n b&aacute;sica en http, donde el request contiene los detalles de la llamada y response contiene la respuesta que le damos a esa llamada.

```js
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hola Mundo de Node');
});

server.listen(port, hostname, () => {
  console.log(`El servidor se está ejecutando en http://${hostname}:${port}/`);
});
```



para ejecutarlo simplemente tecleamos `node app.js`
y tendremos una salida como la siguiente en nuestra consola:

```bash
El servidor se está ejecutando en http://127.0.0.1:3000/
```
