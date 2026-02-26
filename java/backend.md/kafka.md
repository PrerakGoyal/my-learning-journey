# 5. Explore Apache Kafka

## Overview
Apache Kafka is a distributed, fault-tolerant event streaming platform designed for high-throughput, real-time data pipelines and event-driven architectures. It acts as a durable, ordered log of events.

---

## Core Concepts

| Term              | Description                                                              |
|-------------------|--------------------------------------------------------------------------|
| Event / Message   | A key-value record representing something that happened                  |
| Topic             | Named category/feed to which events are published                        |
| Partition         | Ordered, immutable log within a topic (enables parallelism)              |
| Producer          | Application that publishes events to a topic                             |
| Consumer          | Application that reads events from a topic                               |
| Consumer Group    | Set of consumers sharing work across partitions                          |
| Broker            | Kafka server node that stores and serves data                            |
| Cluster           | Multiple brokers working together                                        |
| Offset            | Position of a message within a partition                                 |
| Zookeeper / KRaft | Cluster coordination (KRaft replaces ZooKeeper in modern Kafka)          |

---

## Architecture Diagram

```
Producers                 Kafka Cluster                  Consumers
---------                 ----------------               ----------
[Service A] ─────────►  [Topic: orders]   ──────────►  [Consumer Group A]
[Service B] ─────────►  ├─ Partition 0                  [Consumer Group B]
[Service C] ─────────►  ├─ Partition 1
                         └─ Partition 2
                         
                         [Topic: payments]
                         └─ Partition 0
```

---

## Quick Start with Docker

```yaml
# docker-compose.yml
version: '3.8'
services:
  kafka:
    image: confluentinc/cp-kafka:7.6.0
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      CLUSTER_ID: MkU3OEVBNTcwNTJENDM2Qk

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: kafka-ui
    ports:
      - "8090:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9092
```

```bash
docker compose up -d
# Access UI at http://localhost:8090
```

---

## Spring Boot + Kafka Setup

### Dependency
```xml
<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
```

### `application.yml`
```yaml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.springframework.kafka.support.serializer.JsonSerializer
      acks: all                     # Wait for all replicas to acknowledge
      retries: 3
    consumer:
      group-id: order-consumer-group
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.springframework.kafka.support.serializer.JsonDeserializer
      auto-offset-reset: earliest   # earliest | latest
      properties:
        spring.json.trusted.packages: "com.example.events"
```

---

## Producer

### Configuration
```java
@Configuration
public class KafkaProducerConfig {

    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        config.put(ProducerConfig.ACKS_CONFIG, "all");
        config.put(ProducerConfig.RETRIES_CONFIG, 3);
        return new DefaultKafkaProducerFactory<>(config);
    }

    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}
```

### Event Class
```java
public class OrderEvent {
    private String orderId;
    private String customerId;
    private double amount;
    private String status;
    private LocalDateTime timestamp;
    // Constructors, Getters, Setters
}
```

### Producer Service
```java
@Service
public class OrderProducer {

    private static final String TOPIC = "orders";

    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;

    public void publishOrder(OrderEvent event) {
        // Key = orderId ensures messages for same order go to same partition
        kafkaTemplate.send(TOPIC, event.getOrderId(), event)
            .whenComplete((result, ex) -> {
                if (ex == null) {
                    System.out.printf("Sent order %s to partition %d, offset %d%n",
                        event.getOrderId(),
                        result.getRecordMetadata().partition(),
                        result.getRecordMetadata().offset());
                } else {
                    System.err.println("Failed to send: " + ex.getMessage());
                }
            });
    }

    // Send to specific partition
    public void publishToPartition(OrderEvent event, int partition) {
        kafkaTemplate.send(TOPIC, partition, event.getOrderId(), event);
    }
}
```

---

## Consumer

### Configuration
```java
@Configuration
@EnableKafka
public class KafkaConsumerConfig {

    @Bean
    public ConsumerFactory<String, OrderEvent> consumerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "order-consumer-group");
        config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
        config.put(JsonDeserializer.TRUSTED_PACKAGES, "com.example.events");
        return new DefaultKafkaConsumerFactory<>(config,
                new StringDeserializer(),
                new JsonDeserializer<>(OrderEvent.class));
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, OrderEvent> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, OrderEvent> factory =
                new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(3);  // 3 consumer threads
        return factory;
    }
}
```

### Consumer Service
```java
@Service
public class OrderConsumer {

    // Basic listener
    @KafkaListener(topics = "orders", groupId = "order-consumer-group")
    public void consumeOrder(OrderEvent event) {
        System.out.println("Received order: " + event.getOrderId());
        // Process order...
    }

    // Listener with metadata
    @KafkaListener(topics = "orders", groupId = "notification-group")
    public void consumeWithMetadata(
            @Payload OrderEvent event,
            @Header(KafkaHeaders.RECEIVED_PARTITION) int partition,
            @Header(KafkaHeaders.OFFSET) long offset) {
        System.out.printf("Partition: %d | Offset: %d | Order: %s%n",
                partition, offset, event.getOrderId());
    }

    // Batch listener
    @KafkaListener(topics = "orders", groupId = "batch-group",
                   containerFactory = "batchFactory")
    public void consumeBatch(List<OrderEvent> events) {
        System.out.println("Processing batch of: " + events.size());
    }
}
```

---

## Topic Management

### Programmatic Topic Creation
```java
@Configuration
public class KafkaTopicConfig {

    @Bean
    public NewTopic ordersTopic() {
        return TopicBuilder.name("orders")
                .partitions(3)
                .replicas(1)
                .config(TopicConfig.RETENTION_MS_CONFIG, "604800000") // 7 days
                .build();
    }

    @Bean
    public NewTopic paymentsTopic() {
        return TopicBuilder.name("payments")
                .partitions(3)
                .replicas(1)
                .build();
    }
}
```

### CLI Commands
```bash
# List topics
docker exec kafka kafka-topics --bootstrap-server localhost:9092 --list

# Create topic
docker exec kafka kafka-topics --bootstrap-server localhost:9092 \
  --create --topic orders --partitions 3 --replication-factor 1

# Describe topic
docker exec kafka kafka-topics --bootstrap-server localhost:9092 \
  --describe --topic orders

# Produce messages (testing)
docker exec -it kafka kafka-console-producer \
  --bootstrap-server localhost:9092 --topic orders

# Consume messages (testing)
docker exec -it kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 --topic orders --from-beginning
```

---

## Error Handling & Dead Letter Topic (DLT)

```java
@Configuration
public class KafkaErrorConfig {

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, OrderEvent> retryableFactory(
            ConsumerFactory<String, OrderEvent> cf,
            KafkaTemplate<String, Object> template) {

        ConcurrentKafkaListenerContainerFactory<String, OrderEvent> factory =
                new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(cf);

        // Retry 3 times, then send to DLT
        DefaultErrorHandler errorHandler = new DefaultErrorHandler(
                new DeadLetterPublishingRecoverer(template),
                new FixedBackOff(2000L, 3)  // 2s delay, 3 attempts
        );
        factory.setCommonErrorHandler(errorHandler);
        return factory;
    }
}

// Listen to Dead Letter Topic
@KafkaListener(topics = "orders.DLT", groupId = "dlt-group")
public void handleDLT(@Payload OrderEvent event,
                       @Header(KafkaHeaders.EXCEPTION_MESSAGE) String error) {
    System.err.println("Failed event: " + event.getOrderId() + " | Error: " + error);
    // Alert, log, or store in DB for manual review
}
```

---

## Kafka Streams (Real-Time Processing)

```java
@Configuration
@EnableKafkaStreams
public class KafkaStreamsConfig {

    @Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME)
    public KafkaStreamsConfiguration streamsConfig() {
        Map<String, Object> props = new HashMap<>();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "order-processor");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        return new KafkaStreamsConfiguration(props);
    }

    @Bean
    public KStream<String, String> processOrders(StreamsBuilder builder) {
        KStream<String, String> stream = builder.stream("orders");

        // Filter and transform
        stream
            .filter((key, value) -> value.contains("COMPLETED"))
            .mapValues(value -> value.toUpperCase())
            .to("completed-orders");

        return stream;
    }
}
```

---

## Kafka vs Traditional Messaging

| Feature            | Kafka                        | RabbitMQ / ActiveMQ          |
|--------------------|------------------------------|-------------------------------|
| Model              | Log-based (pull)             | Queue-based (push)            |
| Message Retention  | Configurable (days/weeks)    | Deleted after consumption     |
| Throughput         | Millions of msgs/sec         | Thousands of msgs/sec         |
| Replay             | Yes (offset replay)          | No                            |
| Ordering           | Per partition                | Per queue                     |
| Use Case           | Event streaming, analytics   | Task queues, RPC              |

---

## Best Practices
- Use a meaningful message key for partition affinity (e.g., `customerId`)
- Set `acks=all` on producers for durability
- Use consumer groups to scale consumers horizontally
- Implement dead letter topics for poison message handling
- Monitor consumer group lag (offset lag = backpressure indicator)
- Use Schema Registry (Confluent) + Avro for schema evolution
- Keep messages small; reference large payloads by ID
- Set appropriate retention periods per topic