# 3. Master Spring Framework Ecosystem

## Overview
The Spring Framework is a vast ecosystem of projects covering everything from web development and data access to security, messaging, and reactive programming. Mastering it means understanding the core container and the most important sub-projects.

---

## Spring Ecosystem Map

```
Spring Framework (Core)
├── Spring Boot          — Auto-configuration, embedded server, starter POMs
├── Spring MVC           — Web layer, REST controllers
├── Spring WebFlux       — Reactive, non-blocking web framework
├── Spring Data          — Repository abstraction (JPA, MongoDB, Redis, etc.)
├── Spring Security      — Authentication & Authorization
├── Spring Cloud         — Microservices tooling (Eureka, Gateway, Config, etc.)
├── Spring Batch         — Large-scale batch processing
├── Spring Integration   — Enterprise integration patterns (EIP)
├── Spring Messaging     — Kafka, RabbitMQ, WebSocket
└── Spring AOP           — Aspect-Oriented Programming
```

---

## 1. Spring Core — IoC & Dependency Injection

The IoC (Inversion of Control) container is the heart of Spring. It manages object lifecycle and dependencies.

### Bean Declaration
```java
// Method 1: @Component stereotype annotations
@Component      // Generic bean
@Service        // Business logic layer
@Repository     // Data access layer
@Controller     // Web layer
@RestController // Web layer + @ResponseBody

// Method 2: @Bean inside @Configuration class
@Configuration
public class AppConfig {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### Dependency Injection
```java
// Constructor Injection (PREFERRED — promotes immutability & testability)
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {  // Spring auto-injects
        this.repository = repository;
    }
}

// Field Injection (convenient but not recommended for production)
@Service
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

### Bean Scopes
```java
@Component
@Scope("singleton")   // Default: one instance per container
@Scope("prototype")   // New instance per request
@Scope("request")     // One per HTTP request (web only)
@Scope("session")     // One per HTTP session (web only)
```

---

## 2. Spring AOP — Aspect-Oriented Programming

AOP lets you separate cross-cutting concerns (logging, security, transactions) from business logic.

```java
@Aspect
@Component
public class LoggingAspect {

    // Before any method in the service layer
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Calling: " + joinPoint.getSignature().getName());
    }

    // After returning successfully
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
    public void logAfterReturning(Object result) {
        System.out.println("Method returned: " + result);
    }

    // Around advice (most powerful — can alter inputs/outputs)
    @Around("execution(* com.example.service.*.*(..))")
    public Object measureTime(ProceedingJoinPoint pjp) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = pjp.proceed();
        System.out.println("Execution time: " + (System.currentTimeMillis() - start) + "ms");
        return result;
    }
}
```

---

## 3. Spring Data JPA

Abstracts the data access layer; eliminates boilerplate CRUD code.

```java
// Repository with derived queries
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByAgeGreaterThan(int age);
    boolean existsByEmail(String email);
}

// Custom JPQL query
@Query("SELECT u FROM User u WHERE u.status = :status")
List<User> findActiveUsers(@Param("status") String status);

// Native SQL
@Query(value = "SELECT * FROM users WHERE email = ?1", nativeQuery = true)
User findByEmailNative(String email);
```

### Transactions
```java
@Service
public class TransferService {

    @Transactional  // Rollbacks on RuntimeException by default
    public void transfer(Long fromId, Long toId, double amount) {
        Account from = accountRepo.findById(fromId).orElseThrow();
        Account to   = accountRepo.findById(toId).orElseThrow();
        from.debit(amount);
        to.credit(amount);
        accountRepo.save(from);
        accountRepo.save(to);
    }
}
```

---

## 4. Spring Security

Handles authentication and authorization.

### Security Configuration (Spring Boot 3.x)
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .sessionManagement(session ->
                session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### JWT Authentication Filter
```java
@Component
public class JwtAuthFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain chain) throws ServletException, IOException {
        String header = request.getHeader("Authorization");
        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            String username = jwtService.extractUsername(token);
            // Set SecurityContext...
        }
        chain.doFilter(request, response);
    }
}
```

---

## 5. Spring WebFlux (Reactive)

Non-blocking, reactive programming model using Project Reactor.

```java
@RestController
@RequestMapping("/api/products")
public class ReactiveProductController {

    @Autowired
    private ReactiveProductRepository repository;

    @GetMapping
    public Flux<Product> getAll() {              // Flux = 0..N elements
        return repository.findAll();
    }

    @GetMapping("/{id}")
    public Mono<Product> getOne(@PathVariable String id) {  // Mono = 0..1 element
        return repository.findById(id);
    }

    @PostMapping
    public Mono<Product> create(@RequestBody Product product) {
        return repository.save(product);
    }
}
```

---

## 6. Spring Events

Loose coupling via application events.

```java
// Define Event
public class UserRegisteredEvent extends ApplicationEvent {
    private final User user;
    public UserRegisteredEvent(Object source, User user) {
        super(source);
        this.user = user;
    }
}

// Publish Event
@Service
public class AuthService {
    @Autowired
    private ApplicationEventPublisher publisher;

    public void register(User user) {
        userRepo.save(user);
        publisher.publishEvent(new UserRegisteredEvent(this, user));
    }
}

// Listen to Event
@Component
public class EmailListener {
    @EventListener
    public void onUserRegistered(UserRegisteredEvent event) {
        emailService.sendWelcomeEmail(event.getUser());
    }
}
```

---

## 7. Spring Boot Actuator

Production-ready endpoints for monitoring.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,env,beans
  endpoint:
    health:
      show-details: always
```

Key endpoints: `/actuator/health`, `/actuator/metrics`, `/actuator/info`

---

## Spring Sub-Project Quick Reference

| Project            | Use Case                                        |
|--------------------|-------------------------------------------------|
| Spring Boot        | Rapid application setup & auto-configuration    |
| Spring Data JPA    | Relational DB access (MySQL, PostgreSQL, H2)    |
| Spring Data MongoDB| Document DB access                              |
| Spring Data Redis  | Caching & session storage                       |
| Spring Security    | Auth, JWT, OAuth2, LDAP                         |
| Spring Cloud       | Microservices (Eureka, Gateway, Config, Feign)  |
| Spring Batch       | Scheduled batch jobs                            |
| Spring WebFlux     | Reactive / non-blocking APIs                    |
| Spring Integration | EIP patterns, file/queue integration            |

---

## Best Practices
- Prefer constructor injection over field injection
- Use `@Transactional` at the service layer, not the controller
- Keep configuration in `application.yml` / externalized config
- Use profiles (`@Profile("dev")`, `@Profile("prod")`) for environment-specific beans
- Use Spring Boot Actuator for health checks and metrics in production