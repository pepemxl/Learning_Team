# Event Driven Development

**Event-Driven Design** (o más comúnmente **Event-Driven Architecture – EDA**) es un paradigma de diseño de software donde los componentes del sistema se comunican y reaccionan principalmente a través de **eventos** en lugar de llamadas directas síncronas (request-response).

En vez de que un servicio llame directamente a otro y espere respuesta, un componente **produce un evento** (algo importante ocurrió) y otros componentes **lo consumen** de forma asíncrona cuando les interesa.

### ¿Qué es un "evento" en este contexto?

Un evento es un **registro inmutable** que representa un hecho significativo que ocurrió en el pasado.  
Ejemplos muy típicos (2025–2026):

- `OrderPlaced`
- `PaymentProcessed`
- `UserRegistered`
- `InventoryUpdated`
- `ShipmentDelivered`
- `TemperatureExceededThreshold`
- `FraudDetected`

Características clave de un buen evento:

- **Nombre en pasado** (indicativo de que ya ocurrió)
- **Inmutable** (nunca se modifica después de creado)
- **Contiene datos suficientes** para que los consumidores tomen decisiones sin preguntar de vuelta al productor

### Componentes principales de una arquitectura Event-Driven

| Componente          | Rol principal                                      | Ejemplos tecnológicos comunes (2025–2026)          |
|---------------------|----------------------------------------------------|-----------------------------------------------------|
| Event Producer      | Genera y publica eventos                           | Microservicio, IoT device, frontend action          |
| Event Router / Broker | Recibe, filtra, enruta y almacena eventos         | Kafka, RabbitMQ, AWS EventBridge, Google Pub/Sub, Redis Streams, Pulsar |
| Event Consumer      | Escucha eventos y reacciona                        | Microservicio, función serverless, workflow engine  |
| Event Store (opcional) | Guarda secuencia de eventos para replay / auditoría | Kafka (como log), EventStoreDB, AWS Kinesis         |

### Comparación: EDA vs enfoques tradicionales

| Característica              | Request-Response (REST/gRPC síncrono) | Event-Driven (EDA)                          |
|-----------------------------|----------------------------------------|---------------------------------------------|
| Acoplamiento                | Alto (conocen endpoints y contratos)   | Muy bajo (solo conocen el formato del evento) |
| Comunicación                | Síncrona                               | Asíncrona                                   |
| Tolerancia a fallos         | Si falla el receptor → falla la llamada | El productor sigue funcionando              |
| Escalabilidad horizontal    | Difícil (cargas acopladas)             | Muy buena (consumidores independientes)     |
| Reacción en tiempo real     | Limitada                               | Nativa                                      |
| Complejidad operativa       | Media                                  | Alta (observabilidad, idempotencia, ordering) |
| Casos ideales               | Operaciones transaccionales simples    | Sistemas reactivos, alta concurrencia, IoT, workflows largos |

### Patrones más importantes en Event-Driven Design (2025–2026)

1. **Publish-Subscribe (Pub/Sub)**  
   → Un evento puede tener múltiples consumidores independientes

2. **Event Notification**  
   → "Oye, pasó algo" (el consumidor decide qué hacer)

3. **Event-Carried State Transfer**  
   → El evento lleva todo el estado necesario (evita consultas posteriores)

4. **Choreography**  
   → Cada servicio reacciona a eventos sin orquestador central (muy común en microservicios)

5. **Event Sourcing**  
   → El estado se reconstruye reproduciendo la secuencia de eventos

6. **CQRS + Event Sourcing**  
   → Lecturas y escrituras separadas, estado derivado de eventos

7. **Saga (Coreografiada)**  
   → Workflow distribuido coordinado mediante eventos (sin orquestador central)

### EDA y DDD – Combinación muy poderosa (muy usada en 2025–2026)

- **DDD táctico/estratégico** → te ayuda a descubrir **qué eventos son importantes** para el negocio (Domain Events)
- **Bounded Contexts** → cada contexto publica sus propios eventos con su propio modelo
- **Context Mapping** → los eventos actúan como **Published Language** entre contextos
- Los **Domain Events** son la principal forma de comunicación entre bounded contexts

### Cuándo SÍ vale la pena usar Event-Driven Design

- Necesitas **alta disponibilidad** y **resiliencia** (un servicio caído no para todo)
- Tienes **flujos asíncronos largos** (pedido → pago → preparación → envío → entrega)
- Procesamiento de **grandes volúmenes** en tiempo real (IoT, finanzas, e-commerce peak)
- Quieres **desacoplar equipos** al máximo (microservicios muy independientes)
- Buscas **extensibilidad** (fácil agregar nuevos consumidores sin tocar productores)

### Cuándo NO (o con mucho cuidado)

- Operaciones que necesitan **transaccionalidad fuerte inmediata** (dinero moviéndose)
- Dominios muy simples / CRUD básico
- Equipos con poca experiencia en sistemas distribuidos
- Sistemas donde la latencia de eventual consistency sea inaceptable




