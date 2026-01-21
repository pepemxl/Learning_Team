# Domain Driven Design

**Domain-Driven Design (DDD)** es una filosofía y conjunto de patrones para el diseño de software que pone el **dominio del negocio** en el centro absoluto del desarrollo.

Fue introducido formalmente por **Eric Evans** en su famoso libro "Domain-Driven Design: Tackling Complexity in the Heart of Software".

"El diseño del software debe estar profundamente alineado con el modelo del dominio del negocio y evolucionar junto con el entendimiento que tiene el equipo del negocio"

## Principios fundamentales de DDD

| Principio | En palabras simples | Por qué importa mucho? |
|---|---|---|
| Ubiquitous Language      | Todos (desarrolladores + expertos de negocio) hablan el mismo idioma exacto | Evita malentendidos caros y pérdida de significado |
| Domain Model             | El software refleja un modelo conceptual del negocio real | El código expresa el negocio, no solo "guarda datos" |
| Focus on the Core Domain | Identificar y poner máximo esfuerzo en la parte que realmente da ventaja competitiva| Recursos limitados → maximizar impacto             |
| Model-Driven Design      | El diseño técnico está subordinado al modelo del dominio | El modelo dicta la arquitectura, no al revés       |
| Bounded Context          | Cada modelo tiene un límite claro donde es válido | Soluciona el problema del "modelo grande y único" |
| Context Mapping          | Definir explícitamente las relaciones entre diferentes contextos delimitados | Evita el caos en sistemas grandes/distribuidos     |

El lenguaje ubicuo se refiere al lenguaje que usan en cada departamento o empresa(idealmente), usualmente le llamamos el "jargon", desde ahi sabemo que tan solo comunicarse podria volverse un problema. Hablaremos de los demas terminos en las siguientes secciones.


## Las dos grandes divisiones del DDD (2025)

Hoy en día se suele hablar de dos niveles de DDD:

1. **DDD Táctica** (más común)
   - Building blocks técnicos del modelado
   - Entity, Value Object, Aggregate, Aggregate Root, Repository, Domain Service, Domain Event, Application Service, Factory, etc.

2. **DDD Estratégico** (el que realmente marca la diferencia en sistemas grandes)
   - Bounded Context
   - Context Mapping patterns (Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language…)
   - Core Domain, Supporting Subdomain, Generic Subdomain
   - Distinción entre Core, Supporting y Generic

## Comparación DDD vs otros enfoques


|Característica              | Enfoque tradicional               | DDD bien aplicado |
| --- | --- | --- |
|Modelo | Básicamente tablas + CRUD | Modelo rico del negocio |
|Lugar del negocio | En servicios/casos de uso | En entidades + agregados |
|Validación | En capas superiores o UI | En el propio modelo del dominio|
|Lenguaje | Técnico + algo de negocio | Ubiquitous Language compartida |
|Escalabilidad conceptual | Se rompe con la complejidad | Soporta mejor la complejidad creciente|
|Tamaño ideal del proyecto | Pequeño-mediano simple | Mediano-grande-complejo|


## Jerarquía aproximada de cuándo vale la pena usar cada nivel de DDD (2025)

|Nivel de complejidad del dominio | Recomendación actual |
| --- | --- |
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
Simple-medio          | Táctico ligero (Value Objects + Entities + pequeños Aggregates) |
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
Medio                 | Táctico completo + algunos conceptos estratégicos |
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
Medio-alto            | DDD táctico fuerte + estratégico importante
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
| Alto-muy alto (core business) |DDD estratégico + táctico profundo + Ubiquitous Language muy cuidada |
| Muy simple (CRUD puro) | Casi nunca vale la pena DDD completo |
Dominio extremadamente complejo | DDD estratégico muy maduro + múltiples Bounded Contexts + Context Mapping sofisticado |


## Fases Recomendadas

- **DDD Táctico básico**: "Poner lógica de negocio dentro de objetos ricos en vez de servicios anémicos"
- **DDD Táctico completo**: "Modelar con Aggregates, mantener invariantes y usar Domain Events"
- **DDD Estratégico**: "Dividir el sistema en Bounded Contexts con modelos diferentes y relaciones explícitas entre ellos"
- **DDD full maduro**: "Todo lo anterior + lenguaje ubicuo muy fuerte + foco obsesivo en el Core Domain + evolución continua del modelo"

