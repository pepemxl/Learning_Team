# Analisis de Dominio para desarrollo de API

En nuestra API tenemos varios componentes

Debemos responder las siguientes preguntas:

1. ¿Quiénes son los participantes?
2. ¿Son recursos externos o internos? 
3. ¿Qué soluciones/recursos de API desean los clientes obtener con la API? 
4. ¿Qué otras soluciones de API o recursos serán utilizados por esta API?
5. ¿Qué datos u objetos de dominio usará el cliente?


Dividiremos las actividades en pasos o descripciones de uso:
- Un recurso dependiente no puede existir sin otro.
    - Por ejemplo, la asociación entre un podcast y su consumidor no se puede determinar a menos que se creen el podcast y su consumidor.
- Un recurso independiente puede existir sin otro.
    - Por ejemplo, un recurso de podcast puede existir sin ninguna dependencia.
- ​​Un recurso asociativo existe de forma independiente, pero mantiene algún tipo de relación, es decir, puede estar conectado por referencia.



