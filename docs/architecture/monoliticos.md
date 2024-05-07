# Arquitectura Monolítica

El estilo arquitectónico monolítico consiste en crear una aplicación autosuficiente que contenga absolutamente toda la funcionalidad necesaria para realizar la tarea para la cual fue diseñada, sin contar con dependencias externas que complementen su funcionalidad. En este sentido, sus componentes trabajan juntos, compartiendo los mismos recursos y memoria. En pocas palabras, una aplicación monolítica es una unidad cohesiva de código.


Un monolítico podrías estar construido como una sola unidad de software o creada a partir de varios módulo o librerías, pero lo que la distingue es que al momento de compilarse se empaqueta como una solo pieza, de tal forma que todos los módulos y librerías se empaquetarán junto con la aplicación principal.

El estilo monolítico no es algo que haya sido planeado o ideado por alguien en particular, si no que todas las aplicaciones al inicio de la computación nacían con este estilo arquitectónico. Solo hace falta recordar los sistemas antiguos, donde todo funcionaba en una súper computadora, la cual realizaba todas las tareas. Recordemos que al inicio no existían el internet, por lo que no había forma de consumir servicios externos para realizar determinadas tareas, en su lugar, el sistema monolítico tenía que implementar absolutamente toda la funcionalidad necesaria para funcionar, y de esta forma ser auto suficiente.


## Características de un Monolítico

Las características se pueden convertir en ventajas o desventajas solo cuando analizamos la problemática que vamos a resolver, mientras tanto, son solo características:

- Son aplicaciones autosuficientes (no requieren de nada para funcionar).
- Realizan de punta a punta todas las operaciones para terminar una tarea.
- Son por lo general aplicaciones grandes, un que no es un requisito.
- Son por lo general silos de datos privados, es decir, cada instalación administra si propia base de datos.
- Todo el sistema corre sobre una solo plataforma.

### Ventajas
- Fácil de desarrollar: Debido a que solo existe un componente, es muy fácil para un equipo pequeño de desarrollo iniciar un nuevo proyecto y ponerlo en producción rápidamente.
- Fácil de escalar: Solo es necesario instalar la aplicación en varios servidores y ponerlo detrás de un balanceador de cargar.
- Pocos puntos de fallo: El hecho de no depender de nadie más, mitiga gran parte de los errores de comunicación, red, integraciones, etc. Prácticamente los errores que pueden salir son por algún bug del programador, pero no por factores ajenos.
- Autónomo: Las aplicaciones Monolíticas se caracterizan por ser totalmente autónomas (auto suficientes), lo que les permite funcionar independientemente del resto de aplicaciones.
- Performance: Las aplicaciones Monolíticas son significativamente más rápidas debido que todo el procesamiento lo realizan localmente y no requieren consumir procesos distribuidos para completar una tarea.
- Fácil de probar: Debido a que es una sola unidad de código, toda la funcionalidad está disponible desde el inicio de la aplicación, por lo que es posible realizar todas las pruebas necesarias sin depender de nada más.

## desventajas
- Anclado a un Stack tecnológico: Debido a que todo el software es una sola pieza, implica que utilicemos el mismo Stack tecnológico para absolutamente todo, lo que impide que aprovechemos todas las tecnologías disponibles.
- Escalado Monolítico: Escalar una aplicación Monolítica implica escalar absolutamente toda la aplicación, gastando recursos para funcionalidad que quizás no necesita ser escalada (en el estilo de Microservicios analizaremos como solucionar esto).
- El tamaño:  las aplicaciones Monolíticas son fácil de operar con equipo pequeños, pero a medida que la aplicación crece y con ello el equipo de desarrollo, se vuelve cada vez más complicado dividir el trabajo sin afectar funcionalidad que otro miembro del equipo también está moviendo.
- Versión tras versión: Cualquier mínimo cambio en la aplicación implicará realizar una compilación del todo el artefacto y con ello una nueva versión que tendrá que ser administrada.
- Si falla, falla todo: A menos que tengamos alta disponibilidad, si la aplicación Monolítica falla, falla todo el sistema, quedando totalmente inoperable.
- Es fácil perder el rumbo: Por la naturaleza de tener todo en un mismo módulo es fácil caer en malas prácticas de programación, separación de responsabilidades y organización de las clases del código.
- Puede ser abrumador: En proyectos muy grandes, puede ser abrumador para un nuevo programador hacer un cambio en el sistema.





# Migración a Microservicios?

## Problemas de la migración a microservicios
- Performance: La serialización de data y el envio a traves de la red provoca un overhead el cual se convierte en un cuello de botella.
- Correctness: La consistencia e interacción entre las versiones de cada servicio desplegado se vuelve un problema ( más aun para esos sistemas creados estrictamente con paradigmas funcionales)
- Management: En lugar de mantener un solo flujo para el build del binario, pruebas y desplegado ahora debemos manejar decenas junto con calendarios de liberación.
- Freeze APIs: Una vez desplegada una API el proceso para cambiar cualquier comportamiento de la API se vuelve complicado debido a que se establecen contratos entre el servicio y los clientes, al modificar el servicio se rompe el funcionamiento de los clientes.


# Alternativas

Hay algunas recomendaciones:
- Monolithic applications: Cuando se creen aplicaciones dentro del monolito, hacerlo de manera modular en sus distintos componentes logicos. Un componente es un agente de larga duración, similar a un [actor](https://en.wikipedia.org/wiki/Actor_model).
- 









## Referencias:
- Actor Model [https://en.wikipedia.org/wiki/Actor_model](https://en.wikipedia.org/wiki/Actor_model)
- Actor Model [https://www.codeproject.com/articles/481168/using-the-actor-programming-model](https://www.codeproject.com/articles/481168/using-the-actor-programming-model)


