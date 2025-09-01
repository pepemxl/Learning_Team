# OpenAPI


Vamos a desglosar los elementos que veremnos en un archivo yaml de OpenAPI



```yaml title="Versión de OpenAPI" linenums="1"
openapi: 3.0.3
```

```yaml title="Metadata de la API" linenums="2"
info:
  title: UserAccount API
  description: For users
  version: 1.0.0
```

```yaml title="Tags para agrupar operaciones" linenums="6"
tags:
  - name User
    description: User relatted operations
```

```yaml title="Lugar donde la API es servida" linenums="9"
servers:
    - url https://example.com
```

```yaml title="URLs y metodos" linenums="11"
paths:
    /users/{id}: 
      put:
        summary: Modify user
```

```yaml title="Descripción soporta Markdown" linenums="15"
        description: |
          Modify the user and return `updated`

          **Needs Authentication**
```

```yaml linenums="19"
          operationId: modifyUser
          tags:
          - User
```

```yaml title="Lista de tipos requeridos para seguridad" linenums="22"
          security:
          - V0Tokens []
```

```yaml title="Parámetros para la URL" linenums="24"
          parameters:
          - name id
            in: path
            required: true
            schema:
              type: string
```

```yaml title="Parámetros Query" linenums="30"
          - name: role
            in: query
            schema:
              type: string
              enum:
              - admin
              - member
              default: member
```

```yaml title="Body del Request" linenums="38"
          requestBody:
            content:
              application/json:
                schema:
                  oneOf:
                  - $ref: '#/components/schemas/Employee'
                  - $ref: '#/components/schemas/Customer'
```


```yaml title="Responses" linenums="45"
          responses:
            '200':
              description: Updated User
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/User'
            '201': 
              ...
```



