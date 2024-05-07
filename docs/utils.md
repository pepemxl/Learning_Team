# Herramientas

## Para crear y revisar APIs usaremos algunas herramientas

En visual studio trabajaremos con la herramienta REST Client v0.24.5, y con ella seremos capaces de emular herramientas como postman.

Esta herramienta soporta las siguientes extensiones:
- `.http`
- `.rest`

referencias en 
[https://marketplace.visualstudio.com/items?itemName=humao.rest-client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

Por ejemplo un POST se haria de la siguiente manera:

```http
POST https://example.com/comments HTTP/1.1
content-type: application/json

{
    "name": "sample",
    "time": "Wed, 7 Nov 2021 18:27:50 GMT"
}
```
