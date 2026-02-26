# 🌐 HTTP and API Fundamentals - Complete Guide

**Author:** Prerak  
**Purpose:** Master HTTP protocol and REST API concepts  
**Version:** 1.0 Complete

---

## 📋 TABLE OF CONTENTS

1. [HTTP Fundamentals](#http-fundamentals)
2. [HTTP Methods](#http-methods)
3. [HTTP Status Codes](#http-status-codes)
4. [HTTP Headers](#http-headers)
5. [Request and Response Structure](#request-and-response-structure)
6. [API Fundamentals](#api-fundamentals)
7. [REST API Design](#rest-api-design)
8. [Authentication and Security](#authentication-and-security)
9. [Python HTTP Requests](#python-http-requests)
10. [Best Practices](#best-practices)

---

## 1. HTTP Fundamentals

### What is HTTP?

**HTTP (HyperText Transfer Protocol)** is an application-layer protocol for transmitting hypermedia documents. It's the foundation of data communication for the World Wide Web.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| **Stateless** | Each request is independent |
| **Client-Server** | Request-response model |
| **Text-based** | Human-readable protocol |
| **Port** | Default port 80 (HTTP), 443 (HTTPS) |
| **Protocol** | Application layer (OSI Model) |

### HTTP vs HTTPS

```
HTTP (Port 80)
- Unencrypted
- Faster (no encryption overhead)
- Insecure for sensitive data

HTTPS (Port 443)
- Encrypted with SSL/TLS
- Secure data transmission
- Required for sensitive data
- SEO benefits
```

### How HTTP Works

```
Client                                    Server
  |                                         |
  |  1. DNS Resolution                      |
  |------------------------------------>    |
  |                                         |
  |  2. TCP Connection (3-way handshake)    |
  |<----------------------------------->    |
  |                                         |
  |  3. HTTP Request                        |
  |------------------------------------>    |
  |                                         |
  |  4. HTTP Response                       |
  |<------------------------------------|    |
  |                                         |
  |  5. Connection Close (or keep-alive)    |
  |<----------------------------------->    |
```

### HTTP Request-Response Cycle

```python
# Simple illustration
"""
CLIENT SENDS:
GET /api/users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer token123

SERVER RESPONDS:
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 85

{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
}
"""
```

---

## 2. HTTP Methods

### Common HTTP Methods

| Method | Purpose | Safe | Idempotent | Cacheable |
|--------|---------|------|------------|-----------|
| **GET** | Retrieve data | Yes | Yes | Yes |
| **POST** | Create new resource | No | No | No* |
| **PUT** | Update/Replace resource | No | Yes | No |
| **PATCH** | Partial update | No | No | No |
| **DELETE** | Remove resource | No | Yes | No |
| **HEAD** | GET without body | Yes | Yes | Yes |
| **OPTIONS** | Get allowed methods | Yes | Yes | No |

*POST can be cacheable with proper headers

### GET - Retrieve Data

```python
# Python example
import requests

# Get single resource
response = requests.get('https://api.example.com/users/123')
user = response.json()

# Get collection with query parameters
response = requests.get('https://api.example.com/users', params={
    'page': 1,
    'limit': 10,
    'sort': 'name'
})
users = response.json()

# URL becomes: https://api.example.com/users?page=1&limit=10&sort=name
```

**Characteristics:**
- Should not modify server state
- Parameters in URL (query string)
- Can be bookmarked
- Can be cached
- Length limited (~2000 chars)

### POST - Create Resource

```python
# Create new user
new_user = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.post(
    'https://api.example.com/users',
    json=new_user,
    headers={'Content-Type': 'application/json'}
)

if response.status_code == 201:
    created_user = response.json()
    print(f"Created user ID: {created_user['id']}")
```

**Characteristics:**
- Creates new resources
- Data in request body
- Not idempotent (multiple calls = multiple resources)
- Not cacheable by default

### PUT - Update/Replace Resource

```python
# Replace entire user resource
updated_user = {
    'name': 'John Smith',
    'email': 'john.smith@example.com',
    'age': 31
}

response = requests.put(
    'https://api.example.com/users/123',
    json=updated_user
)

if response.status_code == 200:
    print("User updated successfully")
```

**Characteristics:**
- Replaces entire resource
- Idempotent (same request multiple times = same result)
- Must send complete resource

### PATCH - Partial Update

```python
# Update only specific fields
partial_update = {
    'age': 31
}

response = requests.patch(
    'https://api.example.com/users/123',
    json=partial_update
)

if response.status_code == 200:
    print("User partially updated")
```

**Characteristics:**
- Updates specific fields
- Sends only changed fields
- More efficient than PUT

### DELETE - Remove Resource

```python
# Delete user
response = requests.delete('https://api.example.com/users/123')

if response.status_code == 204:
    print("User deleted successfully")
elif response.status_code == 404:
    print("User not found")
```

**Characteristics:**
- Removes resource
- Idempotent
- Often returns 204 (No Content)

### HEAD - Metadata Only

```python
# Check if resource exists without downloading
response = requests.head('https://api.example.com/users/123')

if response.status_code == 200:
    print(f"Content-Length: {response.headers.get('Content-Length')}")
    print(f"Last-Modified: {response.headers.get('Last-Modified')}")
```

### OPTIONS - Discover Allowed Methods

```python
# Check what methods are allowed
response = requests.options('https://api.example.com/users/123')
allowed_methods = response.headers.get('Allow')
print(f"Allowed methods: {allowed_methods}")
```

---

## 3. HTTP Status Codes

### Status Code Categories

| Range | Category | Meaning |
|-------|----------|---------|
| **1xx** | Informational | Request received, continuing |
| **2xx** | Success | Request successful |
| **3xx** | Redirection | Further action needed |
| **4xx** | Client Error | Client-side error |
| **5xx** | Server Error | Server-side error |

### Common Status Codes

#### 2xx Success

```python
# 200 OK - Request successful
response = requests.get('https://api.example.com/users/123')
assert response.status_code == 200

# 201 Created - Resource created
response = requests.post('https://api.example.com/users', json=new_user)
assert response.status_code == 201

# 204 No Content - Success, no body returned
response = requests.delete('https://api.example.com/users/123')
assert response.status_code == 204
```

| Code | Name | Usage |
|------|------|-------|
| 200 | OK | General success |
| 201 | Created | Resource created (POST/PUT) |
| 202 | Accepted | Async processing started |
| 204 | No Content | Success, no response body |

#### 3xx Redirection

```python
# 301 Moved Permanently
response = requests.get('https://example.com/old-url', allow_redirects=False)
if response.status_code == 301:
    new_url = response.headers['Location']
    print(f"Redirect to: {new_url}")

# 304 Not Modified - Use cached version
response = requests.get('https://api.example.com/data', headers={
    'If-None-Match': 'etag123'
})
if response.status_code == 304:
    print("Use cached version")
```

| Code | Name | Usage |
|------|------|-------|
| 301 | Moved Permanently | Permanent redirect |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cached version valid |
| 307 | Temporary Redirect | Keep HTTP method |

#### 4xx Client Errors

```python
# 400 Bad Request
try:
    response = requests.post('https://api.example.com/users', json=invalid_data)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 400:
        print(f"Bad request: {e.response.json()}")

# 401 Unauthorized
response = requests.get('https://api.example.com/protected')
if response.status_code == 401:
    print("Authentication required")

# 403 Forbidden
response = requests.get('https://api.example.com/admin')
if response.status_code == 403:
    print("Access denied - insufficient permissions")

# 404 Not Found
response = requests.get('https://api.example.com/users/999')
if response.status_code == 404:
    print("Resource not found")

# 429 Too Many Requests
response = requests.get('https://api.example.com/data')
if response.status_code == 429:
    retry_after = response.headers.get('Retry-After')
    print(f"Rate limited. Retry after {retry_after} seconds")
```

| Code | Name | Meaning |
|------|------|---------|
| 400 | Bad Request | Invalid syntax/data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | HTTP method not supported |
| 409 | Conflict | Request conflicts with current state |
| 422 | Unprocessable Entity | Validation errors |
| 429 | Too Many Requests | Rate limit exceeded |

#### 5xx Server Errors

```python
# 500 Internal Server Error
response = requests.get('https://api.example.com/users')
if response.status_code == 500:
    print("Server error occurred")

# 502 Bad Gateway
# Proxy received invalid response from upstream server

# 503 Service Unavailable
response = requests.get('https://api.example.com/data')
if response.status_code == 503:
    retry_after = response.headers.get('Retry-After')
    print(f"Service temporarily unavailable. Retry after {retry_after}")

# 504 Gateway Timeout
# Upstream server didn't respond in time
```

| Code | Name | Meaning |
|------|------|---------|
| 500 | Internal Server Error | Generic server error |
| 502 | Bad Gateway | Invalid upstream response |
| 503 | Service Unavailable | Temporary downtime |
| 504 | Gateway Timeout | Upstream timeout |

---

## 4. HTTP Headers

### Request Headers

```python
# Common request headers
headers = {
    # Content headers
    'Content-Type': 'application/json',
    'Content-Length': '123',
    
    # Authentication
    'Authorization': 'Bearer eyJhbGc...',
    'API-Key': 'your-api-key',
    
    # Client info
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    
    # Caching
    'If-None-Match': 'etag123',
    'If-Modified-Since': 'Wed, 21 Oct 2023 07:28:00 GMT',
    
    # Custom headers
    'X-Request-ID': 'unique-request-id',
    'X-API-Version': 'v1'
}

response = requests.get('https://api.example.com/data', headers=headers)
```

### Response Headers

```python
response = requests.get('https://api.example.com/users')

# Content headers
content_type = response.headers.get('Content-Type')
content_length = response.headers.get('Content-Length')

# Caching
cache_control = response.headers.get('Cache-Control')
etag = response.headers.get('ETag')
last_modified = response.headers.get('Last-Modified')

# Security
cors = response.headers.get('Access-Control-Allow-Origin')
csp = response.headers.get('Content-Security-Policy')

# Rate limiting
rate_limit = response.headers.get('X-RateLimit-Limit')
rate_remaining = response.headers.get('X-RateLimit-Remaining')
rate_reset = response.headers.get('X-RateLimit-Reset')

print(f"Rate Limit: {rate_remaining}/{rate_limit} (resets at {rate_reset})")
```

### Important Headers Reference

#### Content Negotiation

```python
# Request specific content type
response = requests.get('https://api.example.com/data', headers={
    'Accept': 'application/json'  # Or application/xml, text/html, etc.
})

# Send data in specific format
response = requests.post('https://api.example.com/data',
    json=data,
    headers={'Content-Type': 'application/json'}
)
```

#### Caching Headers

```python
# Server tells client how to cache
"""
Cache-Control: max-age=3600, public
Cache-Control: no-cache, no-store, must-revalidate
Expires: Wed, 21 Oct 2023 07:28:00 GMT
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT
"""

# Client sends conditional request
response = requests.get('https://api.example.com/data', headers={
    'If-None-Match': 'etag-value',
    'If-Modified-Since': 'Wed, 21 Oct 2023 07:28:00 GMT'
})
```

#### CORS Headers

```python
# Preflight request (OPTIONS)
"""
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 86400
Access-Control-Allow-Credentials: true
"""
```

---

## 5. Request and Response Structure

### HTTP Request Structure

```
POST /api/users HTTP/1.1                    ← Request Line
Host: api.example.com                        ← Headers
Content-Type: application/json
Content-Length: 85
Authorization: Bearer token123
Accept: application/json

{                                            ← Body
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}
```

### HTTP Response Structure

```
HTTP/1.1 201 Created                         ← Status Line
Content-Type: application/json               ← Headers
Content-Length: 105
Location: /api/users/123
ETag: "abc123"
Date: Wed, 21 Oct 2023 07:28:00 GMT

{                                            ← Body
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "created_at": "2023-10-21T07:28:00Z"
}
```

### Python Request Example

```python
import requests
import json

# Complete request example
url = 'https://api.example.com/users'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your-token-here',
    'User-Agent': 'MyApp/1.0'
}
data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.post(url, json=data, headers=headers)

# Access response components
print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Body: {response.json()}")
print(f"Encoding: {response.encoding}")
print(f"URL: {response.url}")
```

---

## 6. API Fundamentals

### What is an API?

**API (Application Programming Interface)** is a set of rules and protocols that allows different software applications to communicate with each other.

### Types of APIs

| Type | Description | Example |
|------|-------------|---------|
| **REST** | Resource-based, HTTP methods | Most web APIs |
| **SOAP** | XML-based protocol | Enterprise systems |
| **GraphQL** | Query language | Facebook, GitHub |
| **WebSocket** | Bi-directional communication | Real-time apps |
| **gRPC** | High-performance RPC | Microservices |

### REST API Principles

```
1. Client-Server Architecture
2. Stateless Communication
3. Cacheable Responses
4. Uniform Interface
5. Layered System
6. Code on Demand (optional)
```

### Resource-Based URLs

```python
# Good - Resource-based
GET    /api/users              # Get all users
GET    /api/users/123          # Get specific user
POST   /api/users              # Create new user
PUT    /api/users/123          # Update user
DELETE /api/users/123          # Delete user

# Nested resources
GET    /api/users/123/orders   # Get user's orders
GET    /api/users/123/orders/456  # Get specific order

# Bad - Action-based (RPC-style)
POST   /api/getUser
POST   /api/createUser
POST   /api/updateUser
POST   /api/deleteUser
```

---

## 7. REST API Design

### Naming Conventions

```python
# Use nouns, not verbs
✓ GET  /api/products
✗ GET  /api/getProducts

# Use plural nouns
✓ GET  /api/users
✗ GET  /api/user

# Use kebab-case for multi-word resources
✓ GET  /api/user-profiles
✗ GET  /api/userProfiles
✗ GET  /api/user_profiles

# Keep it simple
✓ GET  /api/users/123/orders
✗ GET  /api/getUserOrdersByUserId/123
```

### Query Parameters

```python
# Filtering
GET /api/products?category=electronics&price_min=100&price_max=500

# Sorting
GET /api/users?sort=name&order=asc

# Pagination
GET /api/products?page=2&limit=20

# Search
GET /api/users?search=john&fields=name,email

# Implementation
from flask import Flask, request

@app.route('/api/products')
def get_products():
    # Get query parameters
    category = request.args.get('category')
    min_price = request.args.get('price_min', type=float)
    max_price = request.args.get('price_max', type=float)
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)
    
    # Filter and return products
    products = filter_products(category, min_price, max_price)
    return paginate(products, page, limit)
```

### Versioning

```python
# URL versioning (most common)
GET /api/v1/users
GET /api/v2/users

# Header versioning
GET /api/users
Headers: API-Version: 1

# Content-Type versioning
GET /api/users
Headers: Accept: application/vnd.myapi.v1+json
```

### Response Format

```python
# Success response (200 OK)
{
    "status": "success",
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com"
    }
}

# Collection response
{
    "status": "success",
    "data": [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"}
    ],
    "pagination": {
        "page": 1,
        "limit": 20,
        "total": 100,
        "pages": 5
    }
}

# Error response (400 Bad Request)
{
    "status": "error",
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid input data",
        "details": [
            {"field": "email", "message": "Invalid email format"},
            {"field": "age", "message": "Must be at least 18"}
        ]
    }
}
```

---

## 8. Authentication and Security

### Authentication Methods

#### 1. API Keys

```python
# In header
response = requests.get('https://api.example.com/data', headers={
    'X-API-Key': 'your-api-key-here'
})

# In query parameter (less secure)
response = requests.get('https://api.example.com/data?api_key=your-key')
```

#### 2. Bearer Token (JWT)

```python
# Get token
response = requests.post('https://api.example.com/auth/login', json={
    'username': 'john',
    'password': 'secret'
})
token = response.json()['access_token']

# Use token
response = requests.get('https://api.example.com/protected', headers={
    'Authorization': f'Bearer {token}'
})
```

#### 3. Basic Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.example.com/data',
    auth=HTTPBasicAuth('username', 'password')
)

# Or simpler
response = requests.get('https://api.example.com/data',
    auth=('username', 'password')
)
```

#### 4. OAuth 2.0

```python
# Authorization code flow
import requests

# Step 1: Get authorization code (user login)
auth_url = 'https://auth.example.com/oauth/authorize'
params = {
    'client_id': 'your-client-id',
    'redirect_uri': 'https://yourapp.com/callback',
    'response_type': 'code',
    'scope': 'read write'
}

# Step 2: Exchange code for token
token_url = 'https://auth.example.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'code': 'authorization-code',
    'client_id': 'your-client-id',
    'client_secret': 'your-client-secret',
    'redirect_uri': 'https://yourapp.com/callback'
}
response = requests.post(token_url, data=data)
tokens = response.json()

# Step 3: Use access token
headers = {'Authorization': f"Bearer {tokens['access_token']}"}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Security Best Practices

```python
# 1. Always use HTTPS
url = 'https://api.example.com'  # Not http://

# 2. Validate SSL certificates
response = requests.get(url, verify=True)

# 3. Set timeouts
response = requests.get(url, timeout=30)

# 4. Rate limiting
from time import sleep
from datetime import datetime

class RateLimiter:
    def __init__(self, calls_per_minute):
        self.calls_per_minute = calls_per_minute
        self.calls = []
    
    def wait_if_needed(self):
        now = datetime.now()
        # Remove calls older than 1 minute
        self.calls = [t for t in self.calls if (now - t).seconds < 60]
        
        if len(self.calls) >= self.calls_per_minute:
            sleep_time = 60 - (now - self.calls[0]).seconds
            sleep(sleep_time)
        
        self.calls.append(now)

limiter = RateLimiter(calls_per_minute=60)

def make_api_call():
    limiter.wait_if_needed()
    return requests.get('https://api.example.com/data')
```

---

## 9. Python HTTP Requests

### Requests Library Basics

```python
import requests

# GET request
response = requests.get('https://api.example.com/users/123')

# POST request
data = {'name': 'John', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=data)

# PUT request
response = requests.put('https://api.example.com/users/123', json=data)

# PATCH request
response = requests.patch('https://api.example.com/users/123', json={'age': 31})

# DELETE request
response = requests.delete('https://api.example.com/users/123')
```

### Handling Responses

```python
response = requests.get('https://api.example.com/users/123')

# Status code
print(response.status_code)  # 200
print(response.ok)  # True if status < 400

# Response body
print(response.text)  # Raw string
print(response.content)  # Bytes
print(response.json())  # Parsed JSON

# Headers
print(response.headers)
print(response.headers['Content-Type'])

# Cookies
print(response.cookies)

# Raise exception for error status
response.raise_for_status()
```

### Session Management

```python
# Use session for multiple requests
session = requests.Session()

# Set default headers
session.headers.update({
    'Authorization': 'Bearer token123',
    'User-Agent': 'MyApp/1.0'
})

# All requests use session settings
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/products')

# Cookies are automatically handled
session.close()
```

### Error Handling

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError

try:
    response = requests.get('https://api.example.com/data', timeout=10)
    response.raise_for_status()
    data = response.json()
    
except Timeout:
    print("Request timed out")
except ConnectionError:
    print("Failed to connect to server")
except HTTPError as e:
    if e.response.status_code == 404:
        print("Resource not found")
    elif e.response.status_code == 401:
        print("Unauthorized")
    else:
        print(f"HTTP error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Complete API Client Example

```python
import requests
from typing import Optional, Dict, Any

class APIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        if api_key:
            self.session.headers['Authorization'] = f'Bearer {api_key}'
        
        self.session.headers['User-Agent'] = 'MyApp/1.0'
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[Any, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, timeout=30, **kwargs)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e.response.status_code}")
            raise
        except requests.exceptions.Timeout:
            print("Request timed out")
            raise
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        return self._make_request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Dict) -> Dict:
        return self._make_request('POST', endpoint, json=data)
    
    def put(self, endpoint: str, data: Dict) -> Dict:
        return self._make_request('PUT', endpoint, json=data)
    
    def patch(self, endpoint: str, data: Dict) -> Dict:
        return self._make_request('PATCH', endpoint, json=data)
    
    def delete(self, endpoint: str) -> Dict:
        return self._make_request('DELETE', endpoint)
    
    def close(self):
        self.session.close()

# Usage
client = APIClient('https://api.example.com', api_key='your-key')

# Get user
user = client.get('/users/123')

# Create user
new_user = client.post('/users', data={'name': 'John', 'email': 'john@example.com'})

# Update user
updated_user = client.patch('/users/123', data={'age': 31})

# Delete user
client.delete('/users/123')

client.close()
```

---

## 10. Best Practices

### API Design Best Practices

```
1. Use nouns for resources, not verbs
2. Use plural nouns consistently
3. Keep URLs simple and intuitive
4. Version your API
5. Return appropriate status codes
6. Provide detailed error messages
7. Support filtering, sorting, and pagination
8. Document your API thoroughly
9. Use HTTPS everywhere
10. Implement rate limiting
```

### Request Best Practices

```python
# 1. Set timeouts
requests.get(url, timeout=30)

# 2. Use sessions for multiple requests
session = requests.Session()

# 3. Handle errors properly
try:
    response.raise_for_status()
except HTTPError as e:
    # Handle error
    pass

# 4. Close connections
session.close()

# 5. Use connection pooling
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100
)
session.mount('https://', adapter)
```

### Response Best Practices

```python
# Consistent response structure
{
    "status": "success|error",
    "data": {},  # For success
    "error": {},  # For error
    "metadata": {}  # Pagination, etc.
}

# Include request ID for debugging
{
    "request_id": "unique-id",
    "status": "success",
    "data": {}
}

# Provide helpful error messages
{
    "status": "error",
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Validation failed",
        "details": [
            {"field": "email", "error": "Invalid format"}
        ]
    }
}
```

---

## 🎯 Quick Reference

### Common HTTP Methods

```
GET    - Retrieve resource
POST   - Create resource
PUT    - Update/replace resource
PATCH  - Partial update
DELETE - Remove resource
```

### Status Code Quick Guide

```
200 - OK
201 - Created
204 - No Content
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Server Error
```

### Essential Headers

```
Authorization: Bearer token
Content-Type: application/json
Accept: application/json
User-Agent: MyApp/1.0
```

---

**END OF HTTP AND API FUNDAMENTALS**

*You're now ready to build and consume REST APIs!*