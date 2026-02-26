# 4. Learn Containerization — Docker & Kubernetes

## Overview
Containerization packages your Java application and all its dependencies into a portable unit that runs consistently anywhere. Docker creates containers; Kubernetes (K8s) orchestrates them at scale.

---

## Part A: Docker

### Core Concepts

| Term        | Description                                           |
|-------------|-------------------------------------------------------|
| Image       | Blueprint / snapshot of your app + environment        |
| Container   | Running instance of an image                          |
| Dockerfile  | Instructions to build an image                        |
| Registry    | Image repository (Docker Hub, AWS ECR, GCR)           |
| Volume      | Persistent data storage outside the container         |
| Network     | Communication channel between containers              |

---

### Dockerfile for a Spring Boot Application

```dockerfile
# ---- Stage 1: Build ----
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
# Download dependencies separately (better layer caching)
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn package -DskipTests

# ---- Stage 2: Runtime ----
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app

# Non-root user for security
RUN addgroup -S spring && adduser -S spring -G spring
USER spring

COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Build & Run
```bash
# Build image
docker build -t my-spring-app:1.0 .

# Run container
docker run -d \
  --name spring-app \
  -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=prod \
  my-spring-app:1.0

# View logs
docker logs -f spring-app

# Stop & remove
docker stop spring-app && docker rm spring-app
```

---

### Docker Compose (Multi-Container Setup)

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    container_name: spring-app
    ports:
      - "8080:8080"
    environment:
      - SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/mydb
      - SPRING_DATASOURCE_USERNAME=postgres
      - SPRING_DATASOURCE_PASSWORD=secret
    depends_on:
      db:
        condition: service_healthy
    networks:
      - app-network

  db:
    image: postgres:16-alpine
    container_name: postgres-db
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    container_name: redis-cache
    ports:
      - "6379:6379"
    networks:
      - app-network

volumes:
  postgres-data:

networks:
  app-network:
    driver: bridge
```

```bash
# Start all services
docker compose up -d

# View running containers
docker compose ps

# Tear down
docker compose down -v
```

---

### Essential Docker Commands

```bash
# Images
docker images                          # List images
docker pull openjdk:21-jre             # Pull from registry
docker rmi my-spring-app:1.0           # Remove image
docker tag my-app:1.0 myrepo/my-app:1.0 # Tag for push
docker push myrepo/my-app:1.0          # Push to registry

# Containers
docker ps                              # Running containers
docker ps -a                           # All containers
docker exec -it spring-app /bin/sh     # Shell into container
docker inspect spring-app              # Container details
docker stats                           # Resource usage

# Cleanup
docker system prune -af                # Remove all unused resources
```

---

## Part B: Kubernetes (K8s)

### Core Concepts

| Resource      | Description                                              |
|---------------|----------------------------------------------------------|
| Pod           | Smallest deployable unit; wraps one or more containers   |
| Deployment    | Manages replica Pods, handles rolling updates            |
| Service       | Stable network endpoint to access Pods                   |
| ConfigMap     | Non-sensitive configuration data                         |
| Secret        | Sensitive data (passwords, tokens) — base64 encoded      |
| Ingress       | HTTP/HTTPS routing into the cluster                      |
| Namespace     | Logical isolation within a cluster                       |
| HPA           | Horizontal Pod Autoscaler — auto-scales based on CPU/mem |

---

### Deployment Manifest

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-app
  namespace: production
  labels:
    app: spring-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: spring-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: spring-app
    spec:
      containers:
        - name: spring-app
          image: myrepo/spring-app:1.0
          ports:
            - containerPort: 8080
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "prod"
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: password
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          readinessProbe:
            httpGet:
              path: /actuator/health/readiness
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /actuator/health/liveness
              port: 8080
            initialDelaySeconds: 60
            periodSeconds: 15
```

---

### Service Manifest

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: spring-app-service
  namespace: production
spec:
  selector:
    app: spring-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP   # ClusterIP | NodePort | LoadBalancer
```

---

### ConfigMap & Secret

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: INFO

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=   # base64 encoded "password123"
  username: cG9zdGdyZXM=       # base64 encoded "postgres"
```

---

### Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: spring-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: spring-app-service
                port:
                  number: 80
```

---

### Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: spring-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: spring-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

### Essential kubectl Commands

```bash
# Apply manifests
kubectl apply -f deployment.yaml
kubectl apply -f .                  # Apply all YAMLs in directory

# Inspect
kubectl get pods -n production
kubectl get services -n production
kubectl describe pod <pod-name> -n production
kubectl logs <pod-name> -n production -f

# Scaling
kubectl scale deployment spring-app --replicas=5 -n production

# Rolling update
kubectl set image deployment/spring-app spring-app=myrepo/spring-app:2.0

# Rollback
kubectl rollout undo deployment/spring-app

# Port forward (local testing)
kubectl port-forward svc/spring-app-service 8080:80 -n production

# Delete
kubectl delete -f deployment.yaml
```

---

### Spring Boot + Kubernetes Integration

```properties
# application.properties — Spring Boot Actuator probes for K8s
management.endpoint.health.probes.enabled=true
management.health.livenessState.enabled=true
management.health.readinessState.enabled=true
```

---

## Docker vs Kubernetes — When to Use

| Scenario                        | Tool       |
|---------------------------------|------------|
| Local development               | Docker / Docker Compose |
| Single server deployment        | Docker     |
| Multi-service local testing     | Docker Compose |
| Production multi-node scaling   | Kubernetes |
| Auto-healing & self-scaling     | Kubernetes |
| CI/CD pipeline image build      | Docker     |

---

## Best Practices
- Use multi-stage Docker builds to minimize image size
- Never run containers as root
- Set resource `requests` and `limits` in K8s
- Use liveness and readiness probes with Spring Actuator
- Store secrets in Kubernetes Secrets or external vaults (HashiCorp Vault, AWS Secrets Manager)
- Use namespaces to isolate environments (dev, staging, prod)
- Tag images with semantic versions, never just `latest`