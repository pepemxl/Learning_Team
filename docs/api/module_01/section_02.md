# Diseño de API bajo la arquitectura de microservicios

## Qué debemos cuidar?

- Descomposición eficaz de servicios
- Pruebas de integración de microservicios
- Gestión de la indisponibilidad de servicios
- Rastreo de transacciones distribuidas
- Mayor complejidad operativa y sobrecarga de infraestructura

### Descomposición eficaz de servicios

Uno de los desafíos más importantes al diseñar microservicios es la descomposición de servicios. Debemos descomponer una plataforma en componentes débilmente acoplados, pero suficientemente independientes, con límites claramente definidos. 

Se puede detectar un acoplamiento irrazonable entre los servicios si se observa que se cambia un servicio cada vez que se cambia otro. En tales situaciones, el contrato entre servicios no es resiliente o existen suficientes dependencias entre ambos componentes como para justificar su fusión. 

No descomponer un sistema en microservicios independientes puede resultar en lo queusualmente llamamos **monolito**, una situación en la que se combinan todos los problemas de las arquitecturas monolíticas con todos los problemas de los microservicios, sin disfrutar de los beneficios de ninguno de ellos.



## Pruebas de integración de microservicios


Usualmente los microservicios suelen ser más fáciles de probar y que sus conjuntos de pruebas suelen ejecutarse más rápido. 

Las pruebas de integración de microservicios pueden ser significativamente más difíciles de ejecutar, especialmente cuando una sola transacción implica la colaboración entre varios microservicios. Cuando toda la aplicación se ejecuta dentro del mismo proceso, es bastante fácil probar la integración entre diferentes componentes, y la mayoría de las veces solo requerirá pruebas unitarias bien escritas. 

En un contexto de microservicios, para probar la integración entre múltiples servicios, es necesario poder ejecutarlos todos con una configuración similar a la de su entorno de producción.

Siempre debe asegurarse de que el cliente de la API la consuma exactamente como lo indica la documentación. Así que debemos escribir pruebas unitarias para el cliente de la API usando la documentación de la API para generar respuestas simuladas del servicio. 

Siempre es necesario hacer pruebas e2e.

## Gestión de la indisponibilidad de servicios

Debemos asegurarnos de que nuestras aplicaciones sean resilientes ante la indisponibilidad del servicio, tiempos de espera de conexión y solicitud, solicitudes con errores, etc.

Por ejemplo, al realizar un pedido a través de una aplicación de entrega de comida a domicilio,se despliega una cadena de solicitudes entre servicios para procesarlo y entregarlo, y cualquiera de estas solicitudes puede fallar en cualquier momento. 

- Un cliente realiza un pedido y lo paga. 
    - El pedido se realiza mediante el servicio de pedidos, y para procesar el pago, este trabaja en conjunto con el servicio de pagos.
        - Si el pago se realiza correctamente, el servicio de pedidos solicita al servicio de cocina que programe la producción del pedido.
            - Una vez producido el pedido, el servicio de cocina solicita al servicio de reparto que programe la entrega.

En esta compleja cadena de solicitudes, si uno de los servicios involucrados no responde como se espera, puede desencadenar un error en cascada en la plataforma que deja el pedido sin procesar o en un estado inconsistente. Por esta razón, es importante diseñar microservicios que puedan gestionar de forma fiable los endpoints fallidos. Nuestras pruebas integrales deben considerar estos escenarios y evaluar el comportamiento de nuestros servicios en ellas.

## Rastreo de transacciones distribuidas

Los servicios colaboradores a veces deben gestionar transacciones distribuidas. Estas transacciones requieren la colaboración de dos o más servicios. Por ejemplo, en una aplicación de reparto de comida, queremos controlar el stock de ingredientes para que nuestro catálogo refleje con precisión la disponibilidad del producto. Cuando un usuario realiza un pedido, queremos actualizar el stock de ingredientes para que refleje la nueva disponibilidad. En concreto, queremos actualizar el stock de ingredientes una vez que el pago se haya procesado correctamente. El procesamiento correcto de un pedido implica las siguientes acciones:

1. Procesar el pago.
2. Si el pago se realiza correctamente, actualizar el estado del pedido para indicar que está en curso.
3. Interactuar con el servicio de cocina para programar la producción del pedido.
4. Actualizar el stock de ingredientes para que refleje su disponibilidad actual.

Todas estas operaciones están relacionadas y deben orquestarse para que tengan éxito o fracasen conjuntamente. No podemos pagar un pedido correctamente sin actualizar correctamente su estado, y no deberíamos programar su producción si el pago falla. Quizás queramos actualizar la disponibilidad de los ingredientes al momento de realizar el pedido y, si el pago falla posteriormente, asegurarnos de revertir la actualización. Si todas estas acciones ocurren dentro del mismo proceso, gestionar el flujo es sencillo, pero con los microservicios debemos gestionar los resultados de varios procesos. Al usar microservicios, el desafío es **garantizar un proceso de comunicación sólido entre los servicios para saber exactamente qué tipo de error ocurre y tomar las medidas adecuadas en respuesta a él**. 

En el caso de los servicios que trabajan en colaboración para atender ciertas solicitudes, también es necesario poder rastrear el ciclo de la solicitud a medida que pasa por los diferentes servicios para poder detectar errores durante la transacción. Para obtener visibilidad de las transacciones distribuidas, se deberá configurar el registro y el seguimiento distribuidos entre los microservicios.


## A mayor complejidad operativa mayor la sobrecarga de infraestructura


