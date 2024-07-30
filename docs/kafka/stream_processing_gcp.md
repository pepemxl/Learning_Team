# Practica de kafka en GCP

En esta practica crearemos un streaming data pipeline con Kafka, con lo cual nos habituaremos al uso de Kafka Streams API.


Correremos una aplicacion JAVA que usa una libreria Kafka Streams mostrando un simple caso e2e data pipeline.



- Empezar un cluster de Kafka usando una sola maquina
- Escribir un ejemplo `input` data a un topic de kafka, usando la producer consola.
- Procesaremos el input de kafka con una aplicación JAVA que llamaremos `WordCount` que usa la libreria Kafka Streams(viene incluido usualmente en los ejemplos de kafka `streams/examples/src/main/java/org/apache/kafka/streams/examples/wordcount/WordCountDemo.java`).
- Inpexccionaremos las salidas de esta aplicacion usando la consola consumer.



## Setup y requirimientos

- Recuerda hacer las practicas en una ventana igcognito para evitar desloguear tu cuenta o perder accesos.
- No uses tu cuenta personal o te cobraran!

1. Haz click en el button para abrir la google cloud console
    - user: `Username`
    - password: `Password`
2. Continua:
    - Acepta terminos y condiciones
    - No agregues ningún multifactor authentication
    - No hahas singg up a ninguna otra cosa

## Task 1

1. En la cloud console abre el menu de navegación y haz click en Marketplace.
2. Localiza Apache Kafka deployment(Apache Kafka Server on Ubuntu Server 20.04)
    - Haz click en get started
    - Acepta terminos y condiciones
    - Acepta
3. Haz click en deploy
4. Bajo la pagina New Apache Kafka Server on Ubuntu Server 20.04 deployment
    - Selecciona `Deployment Service Account` como `New account` y entra a `Service account name` como `apache-kafka`
5. Selecciona una zona `ZONE`
6. Bajo `Machine Type` cambia a Series E2 y selecciona `e2-medium`.
7. Deja el resto de valoes por defecto
    - Acepta terminos
    - Hasz click en `Deploy`


```java
// Serializers/deserializers (serde) for String and Long types
final Serde<String> stringSerde = Serdes.String();
final Serde<Long> longSerde = Serdes.Long();

// Construct a `KStream` from the input topic "streams-plaintext-input", where message values
// represent lines of text (for the sake of this example, we ignore whatever may be stored
// in the message keys).
KStream<String, String> textLines = builder.stream("streams-plaintext-input", Consumed.with(stringSerde, stringSerde));

KTable<String, Long> wordCounts = textLines
    // Split each text line, by whitespace, into words.  The text lines are the message
    // values, i.e. we can ignore whatever data is in the message keys and thus invoke
    // `flatMapValues` instead of the more generic `flatMap`.
    .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
    // We use `groupBy` to ensure the words are available as message keys
    .groupBy((key, value) -> value)
    // Count the occurrences of each word (message key).
    .count();

// Convert the `KTable<String, Long>` into a `KStream<String, Long>` and write to the output topic.
wordCounts.toStream().to("streams-wordcount-output", Produced.with(stringSerde, longSerde));
```


### Inicia un ambiente de Kafka

1. En la consola abre un menu de navegación y selecciona `Compute Engine > VM Instances`
2. Junto al nombre de la VM `kafka-1-vm` haz click en el boton `SSH` para conectarnos a la VM de Kafka.
3. Primero ve al path de instalación de kafka.
    - `cd /opt/kafka/`
4. Inicia el servicio de zookeper
    - `sudo bin/zookeeper-server-start.sh config/zookeeper.properties`
5. Abre otra instanacia SSH

### Inicia un broker de Kafka

- Inicia un broker de kafka.
```bash
cd /opt/kafka/
sudo bin/kafka-server-start.sh config/server.properties
```

- Abre otra instancia SSH(3ra).

## Task 2 Prepara los topics y la entrada de datos.

1. ve a `cd /opt/kafka/`
2. Crea un topic `streams-plaintext-input`:
```bash
sudo bin/kafka-topics.sh --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic streams-plaintext-input
```
3. Crea el output topic:
```bash
sudo bin/kafka-topics.sh --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic streams-wordcount-output
```
4. Ahora genera datos de entrada y guardalos en `/tmp/file-input.txt`
```bash
echo -e "En la parte más alta de la ciudad, sobre una columnita, se alzaba la estatua del Príncipe Feliz.\n Estaba toda revestida de madreselva de oro fino. Tenía, a guisa de ojos, dos centelleantes zafiros y un gran rubí rojo ardía en el puño de su espada." > /tmp/file-input.txt
```
5. Envia los datos al topic
```bash
cat /tmp/file-input.txt | sudo bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic streams-plaintext-input
```
En la practica los datos llegan en paralelo y de muchos distintos origenes.


## Task 3 Procesa la data de entrada con Kafka Streams

```bash
sudo bin/kafka-run-class.sh org.apache.kafka.streams.examples.wordcount.WordCountDemo
```

## Task 4 Inspecciona la salida

1. En la pagina VM-instances haz click en el boton `SSH` para iniciar una nueva conexión.
2. Consume del topic `streams-wordcount-output`:
```bash
cd /opt/kafka
sudo bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
    --topic streams-wordcount-output \
    --from-beginning \
    --formatter kafka.tools.DefaultMessageFormatter \
    --property print.key=true \
    --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
    --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer
```

## Task 5 Para el cluster de Kafka

1. Para el broker con `Ctrl+C` o `kill` el proceso del broker.
2. Para la instancia de zooleper con `Ctrl+C` o `kill` el proceso de zookeeper.
3. Para la instancia que corre la aplicación/clase de java.
