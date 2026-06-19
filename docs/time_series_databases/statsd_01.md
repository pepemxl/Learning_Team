# Statsd

StatsD es un daemon(demonio😈) de red basado en Node.js que recopila, agrega y distribuye métricas. Ofrece una forma sencilla de monitorizar las métricas de las aplicaciones en tiempo real mediante la recepción de estadísticas a través de UDP o TCP y el envío de datos agregados a sistemas de almacenamiento backend como [Graphite](http://graphite.readthedocs.org/).

StatsD está diseñado para recopilar y procesar métricas de diversas fuentes de forma eficiente, lo que facilita la instrumentación del código de la aplicación. El sistema utiliza un modelo cliente-servidor: las aplicaciones envían métricas a StatsD mediante un protocolo de texto simple. StatsD las agrega y las transfiere a servicios backend configurables.

## Características clave

- Recopilación de diversos tipos de métricas (contadores, temporizadores, indicadores, conjuntos)
- Agregación de métricas para reducir la carga en los sistemas backend
- Compatibilidad con múltiples sistemas de almacenamiento backend
- Compatibilidad con transporte UDP y TCP para minimizar el impacto en el rendimiento de la aplicación
- Intervalos de descarga y frecuencias de muestreo configurables
- Arquitectura de plugins extensible para backends y servidores


## Conceptos basicos

### Tipos de métricas

StatsD admite cuatro tipos principales de métricas:

1. Contadores: Contadores simples que registran cuantas veces ocurre un evento
2. Temporizadores: Registran la duración de las operaciones
3. Indicadores: Registre un valor que puede aumentar o disminuir con el tiempo
4. Conjuntos: Cuentan las ocurrencias únicas de eventos

### Buckets

Cada estadística se almacena en su propio "bucket", un espacio de nombres para una métrica específica. Los buckets pueden nombrarse con cualquier cadena que se traduzca correctamente al sistema de almacenamiento del backend (por ejemplo, los puntos en los nombres crean jerarquías de carpetas en Graphite).

### Intervalo de tiempo para el Flush (Vaciado de buffer)

Despues de un intervalo de tiempo para el flush, el cual es configurable (default: 10 segundos), StatsD agrega todas las métricas recopiladas y las envía a los servicios del backend configurados. Este método de procesamiento por lotes reduce la carga en los sistemas del backend.


## Componentes principales

### Componentes del servidor

StatsD admite múltiples protocolos de transporte para recibir métricas:

1. Servidor UDP: Servidor predeterminado con baja sobrecarga para aplicaciones de alto rendimiento
2. Servidor TCP: Alternativa para un transporte fiable con mayor sobrecarga
3. Socket Unix: Opción de comunicación local

Los componentes del servidor analizan los paquetes entrantes y validan las métricas antes de pasarlas al procesamiento principal.

### Procesamiento principal

El componente principal es stats.js, que:

- Administra los grupos de métricas para diferentes tipos de métricas
- Procesa las métricas entrantes de los componentes del servidor
- Agrega las métricas según su tipo durante el intervalo de vaciado
- Emite eventos para que los módulos del backend procesen los datos agregados


## Sistema backend

Los backends reciben métricas agregadas del core y las formatean y transmiten a sistemas externos:

- Graphite envía métricas a un servidor Graphite mediante el protocolo de texto o Pickle
- Consola envía métricas a la salida estándar para su depuración
- Repetidor reenvía métricas a otras instancias de StatsD
- Backends personalizados definidos por el usuario para la integración con otros sistemas


## Protocolo y uso del cliente

StatsD utiliza un protocolo de texto simple para recibir métricas. El formato básico es:

```bash title="Formato de las métricas"
<nombre de métrica>:<valor>|<tipo>
```

Donde:

- `<nombre de métrica>` es el nombre del depósito
- `<valor>` suele ser un entero
- `<tipo>` indica el tipo de métrica (c=contador, ms=temporizador, g=indicador, s=conjunto)

Ejemplo de envío de una métrica de contador mediante la línea de comandos:

`echo "foo:1|c" | nc -u -w0 127.0.0.1 8125`

Existen varias bibliotecas de cliente disponibles para diferentes lenguajes de programación para facilitar la instrumentación.

## Opciones de implementación

StatsD se puede implementar de varias maneras:

- Docker: Imágenes oficiales de contenedor disponibles en GitHub Container Registry y DockerHub
- Instalación manual: Clonar el repositorio y ejecutar con Node.js
- Paquete Debian: Integración del sistema con el servicio SystemD
- Paquete NPM: Instalación mediante el gestor de paquetes Node.js

Para todos los métodos de implementación, se requiere un archivo de configuración basado en exampleConfig.js.


## Características adicionales

### Proxy de clúster

Para escalar StatsD en múltiples instancias, la función de proxy de clúster distribuye métricas basándose en un hash consistente y realiza comprobaciones de estado.

### Interfaz de administración

Una interfaz TCP para la supervisión y gestión en tiempo de ejecución de la instancia de StatsD, que proporciona acceso a las métricas y la configuración.

### Capacidades de depuración

StatsD incluye opciones de depuración para registrar excepciones e imprimir información de diagnóstico sobre los mensajes entrantes.







