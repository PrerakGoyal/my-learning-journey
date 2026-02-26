# 2. Create Microservices Applications

## Overview
Microservices architecture breaks a monolithic application into small, independently deployable services that communicate over a network. Spring Boot + Spring Cloud is the de facto Java stack for microservices.

---

## Core Building Blocks

| Component              | Tool / Library                        | Purpose                              |
|------------------------|---------------------------------------|--------------------------------------|
| Service Discovery      | Eureka Server (Spring Cloud Netflix)  | Services register and discover each other |
| API Gateway            | Spring Cloud Gateway                  | Single entry point for all clients   |
| Config Server          | Spring Cloud Config                   | Centralized configuration            |
| Load Balancing         | Spring Cloud LoadBalancer             | Client-side load balancing           |
| Circuit Breaker        | Resilience4j                          | Fault tolerance                      |
| Inter-service Calls    | OpenFeign / RestTemplate / WebClient  | Service-to-service HTTP calls        |
| Distributed Tracing    | Micrometer + Zipkin                   | End-to-end request tracing           |

---

## Project Structure (Example: E-Commerce)

```
ecommerce/
├── eureka-server/          # Service Registry
├── api-gateway/            # Gateway
├── config-server/          # Central Config
├── user-service/           # Manages users
├── product-service/        # Manages products
└── order-service/          # Manages orders
```

---

## 1. Eureka Server (Service Registry)

### Dependency
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
</dependency>
```

### Main Class
```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServerApplication.class, args);
    }
}
```

### `application.yml`
```yaml
server:
  port: 8761
eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
```

---

## 2. Microservice (e.g., Product Service)

### Dependency
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
```

### `application.yml`
```yaml
server:
  port: 8082
spring:
  application:
    name: product-service
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
```

---

## 3. API Gateway

### Dependency
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>
```

### `application.yml`
```yaml
server:
  port: 8080
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
        - id: product-service
          uri: lb://product-service
          predicates:
            - Path=/api/products/**
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
```

---

## 4. Inter-Service Communication with OpenFeign

### Dependency
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

### Enable Feign in Main Class
```java
@SpringBootApplication
@EnableFeignClients
public class OrderServiceApplication { ... }
```

### Feign Client Interface
```java
@FeignClient(name = "product-service")
public interface ProductServiceClient {

    @GetMapping("/api/products/{id}")
    ProductDTO getProduct(@PathVariable Long id);
}
```

### Using the Client in a Service
```java
@Service
public class OrderService {

    @Autowired
    private ProductServiceClient productClient;

    public Order createOrder(OrderRequest request) {
        ProductDTO product = productClient.getProduct(request.getProductId());
        // Build order using product data...
    }
}
```

---

## 5. Circuit Breaker with Resilience4j

### Dependency
```xml
<dependency>
    <groupId>io.github.resilience4j</groupId>
    <artifactId>resilience4j-spring-boot3</artifactId>
</dependency>
```

### Usage
```java
@CircuitBreaker(name = "productService", fallbackMethod = "fallbackProduct")
public ProductDTO getProduct(Long id) {
    return productClient.getProduct(id);
}

public ProductDTO fallbackProduct(Long id, Exception ex) {
    return new ProductDTO(id, "Unavailable", 0.0);
}
```

### Configuration in `application.yml`
```yaml
resilience4j:
  circuitbreaker:
    instances:
      productService:
        slidingWindowSize: 5
        failureRateThreshold: 50
        waitDurationInOpenState: 5000
```

---

## 6. Distributed Tracing with Zipkin

### Dependencies
```xml
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-tracing-bridge-brave</artifactId>
</dependency>
<dependency>
    <groupId>io.zipkin.reporter2</groupId>
    <artifactId>zipkin-reporter-brave</artifactId>
</dependency>
```

### Configuration
```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  zipkin:
    tracing:
      endpoint: http://localhost:9411/api/v2/spans
```

Run Zipkin: `docker run -d -p 9411:9411 openzipkin/zipkin`

---

## Communication Patterns

```
Synchronous  →  REST (OpenFeign / RestTemplate / WebClient)
Asynchronous →  Apache Kafka / RabbitMQ
```

---

## Best Practices
- Each microservice owns its own database (Database per Service pattern)
- Communicate asynchronously via events whenever possible
- Use API Gateway as the only public entry point
- Implement circuit breakers to prevent cascade failures
- Use centralized logging (ELK Stack) and distributed tracing (Zipkin)
- Version your APIs (`/api/v1/...`)
- Keep services small and focused on a single business capability