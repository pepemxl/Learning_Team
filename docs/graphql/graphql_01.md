# Como funciona Graphql

Para entender como funciona GraphQL primero veremos los ejemplos clásicos de como obtener información usando REST.

Usualmente para obtener informacion hariamos una llamada a una API
- `personas\get_user_info?name=pepe`

lo cual nos devolvería una respuesta del estilo:

```
[{
    "id": 1,
    "type": "tipo_01",
    "status": "open",
    "name": "pepe",
    "data" : [
        "link1",
        "link2",
        "link3",
        "link4",
        "link5",
        .....
    ]
}]
```
Ahora si yo quiero obtener otra información tengo que hacer más request a distintos endpoints:

- `mipagina\myendpoint-02`
- `mipagina\myendpoint-03`
- `mipagina\myendpoint-04`
- `mipagina\myendpoint-05`
- `mipagina\myendpoint-06`

Ahora en graphql para obtener información nosotros también haríamos un http request

`POST /graphql`

```graphql
query {
    personas(name: "pepe") {
        id
        type
        status
        name
        data
    }
}
```

Esto le dirá que campos queremos, con la ventaja de que le podemos decir exactamente que campos queremos exactamente, sin tener que forzarnos a recibir información extra  cuando reutilizamos APIs para distintos objese tivos.
