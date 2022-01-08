# Node.js

**Node.js** es una plataforma cruzada de javascript open source, que nos permite crear herramientas de linea de comando y archivos que podran correr del lado del servidor fuera del explorador. Esta herramienta le ha dado un gran empuje a javascript convirtiendolo en m&aacute;s que un lenguaje de interacci&oacute;n con el usuario en los exploradores.


Actualmente node corre sobre el famoso motor **V8** que forma parte del core de Google Chrome. 

Una limitaci&oacute;n importante es que Node.js corre un &uacute;nico proceso o thread, sin crear nuevos threads para nuevos request tenemos un importante cuello de botella, para las aplicaciones intensivas.

Node.js nos proporciona  un conjunto de herramientas I/O asincronas, lo cual alivia el problema de bloqueo. Tomar en cuenta que lo usual es desarrollar aplicaciones que tienen un comportamiento de no bloqueo de tareas.

Cuando realizamos una tarea de I/O, como prodira ser:
- acceso a una base de datos
- llamada http

Node.js NO bloquear&aacute; el thread, si no que continuar&aacute; con la tarea una vez que la respuesta regrese, este manejo es que deberemos revisar m&aacute;s adelante para revisar en que casos Node.js podr&aacute; sustituir a otros lenguajes en el backend.

En principio Node.js nos permite manejar miles de conexiones concurrentes con un solo servidor, sin la necesidad de tener que utilizar threads concurrentes, que usualmente son dificiles de manejar/orquestar.




# Primer Ejemplo de Node

posiblemente la manera m&aacute;s sencilla de crear un servidor http, es usando node con el siguiente script:

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

En este caso no tenemos ning&uacute;n contenido pertinente en el request, sin embargo en la respuesta ponemos el estado, el tipo de contenido y cerramos la respuesta con el contenido de la misma.

Recordemos que una vez ejecutada la instrucci&oacute;n est&aacute; vivir&aacute; en node, para poder testear cambios en nuestro archivos .js tendremos que parar el servidor actual y volverlo a inicializar.


En Node.js tenemos una gran cantidad de frameworks y herramientas, por el momento nos enfocaremos en las siguientes:
- [Express](https://expressjs.com/)
- [featherJS](https://feathersjs.com/)
- [Next.js](https://nextjs.org/)
- [Nx](https://nx.dev/)
- [Socket.io](https://socket.io/)
- [Yarn](https://yarnpkg.com/en/)



Para empezar a usar Node.js debemos dorminar algunos aspectos b&aacute;sicos de JS, como son:

- Lexical Structure
- Expressions
- Types
- Classes
- Variables
- Functions
- this
- Arrow Functions
- Loops
- Scopes
- Arrays
- Template Literals
- Semicolons
- Strict Mode
- ECMAScript 6, 2016, 2017



trataremos de dar una peque&ntilde;a introducci&oacute;n a ellos a tr&aacute;ves y durante los ejemplos de node.





