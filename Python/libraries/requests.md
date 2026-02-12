# 🌐 REQUESTS LIBRARY MASTER NOTES — COMPLETE GUIDE

**Author:** Prerak  
**Purpose:** Master Python's Requests module for HTTP requests and API interactions  
**Version:** Complete Edition with Real-World Examples

---

## 📋 TABLE OF CONTENTS

1. [Introduction to Requests](#introduction-to-requests)
2. [Making HTTP Requests](#making-http-requests)
3. [Request Parameters](#request-parameters)
4. [Headers and Authentication](#headers-and-authentication)
5. [Handling Responses](#handling-responses)
6. [Working with JSON](#working-with-json)
7. [File Operations](#file-operations)
8. [Sessions and Cookies](#sessions-and-cookies)
9. [Error Handling](#error-handling)
10. [Advanced Features](#advanced-features)
11. [Real-World Applications](#real-world-applications)
12. [Best Practices](#best-practices)

---

# INTRODUCTION TO REQUESTS

## What is the Requests Library?

**Definition:**  
Requests is an elegant and simple HTTP library for Python. It makes web requests incredibly easy and human-friendly.

**Mental Model:**  
> Requests = Your Python program's way to talk to websites and APIs

**Why Requests Matters:**
- Fetch data from APIs
- Scrape website content
- Download files from the internet
- Submit forms programmatically
- Automate web interactions
- Build API clients

---

## Installation

```bash
# Install requests
pip install requests

# Install with specific version
pip install requests==2.31.0

# Verify installation
python -c "import requests; print(requests.__version__)"
```

---

## Basic Import

```python
import requests

# Check available methods
print(dir(requests))

# Get help
help(requests.get)
```

---

## HTTP Methods Overview

| Method | Purpose | Example Use |
|--------|---------|-------------|
| **GET** | Retrieve data | Fetch user profile, search results |
| **POST** | Submit data | Create new record, login |
| **PUT** | Update data | Update entire record |
| **PATCH** | Partial update | Update specific fields |
| **DELETE** | Remove data | Delete a record |
| **HEAD** | Get headers only | Check if file exists |
| **OPTIONS** | Get allowed methods | Check API capabilities |

---

# MAKING HTTP REQUESTS

## 1) GET Request (Most Common)

### Basic GET Request

```python
import requests

# Simple GET request
response = requests.get('https://api.github.com')

# Check response
print(response.status_code)  # 200
print(response.text)         # Response content
```

**Use Cases:**
- Fetch data from APIs
- Read web pages
- Download content
- Check resource availability

---

### GET with URL Parameters

```python
# Method 1: Manual URL construction
url = 'https://api.github.com/search/repositories?q=python&sort=stars'
response = requests.get(url)

# Method 2: Using params (BETTER)
url = 'https://api.github.com/search/repositories'
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc'
}
response = requests.get(url, params=params)

print(response.url)  # See final URL
print(response.json())
```

---

### Real-World GET Examples

```python
import requests

# Example 1: Weather API
def get_weather(city):
    """Get weather for a city"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'YOUR_API_KEY',
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    return None

# Example 2: GitHub user info
def get_github_user(username):
    """Get GitHub user information"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'followers': data['followers'],
            'repos': data['public_repos']
        }
    return None

# Usage
weather = get_weather('London')
print(weather)

user = get_github_user('octocat')
print(user)
```

---

## 2) POST Request

### Basic POST Request

```python
import requests

# POST with data
url = 'https://httpbin.org/post'
data = {
    'name': 'Prerak',
    'email': 'prerak@example.com'
}

response = requests.post(url, data=data)
print(response.json())
```

**Use Cases:**
- Create new records
- Submit forms
- Upload data
- User registration/login

---

### POST with JSON

```python
import requests

# POST with JSON data
url = 'https://jsonplaceholder.typicode.com/posts'

payload = {
    'title': 'My First Post',
    'body': 'This is the content',
    'userId': 1
}

# Method 1: Using json parameter (RECOMMENDED)
response = requests.post(url, json=payload)

# Method 2: Manual JSON encoding
import json
response = requests.post(
    url, 
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)

print(response.status_code)
print(response.json())
```

---

### Real-World POST Examples

```python
import requests

# Example 1: Create user account
def create_user(username, email, password):
    """Create new user via API"""
    url = "https://api.example.com/users"
    
    payload = {
        'username': username,
        'email': email,
        'password': password
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 201:  # Created
        return response.json()
    else:
        return {'error': response.json()}

# Example 2: Submit contact form
def submit_contact_form(name, email, message):
    """Submit contact form"""
    url = "https://example.com/api/contact"
    
    data = {
        'name': name,
        'email': email,
        'message': message
    }
    
    response = requests.post(url, data=data)
    return response.status_code == 200

# Usage
result = create_user('prerak', 'prerak@email.com', 'securepass123')
print(result)

success = submit_contact_form('Prerak', 'prerak@email.com', 'Hello!')
print(f"Form submitted: {success}")
```

---

## 3) PUT Request

### Update Resource

```python
import requests

# PUT - Update entire resource
url = 'https://jsonplaceholder.typicode.com/posts/1'

updated_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'Updated content',
    'userId': 1
}

response = requests.put(url, json=updated_data)
print(response.json())
```

**Use Cases:**
- Update entire records
- Replace resource data
- Overwrite configuration

---

## 4) PATCH Request

### Partial Update

```python
import requests

# PATCH - Update specific fields only
url = 'https://jsonplaceholder.typicode.com/posts/1'

partial_update = {
    'title': 'New Title Only'
}

response = requests.patch(url, json=partial_update)
print(response.json())
```

**Use Cases:**
- Update specific fields
- Partial modifications
- Efficient updates

---

## 5) DELETE Request

### Remove Resource

```python
import requests

# DELETE request
url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.delete(url)
print(response.status_code)  # 200 or 204 (No Content)
```

**Use Cases:**
- Delete records
- Remove resources
- Clear data

---

## 6) HEAD Request

### Get Headers Only

```python
import requests

# HEAD - Get headers without body
url = 'https://www.google.com'

response = requests.head(url)
print(response.headers)
print(f"Content Length: {response.headers.get('Content-Length')}")
```

**Use Cases:**
- Check if resource exists
- Get file size before downloading
- Check last modified date

---

# REQUEST PARAMETERS

## 1) Query Parameters

### URL Parameters

```python
import requests

# Query parameters
url = 'https://api.github.com/search/repositories'

params = {
    'q': 'machine learning',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 10,
    'page': 1
}

response = requests.get(url, params=params)

# Final URL: https://api.github.com/search/repositories?q=machine+learning&sort=stars&order=desc&per_page=10&page=1
print(response.url)
```

---

### Dynamic Parameters

```python
import requests

def search_github(query, sort_by='stars', per_page=10):
    """Search GitHub repositories"""
    url = 'https://api.github.com/search/repositories'
    
    params = {
        'q': query,
        'sort': sort_by,
        'per_page': per_page
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()['items']
    return []

# Usage
repos = search_github('python', sort_by='stars', per_page=5)
for repo in repos:
    print(f"{repo['name']}: {repo['stargazers_count']} stars")
```

---

## 2) Form Data

### Submit Form Data

```python
import requests

# Form data (like HTML form submission)
url = 'https://httpbin.org/post'

form_data = {
    'username': 'prerak',
    'password': 'secret',
    'remember_me': 'true'
}

response = requests.post(url, data=form_data)
print(response.json())
```

---

### File Upload with Form Data

```python
import requests

# Form data with file upload
url = 'https://httpbin.org/post'

data = {
    'user_id': '123',
    'description': 'Profile picture'
}

files = {
    'file': open('photo.jpg', 'rb')
}

response = requests.post(url, data=data, files=files)
print(response.status_code)
```

---

## 3) JSON Payload

### Send JSON Data

```python
import requests

# JSON payload
url = 'https://jsonplaceholder.typicode.com/posts'

payload = {
    'title': 'API Testing',
    'body': 'Testing JSON payload',
    'userId': 1,
    'tags': ['python', 'api'],
    'metadata': {
        'created_by': 'Prerak',
        'version': '1.0'
    }
}

response = requests.post(url, json=payload)
print(response.json())
```

---

# HEADERS AND AUTHENTICATION

## 1) Custom Headers

### Send Custom Headers

```python
import requests

# Custom headers
url = 'https://api.github.com'

headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'X-Custom-Header': 'custom-value'
}

response = requests.get(url, headers=headers)
print(response.json())
```

---

### Common Headers

```python
import requests

# Common headers configuration
headers = {
    # Identify your application
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    
    # Accept JSON response
    'Accept': 'application/json',
    
    # For POST/PUT with JSON
    'Content-Type': 'application/json',
    
    # Language preference
    'Accept-Language': 'en-US,en;q=0.9',
    
    # Referer (where request came from)
    'Referer': 'https://example.com',
}

response = requests.get('https://api.example.com', headers=headers)
```

---

## 2) Authentication

### Basic Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

# Method 1: Using auth parameter
response = requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', 'password')
)

# Method 2: Tuple shorthand (EASIER)
response = requests.get(
    'https://api.github.com/user',
    auth=('username', 'password')
)

print(response.json())
```

---

### Bearer Token Authentication

```python
import requests

# Bearer token (most common for APIs)
url = 'https://api.github.com/user'

token = 'ghp_your_github_token_here'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(url, headers=headers)
print(response.json())
```

---

### API Key Authentication

```python
import requests

# Method 1: API key in headers
url = 'https://api.example.com/data'

headers = {
    'X-API-Key': 'your_api_key_here'
}

response = requests.get(url, headers=headers)

# Method 2: API key in query parameters
params = {
    'api_key': 'your_api_key_here',
    'q': 'search term'
}

response = requests.get(url, params=params)
```

---

### OAuth 2.0 Authentication

```python
import requests

# OAuth 2.0 flow (simplified)
def get_oauth_token(client_id, client_secret):
    """Get OAuth access token"""
    url = 'https://oauth.example.com/token'
    
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        return response.json()['access_token']
    return None

def call_api_with_oauth(access_token):
    """Make API call with OAuth token"""
    url = 'https://api.example.com/data'
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

# Usage
token = get_oauth_token('client_id', 'client_secret')
data = call_api_with_oauth(token)
```

---

# HANDLING RESPONSES

## 1) Response Object

### Access Response Data

```python
import requests

response = requests.get('https://api.github.com')

# Status code
print(response.status_code)          # 200

# Response text (as string)
print(response.text)                 # Raw text

# Response content (as bytes)
print(response.content)              # Binary content

# Response headers
print(response.headers)              # Dictionary-like object

# Encoding
print(response.encoding)             # 'utf-8'

# URL
print(response.url)                  # Final URL (after redirects)

# Elapsed time
print(response.elapsed)              # Time taken
```

---

## 2) Status Codes

### Check Response Status

```python
import requests

response = requests.get('https://api.github.com/users/octocat')

# Check specific status
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found!")
elif response.status_code == 500:
    print("Server error!")

# Check if successful (200-299)
if response.ok:
    print("Request was successful")

# Raise exception for bad status
try:
    response.raise_for_status()
    print("Status is good")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
```

---

### Status Code Categories

| Code Range | Meaning | Common Codes |
|------------|---------|--------------|
| **1xx** | Informational | 100 Continue |
| **2xx** | Success | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved, 302 Found, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthorized, 404 Not Found |
| **5xx** | Server Error | 500 Internal Error, 503 Service Unavailable |

```python
import requests

def handle_response(response):
    """Handle different status codes"""
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 201:
        return {'message': 'Created successfully'}
    elif response.status_code == 400:
        return {'error': 'Bad request'}
    elif response.status_code == 401:
        return {'error': 'Unauthorized - check credentials'}
    elif response.status_code == 404:
        return {'error': 'Resource not found'}
    elif response.status_code == 429:
        return {'error': 'Rate limit exceeded'}
    elif response.status_code >= 500:
        return {'error': 'Server error - try again later'}
    else:
        return {'error': f'Unexpected status: {response.status_code}'}
```

---

## 3) Response Headers

### Read Response Headers

```python
import requests

response = requests.get('https://api.github.com')

# Access all headers
print(response.headers)

# Access specific header
print(response.headers['Content-Type'])
print(response.headers.get('X-RateLimit-Remaining'))

# Common headers to check
print(f"Content Type: {response.headers.get('Content-Type')}")
print(f"Content Length: {response.headers.get('Content-Length')}")
print(f"Date: {response.headers.get('Date')}")
print(f"Server: {response.headers.get('Server')}")
```

---

### Rate Limit Headers

```python
import requests

def check_rate_limit(response):
    """Check API rate limit from headers"""
    limit = response.headers.get('X-RateLimit-Limit')
    remaining = response.headers.get('X-RateLimit-Remaining')
    reset = response.headers.get('X-RateLimit-Reset')
    
    if limit and remaining:
        print(f"Rate Limit: {remaining}/{limit} remaining")
        
        if int(remaining) < 10:
            print("Warning: Low rate limit!")
    
    return {
        'limit': limit,
        'remaining': remaining,
        'reset': reset
    }

# Usage
response = requests.get('https://api.github.com')
rate_info = check_rate_limit(response)
```

---

# WORKING WITH JSON

## 1) Parse JSON Response

### Get JSON Data

```python
import requests

# GET request returning JSON
response = requests.get('https://api.github.com/users/octocat')

# Parse JSON
data = response.json()

# Access data
print(data['name'])
print(data['followers'])
print(data['public_repos'])

# Pretty print
import json
print(json.dumps(data, indent=2))
```

---

### Handle JSON Errors

```python
import requests

response = requests.get('https://api.github.com/users/octocat')

try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")
    print(response.text)
```

---

## 2) Send JSON Data

### POST JSON

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# Python dictionary
data = {
    'title': 'My Post',
    'body': 'Content here',
    'userId': 1
}

# Automatically converted to JSON
response = requests.post(url, json=data)

# Response as JSON
result = response.json()
print(result)
```

---

## 3) Working with Complex JSON

### Nested JSON Data

```python
import requests

# Complex nested JSON
url = 'https://api.github.com/repos/python/cpython'
response = requests.get(url)
data = response.json()

# Navigate nested structure
print(f"Name: {data['name']}")
print(f"Owner: {data['owner']['login']}")
print(f"Stars: {data['stargazers_count']}")
print(f"License: {data['license']['name']}")

# Extract specific data
repo_info = {
    'name': data['name'],
    'description': data['description'],
    'stars': data['stargazers_count'],
    'forks': data['forks_count'],
    'owner': data['owner']['login'],
    'url': data['html_url']
}

print(repo_info)
```

---

# FILE OPERATIONS

## 1) Download Files

### Download Binary Files

```python
import requests

# Download image
url = 'https://www.python.org/static/img/python-logo.png'
response = requests.get(url)

# Save to file
with open('python-logo.png', 'wb') as f:
    f.write(response.content)

print("File downloaded successfully")
```

---

### Download Large Files (Streaming)

```python
import requests

def download_file(url, filename):
    """Download large file with progress"""
    response = requests.get(url, stream=True)
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                
                # Show progress
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"Downloaded: {percent:.1f}%", end='\r')
    
    print(f"\nDownload complete: {filename}")

# Usage
download_file(
    'https://example.com/large-file.zip',
    'large-file.zip'
)
```

---

### Download with Progress Bar

```python
import requests
from tqdm import tqdm

def download_with_progress(url, filename):
    """Download file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))

# Usage (requires: pip install tqdm)
# download_with_progress('https://example.com/file.zip', 'file.zip')
```

---

## 2) Upload Files

### Upload Single File

```python
import requests

# Upload file
url = 'https://httpbin.org/post'

files = {
    'file': open('document.pdf', 'rb')
}

response = requests.post(url, files=files)
print(response.json())
```

---

### Upload Multiple Files

```python
import requests

url = 'https://httpbin.org/post'

# Multiple files
files = {
    'file1': open('image1.jpg', 'rb'),
    'file2': open('image2.jpg', 'rb'),
    'document': open('report.pdf', 'rb')
}

# With additional data
data = {
    'user_id': '123',
    'category': 'photos'
}

response = requests.post(url, files=files, data=data)
print(response.status_code)
```

---

### Upload with Custom Filename

```python
import requests

url = 'https://httpbin.org/post'

# Custom filename and content type
files = {
    'file': ('custom_name.jpg', open('photo.jpg', 'rb'), 'image/jpeg')
}

response = requests.post(url, files=files)
print(response.json())
```

---

## 3) Download Text Files

### Download and Parse

```python
import requests

# Download text file
url = 'https://raw.githubusercontent.com/user/repo/main/README.md'
response = requests.get(url)

# Get text content
content = response.text

# Save to file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

# Or process line by line
lines = content.split('\n')
for line in lines:
    print(line)
```

---

# SESSIONS AND COOKIES

## 1) Using Sessions

### Session Basics

```python
import requests

# Create session
session = requests.Session()

# Session persists cookies and headers
session.headers.update({
    'User-Agent': 'MyApp/1.0'
})

# First request
response1 = session.get('https://httpbin.org/cookies/set/session_id/12345')

# Second request - cookies automatically included
response2 = session.get('https://httpbin.org/cookies')
print(response2.json())

# Close session
session.close()
```

---

### Session Context Manager

```python
import requests

# Better: Use context manager
with requests.Session() as session:
    # Set default headers
    session.headers.update({
        'Authorization': 'Bearer token123'
    })
    
    # All requests in this session share headers and cookies
    response1 = session.get('https://api.example.com/user')
    response2 = session.get('https://api.example.com/posts')
    
    print(response1.json())
    print(response2.json())

# Session automatically closed
```

---

### Login Session Example

```python
import requests

def create_authenticated_session(username, password):
    """Create session with authentication"""
    session = requests.Session()
    
    # Login
    login_url = 'https://example.com/api/login'
    credentials = {
        'username': username,
        'password': password
    }
    
    response = session.post(login_url, json=credentials)
    
    if response.status_code == 200:
        print("Login successful")
        return session
    else:
        print("Login failed")
        return None

# Usage
session = create_authenticated_session('prerak', 'password123')

if session:
    # Now all requests are authenticated
    profile = session.get('https://example.com/api/profile')
    posts = session.get('https://example.com/api/posts')
    
    print(profile.json())
```

---

## 2) Working with Cookies

### Send Cookies

```python
import requests

# Send cookies with request
url = 'https://httpbin.org/cookies'

cookies = {
    'session_id': '12345',
    'user_id': '67890'
}

response = requests.get(url, cookies=cookies)
print(response.json())
```

---

### Access Response Cookies

```python
import requests

response = requests.get('https://httpbin.org/cookies/set/name/value')

# Access cookies
print(response.cookies)

# Get specific cookie
cookie_value = response.cookies.get('name')
print(cookie_value)

# Convert to dictionary
cookies_dict = response.cookies.get_dict()
print(cookies_dict)
```

---

### Cookie Jar

```python
import requests
from http.cookiejar import CookieJar

# Create cookie jar
jar = CookieJar()

# Use with requests
response = requests.get('https://httpbin.org/cookies/set/test/cookie', cookies=jar)

# Check cookies in jar
for cookie in jar:
    print(f"{cookie.name}: {cookie.value}")
```

---

# ERROR HANDLING

## 1) Exception Types

### Common Exceptions

```python
import requests
from requests.exceptions import (
    RequestException,
    HTTPError,
    ConnectionError,
    Timeout,
    TooManyRedirects
)

url = 'https://api.example.com/data'

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    
except HTTPError as e:
    # HTTP error (4xx, 5xx)
    print(f"HTTP Error: {e}")
    
except ConnectionError:
    # Network problem
    print("Connection failed")
    
except Timeout:
    # Request timed out
    print("Request timed out")
    
except TooManyRedirects:
    # Too many redirects
    print("Too many redirects")
    
except RequestException as e:
    # Catch-all for requests errors
    print(f"Request failed: {e}")
```

---

## 2) Comprehensive Error Handling

### Robust Request Function

```python
import requests
from requests.exceptions import RequestException

def safe_request(url, method='GET', **kwargs):
    """Make request with comprehensive error handling"""
    
    try:
        # Make request
        if method.upper() == 'GET':
            response = requests.get(url, **kwargs)
        elif method.upper() == 'POST':
            response = requests.post(url, **kwargs)
        else:
            response = requests.request(method, url, **kwargs)
        
        # Check status
        response.raise_for_status()
        
        # Return JSON if available
        try:
            return {
                'success': True,
                'data': response.json(),
                'status_code': response.status_code
            }
        except ValueError:
            return {
                'success': True,
                'data': response.text,
                'status_code': response.status_code
            }
    
    except requests.exceptions.HTTPError as e:
        return {
            'success': False,
            'error': f'HTTP Error: {e}',
            'status_code': e.response.status_code if e.response else None
        }
    
    except requests.exceptions.ConnectionError:
        return {
            'success': False,
            'error': 'Connection failed - check your internet'
        }
    
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'error': 'Request timed out'
        }
    
    except RequestException as e:
        return {
            'success': False,
            'error': f'Request failed: {str(e)}'
        }

# Usage
result = safe_request('https://api.github.com/users/octocat')

if result['success']:
    print(result['data'])
else:
    print(f"Error: {result['error']}")
```

---

## 3) Retry Logic

### Retry on Failure

```python
import requests
import time

def request_with_retry(url, max_retries=3, delay=1):
    """Retry request on failure"""
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print(f"All {max_retries} attempts failed")
                raise

# Usage
try:
    response = request_with_retry('https://api.example.com/data')
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Final error: {e}")
```

---

# ADVANCED FEATURES

## 1) Timeouts

### Request Timeout

```python
import requests

# Timeout in seconds
try:
    # Single timeout value
    response = requests.get('https://api.github.com', timeout=5)
    
    # Separate connect and read timeouts
    response = requests.get(
        'https://api.github.com',
        timeout=(3, 10)  # (connect timeout, read timeout)
    )
    
    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out!")
```

**Best Practice:**  
Always set a timeout to prevent hanging requests.

---

## 2) Redirects

### Handle Redirects

```python
import requests

# Follow redirects (default)
response = requests.get('https://github.com')
print(f"Final URL: {response.url}")

# Don't follow redirects
response = requests.get('https://github.com', allow_redirects=False)
print(f"Status: {response.status_code}")

# Limit redirects
response = requests.get(
    'https://github.com',
    max_redirects=5
)
```

---

## 3) Proxies

### Use Proxy

```python
import requests

# HTTP proxy
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'http://proxy.example.com:8080',
}

response = requests.get('https://api.github.com', proxies=proxies)

# Proxy with authentication
proxies = {
    'http': 'http://user:pass@proxy.example.com:8080',
    'https': 'http://user:pass@proxy.example.com:8080',
}

response = requests.get('https://api.github.com', proxies=proxies)
```

---

## 4) SSL Verification

### SSL Certificate Handling

```python
import requests

# Verify SSL (default)
response = requests.get('https://api.github.com', verify=True)

# Disable SSL verification (NOT RECOMMENDED for production)
response = requests.get('https://example.com', verify=False)

# Use custom CA bundle
response = requests.get(
    'https://example.com',
    verify='/path/to/certfile'
)
```

**Warning:**  
Disabling SSL verification is a security risk. Only use for testing.

---

## 5) Custom Adapters

### HTTP Adapter

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Create session with retry strategy
session = requests.Session()

# Define retry strategy
retry_strategy = Retry(
    total=3,                      # Total retries
    backoff_factor=1,             # Wait 1, 2, 4 seconds
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)

# Mount adapter
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Now requests automatically retry
response = session.get('https://api.example.com/data')
```

---

# REAL-WORLD APPLICATIONS

## Application 1: REST API Client

### Complete API Client

```python
import requests
from typing import Optional, Dict, Any

class APIClient:
    """Generic REST API client"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'APIClient/1.0'
        })
        
        # Add API key if provided
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """GET request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """POST request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """PUT request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str) -> bool:
        """DELETE request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.status_code in [200, 204]
    
    def close(self):
        """Close session"""
        self.session.close()

# Usage
client = APIClient('https://jsonplaceholder.typicode.com', api_key='your_key')

# GET
posts = client.get('/posts', params={'userId': 1})
print(f"Found {len(posts)} posts")

# POST
new_post = client.post('/posts', data={
    'title': 'New Post',
    'body': 'Content here',
    'userId': 1
})
print(f"Created post with ID: {new_post['id']}")

# PUT
updated = client.put('/posts/1', data={'title': 'Updated Title'})

# DELETE
deleted = client.delete('/posts/1')
print(f"Deleted: {deleted}")

client.close()
```

---

## Application 2: Web Scraper

### Simple Web Scraper

```python
import requests
from bs4 import BeautifulSoup
import time

class WebScraper:
    """Simple web scraper"""
    
    def __init__(self, delay=1):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.delay = delay
    
    def get_page(self, url):
        """Get page content"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_html(self, html):
        """Parse HTML with BeautifulSoup"""
        return BeautifulSoup(html, 'html.parser')
    
    def scrape_links(self, url):
        """Extract all links from page"""
        html = self.get_page(url)
        if not html:
            return []
        
        soup = self.parse_html(html)
        links = []
        
        for link in soup.find_all('a', href=True):
            links.append(link['href'])
        
        return links
    
    def scrape_with_delay(self, urls):
        """Scrape multiple URLs with delay"""
        results = []
        
        for url in urls:
            print(f"Scraping: {url}")
            html = self.get_page(url)
            
            if html:
                results.append({
                    'url': url,
                    'content': html
                })
            
            time.sleep(self.delay)  # Be polite
        
        return results

# Usage (requires: pip install beautifulsoup4)
# scraper = WebScraper(delay=2)
# links = scraper.scrape_links('https://example.com')
# print(f"Found {len(links)} links")
```

---

## Application 3: File Downloader

### Batch File Downloader

```python
import requests
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

class FileDownloader:
    """Batch file downloader"""
    
    def __init__(self, download_dir='downloads'):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
    
    def download_file(self, url, filename=None):
        """Download single file"""
        if not filename:
            filename = url.split('/')[-1]
        
        filepath = self.download_dir / filename
        
        try:
            print(f"Downloading: {filename}")
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            print(f"{filename}: {percent:.1f}%", end='\r')
            
            print(f"\n{filename}: Complete")
            return str(filepath)
        
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
            return None
    
    def download_multiple(self, urls, max_workers=3):
        """Download multiple files concurrently"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.download_file, urls))
        
        successful = [r for r in results if r is not None]
        print(f"\nDownloaded {len(successful)}/{len(urls)} files")
        return successful

# Usage
downloader = FileDownloader('my_downloads')

# Single file
# downloader.download_file('https://example.com/file.pdf')

# Multiple files
urls = [
    'https://example.com/file1.pdf',
    'https://example.com/file2.pdf',
    'https://example.com/file3.pdf',
]
# downloader.download_multiple(urls, max_workers=3)
```

---

## Application 4: API Rate Limiter

### Rate-Limited API Client

```python
import requests
import time
from collections import deque

class RateLimitedAPI:
    """API client with rate limiting"""
    
    def __init__(self, base_url, calls_per_second=2):
        self.base_url = base_url
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0
        self.session = requests.Session()
    
    def _wait_if_needed(self):
        """Wait if necessary to respect rate limit"""
        current_time = time.time()
        time_since_last = current_time - self.last_call
        
        if time_since_last < self.min_interval:
            sleep_time = self.min_interval - time_since_last
            print(f"Rate limiting: sleeping {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        self.last_call = time.time()
    
    def get(self, endpoint, **kwargs):
        """Rate-limited GET request"""
        self._wait_if_needed()
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.get(url, **kwargs)
    
    def post(self, endpoint, **kwargs):
        """Rate-limited POST request"""
        self._wait_if_needed()
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.post(url, **kwargs)

# Usage
api = RateLimitedAPI('https://api.example.com', calls_per_second=2)

# These requests will be automatically rate-limited
for i in range(10):
    response = api.get(f'/posts/{i}')
    print(f"Request {i}: {response.status_code}")
```

---

## Application 5: Multi-Source Data Aggregator

### Aggregate Data from Multiple APIs

```python
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

class DataAggregator:
    """Fetch and aggregate data from multiple sources"""
    
    def __init__(self):
        self.session = requests.Session()
    
    def fetch_source(self, source_config):
        """Fetch data from a single source"""
        try:
            response = self.session.get(
                source_config['url'],
                params=source_config.get('params'),
                headers=source_config.get('headers'),
                timeout=10
            )
            response.raise_for_status()
            
            return {
                'source': source_config['name'],
                'data': response.json(),
                'success': True
            }
        
        except Exception as e:
            return {
                'source': source_config['name'],
                'error': str(e),
                'success': False
            }
    
    def aggregate(self, sources, max_workers=5):
        """Fetch data from multiple sources concurrently"""
        results = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_source = {
                executor.submit(self.fetch_source, source): source
                for source in sources
            }
            
            # Collect results as they complete
            for future in as_completed(future_to_source):
                result = future.result()
                results.append(result)
                
                if result['success']:
                    print(f"✓ {result['source']}: Success")
                else:
                    print(f"✗ {result['source']}: {result['error']}")
        
        return results

# Usage
aggregator = DataAggregator()

sources = [
    {
        'name': 'GitHub User',
        'url': 'https://api.github.com/users/octocat'
    },
    {
        'name': 'JSONPlaceholder Posts',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'params': {'userId': 1}
    },
    {
        'name': 'Public APIs',
        'url': 'https://api.publicapis.org/entries',
        'params': {'category': 'animals'}
    }
]

results = aggregator.aggregate(sources, max_workers=3)

# Process results
for result in results:
    if result['success']:
        print(f"\n{result['source']} data:")
        print(result['data'])
```

---

# BEST PRACTICES

## 1) Always Use Timeouts

```python
import requests

# ❌ BAD - No timeout (can hang forever)
response = requests.get('https://api.example.com')

# ✅ GOOD - Always set timeout
response = requests.get('https://api.example.com', timeout=10)

# ✅ BETTER - Separate connect and read timeouts
response = requests.get(
    'https://api.example.com',
    timeout=(3, 10)  # 3s connect, 10s read
)
```

---

## 2) Use Sessions for Multiple Requests

```python
import requests

# ❌ BAD - New connection each time
for i in range(100):
    response = requests.get(f'https://api.example.com/items/{i}')

# ✅ GOOD - Reuse connection
with requests.Session() as session:
    for i in range(100):
        response = session.get(f'https://api.example.com/items/{i}')
```

---

## 3) Handle Errors Properly

```python
import requests

# ✅ GOOD - Comprehensive error handling
try:
    response = requests.get('https://api.example.com', timeout=10)
    response.raise_for_status()
    data = response.json()
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## 4) Respect Rate Limits

```python
import requests
import time

# ✅ GOOD - Check and respect rate limits
def make_request_with_rate_limit(url):
    response = requests.get(url)
    
    # Check rate limit headers
    remaining = response.headers.get('X-RateLimit-Remaining')
    if remaining and int(remaining) < 10:
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        wait_time = reset_time - time.time()
        if wait_time > 0:
            print(f"Rate limit low, waiting {wait_time}s")
            time.sleep(wait_time)
    
    return response
```

---

## 5) Use Appropriate Headers

```python
import requests

# ✅ GOOD - Proper headers
headers = {
    'User-Agent': 'MyApp/1.0 (contact@example.com)',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get('https://api.example.com', headers=headers)
```

---

## 6) Secure API Keys

```python
import os
import requests

# ❌ BAD - Hardcoded API key
api_key = 'sk_live_abc123def456'

# ✅ GOOD - Use environment variables
api_key = os.environ.get('API_KEY')

# ✅ BETTER - Use .env file
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get('https://api.example.com', headers=headers)
```

---

## 7) Stream Large Responses

```python
import requests

# ❌ BAD - Load entire large file into memory
response = requests.get('https://example.com/large-file.zip')
with open('file.zip', 'wb') as f:
    f.write(response.content)

# ✅ GOOD - Stream large files
response = requests.get('https://example.com/large-file.zip', stream=True)
with open('file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
```

---

# QUICK REFERENCE CHEAT SHEET

## Essential Operations

```python
import requests

# Basic requests
response = requests.get('https://api.example.com')
response = requests.post('https://api.example.com', json=data)
response = requests.put('https://api.example.com/1', json=data)
response = requests.delete('https://api.example.com/1')

# With parameters
response = requests.get('https://api.example.com', params={'q': 'python'})

# With headers
response = requests.get('https://api.example.com', headers={'Authorization': 'Bearer token'})

# With timeout
response = requests.get('https://api.example.com', timeout=10)

# With authentication
response = requests.get('https://api.example.com', auth=('user', 'pass'))

# Check response
if response.ok:                    # Status 200-299
    data = response.json()         # Parse JSON
    print(response.status_code)    # Status code
    print(response.headers)        # Headers

# Error handling
response.raise_for_status()        # Raise exception for 4xx/5xx

# Sessions
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token'})
    r1 = session.get('https://api.example.com/user')
    r2 = session.get('https://api.example.com/posts')

# Download file
response = requests.get('https://example.com/file.pdf', stream=True)
with open('file.pdf', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# Upload file
files = {'file': open('document.pdf', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
```

---

# WHAT YOU'VE MASTERED

After completing these notes, you can:

✅ Make HTTP requests (GET, POST, PUT, DELETE, etc.)  
✅ Work with query parameters and headers  
✅ Handle authentication (Basic, Bearer, API keys, OAuth)  
✅ Parse and send JSON data  
✅ Download and upload files  
✅ Use sessions for persistent connections  
✅ Handle cookies properly  
✅ Implement comprehensive error handling  
✅ Add timeouts and retries  
✅ Build REST API clients  
✅ Create web scrapers  
✅ Implement rate limiting  
✅ Work with proxies and SSL  
✅ Build production-ready API integrations  

**You're ready to interact with any web API or service!**

---

# PRACTICE EXERCISES

## Beginner Level

1. Fetch data from a public API and display it
2. Download an image from a URL
3. Make a POST request to create data
4. Parse JSON response and extract specific fields
5. Handle 404 errors gracefully

## Intermediate Level

1. Build a weather app using a weather API
2. Create a GitHub repository searcher
3. Download multiple files concurrently
4. Implement retry logic with exponential backoff
5. Build a rate-limited API client

## Advanced Level

1. Create a complete REST API client with authentication
2. Build a web scraper with pagination support
3. Implement OAuth 2.0 authentication flow
4. Create a data aggregator from multiple APIs
5. Build an API monitoring and alerting system

---

**End of Requests Library Master Notes**

*Master HTTP requests, build powerful integrations!* 🌐