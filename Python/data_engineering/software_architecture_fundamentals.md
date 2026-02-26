# 🏗️ Software Architecture Fundamentals - Complete Guide

**Author:** Prerak  
**Purpose:** Master data pipeline architecture patterns (Collector → Parser → Processor → Storage)  
**Version:** 1.0 Complete

---

## 📋 TABLE OF CONTENTS

1. [Architecture Overview](#architecture-overview)
2. [Collector Component](#collector-component)
3. [Parser Component](#parser-component)
4. [Processor Component](#processor-component)
5. [Storage Component](#storage-component)
6. [Complete Pipeline Example](#complete-pipeline-example)
7. [Design Patterns](#design-patterns)
8. [Error Handling](#error-handling)
9. [Scalability and Performance](#scalability-and-performance)
10. [Best Practices](#best-practices)

---

## 1. Architecture Overview

### Data Pipeline Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│             │    │             │    │             │    │             │
│  COLLECTOR  │───▶│   PARSER    │───▶│  PROCESSOR  │───▶│   STORAGE   │
│             │    │             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                   │                   │                   │
     │                   │                   │                   │
     ▼                   ▼                   ▼                   ▼
Raw Data           Structured          Transformed         Persisted
(XML/JSON/API)     Python Objects      Data                Data
```

### Component Responsibilities

| Component | Input | Output | Responsibility |
|-----------|-------|--------|----------------|
| **Collector** | External sources | Raw data | Fetch and collect data |
| **Parser** | Raw data | Structured objects | Parse and validate |
| **Processor** | Structured objects | Transformed data | Business logic |
| **Storage** | Transformed data | Persisted data | Save and retrieve |

### Why This Architecture?

```
✓ Separation of Concerns - Each component has one job
✓ Testability - Easy to test each component independently
✓ Maintainability - Changes isolated to specific components
✓ Scalability - Can scale components independently
✓ Reusability - Components can be reused in different pipelines
✓ Flexibility - Easy to swap implementations
```

---

## 2. Collector Component

### Purpose

**Collector** is responsible for fetching raw data from external sources (APIs, files, databases, web scraping, etc.).

### Basic Collector Interface

```python
from abc import ABC, abstractmethod
from typing import Any, Optional

class DataCollector(ABC):
    """Abstract base class for data collectors"""
    
    @abstractmethod
    def collect(self) -> Any:
        """Collect data from source"""
        pass
    
    @abstractmethod
    def validate_source(self) -> bool:
        """Validate that source is accessible"""
        pass
```

### HTTP API Collector

```python
import requests
from typing import Dict, Optional
import logging

class APICollector(DataCollector):
    """Collect data from HTTP APIs"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        
        if api_key:
            self.session.headers['Authorization'] = f'Bearer {api_key}'
    
    def validate_source(self) -> bool:
        """Check if API is accessible"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except Exception as e:
            self.logger.error(f"Source validation failed: {e}")
            return False
    
    def collect(self, endpoint: str, params: Optional[Dict] = None) -> str:
        """Collect data from API endpoint"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            self.logger.info(f"Successfully collected data from {url}")
            return response.text
        
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to collect data: {e}")
            raise
    
    def collect_paginated(self, endpoint: str, page_size: int = 100):
        """Collect paginated data"""
        page = 1
        while True:
            params = {'page': page, 'limit': page_size}
            data = self.collect(endpoint, params)
            
            if not data or data == '[]':
                break
            
            yield data
            page += 1
    
    def close(self):
        """Close session"""
        self.session.close()

# Usage
collector = APICollector('https://api.example.com', api_key='your-key')

if collector.validate_source():
    # Collect single page
    raw_data = collector.collect('/users')
    
    # Collect all pages
    for page_data in collector.collect_paginated('/users'):
        print(f"Processing page: {len(page_data)} bytes")

collector.close()
```

### File Collector

```python
import os
from pathlib import Path
from typing import List

class FileCollector(DataCollector):
    """Collect data from files"""
    
    def __init__(self, directory: str, pattern: str = '*.xml'):
        self.directory = Path(directory)
        self.pattern = pattern
        self.logger = logging.getLogger(__name__)
    
    def validate_source(self) -> bool:
        """Check if directory exists and is accessible"""
        return self.directory.exists() and self.directory.is_dir()
    
    def collect(self) -> List[str]:
        """Collect all matching files"""
        if not self.validate_source():
            raise ValueError(f"Directory {self.directory} not accessible")
        
        files = list(self.directory.glob(self.pattern))
        self.logger.info(f"Found {len(files)} files matching {self.pattern}")
        
        return [str(f) for f in files]
    
    def collect_content(self, file_path: str) -> str:
        """Read file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.logger.info(f"Read {len(content)} bytes from {file_path}")
            return content
        
        except Exception as e:
            self.logger.error(f"Failed to read {file_path}: {e}")
            raise

# Usage
collector = FileCollector('./data', pattern='*.xml')

if collector.validate_source():
    files = collector.collect()
    
    for file_path in files:
        content = collector.collect_content(file_path)
        print(f"File: {file_path}, Size: {len(content)} bytes")
```

### Database Collector

```python
import sqlite3
from typing import List, Dict

class DatabaseCollector(DataCollector):
    """Collect data from database"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.logger = logging.getLogger(__name__)
    
    def validate_source(self) -> bool:
        """Check if database is accessible"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.close()
            return True
        except Exception as e:
            self.logger.error(f"Database validation failed: {e}")
            return False
    
    def connect(self):
        """Establish database connection"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
    
    def collect(self, query: str, params: tuple = ()) -> List[Dict]:
        """Execute query and collect results"""
        if not self.conn:
            self.connect()
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            
            rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            
            self.logger.info(f"Collected {len(result)} rows")
            return result
        
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            raise
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

# Usage
collector = DatabaseCollector('data.db')

if collector.validate_source():
    users = collector.collect('SELECT * FROM users WHERE active = ?', (1,))
    print(f"Found {len(users)} active users")

collector.close()
```

### Multi-Source Collector

```python
from typing import List, Dict, Any

class MultiSourceCollector:
    """Collect data from multiple sources"""
    
    def __init__(self):
        self.collectors: Dict[str, DataCollector] = {}
        self.logger = logging.getLogger(__name__)
    
    def add_collector(self, name: str, collector: DataCollector):
        """Add a collector"""
        self.collectors[name] = collector
    
    def validate_all(self) -> Dict[str, bool]:
        """Validate all sources"""
        results = {}
        for name, collector in self.collectors.items():
            results[name] = collector.validate_source()
        return results
    
    def collect_all(self) -> Dict[str, Any]:
        """Collect from all sources"""
        results = {}
        
        for name, collector in self.collectors.items():
            try:
                self.logger.info(f"Collecting from {name}")
                results[name] = collector.collect()
            except Exception as e:
                self.logger.error(f"Failed to collect from {name}: {e}")
                results[name] = None
        
        return results

# Usage
multi_collector = MultiSourceCollector()

multi_collector.add_collector('api', APICollector('https://api.example.com'))
multi_collector.add_collector('files', FileCollector('./data'))
multi_collector.add_collector('database', DatabaseCollector('data.db'))

# Validate all sources
validation = multi_collector.validate_all()
print(f"Source validation: {validation}")

# Collect from all sources
all_data = multi_collector.collect_all()
```

---

## 3. Parser Component

### Purpose

**Parser** converts raw data into structured Python objects, validates data integrity, and handles format conversion.

### Basic Parser Interface

```python
from abc import ABC, abstractmethod
from typing import Any, List

class DataParser(ABC):
    """Abstract base class for data parsers"""
    
    @abstractmethod
    def parse(self, raw_data: str) -> Any:
        """Parse raw data into structured format"""
        pass
    
    @abstractmethod
    def validate(self, parsed_data: Any) -> bool:
        """Validate parsed data"""
        pass
```

### XML Parser

```python
import xml.etree.ElementTree as ET
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Book:
    """Book data model"""
    id: str
    title: str
    author: str
    year: int
    price: float
    category: str = None

class XMLParser(DataParser):
    """Parse XML data into Python objects"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def parse(self, raw_data: str) -> List[Book]:
        """Parse XML string to Book objects"""
        try:
            root = ET.fromstring(raw_data)
            books = []
            
            for book_elem in root.findall('.//book'):
                book = self._parse_book(book_elem)
                if book:
                    books.append(book)
            
            self.logger.info(f"Parsed {len(books)} books")
            return books
        
        except ET.ParseError as e:
            self.logger.error(f"XML parse error: {e}")
            raise
    
    def _parse_book(self, element: ET.Element) -> Book:
        """Parse single book element"""
        try:
            return Book(
                id=element.get('id'),
                title=element.find('title').text,
                author=element.find('author').text,
                year=int(element.find('year').text),
                price=float(element.find('price').text),
                category=element.get('category')
            )
        except (AttributeError, ValueError) as e:
            self.logger.warning(f"Failed to parse book: {e}")
            return None
    
    def validate(self, books: List[Book]) -> bool:
        """Validate parsed books"""
        if not books:
            return False
        
        for book in books:
            if not book.id or not book.title or not book.author:
                self.logger.error(f"Invalid book: {book}")
                return False
            
            if book.year < 1900 or book.year > 2100:
                self.logger.error(f"Invalid year: {book.year}")
                return False
            
            if book.price < 0:
                self.logger.error(f"Invalid price: {book.price}")
                return False
        
        return True

# Usage
xml_data = '''<?xml version="1.0"?>
<library>
    <book id="001" category="programming">
        <title>Python Basics</title>
        <author>John Doe</author>
        <year>2023</year>
        <price>29.99</price>
    </book>
</library>'''

parser = XMLParser()
books = parser.parse(xml_data)

if parser.validate(books):
    for book in books:
        print(f"{book.title} by {book.author} - ${book.price}")
```

### JSON Parser

```python
import json
from typing import Dict, List

class JSONParser(DataParser):
    """Parse JSON data into Python objects"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def parse(self, raw_data: str) -> List[Dict]:
        """Parse JSON string"""
        try:
            data = json.loads(raw_data)
            
            # Handle both single object and array
            if isinstance(data, dict):
                data = [data]
            
            self.logger.info(f"Parsed {len(data)} records")
            return data
        
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON parse error: {e}")
            raise
    
    def validate(self, data: List[Dict]) -> bool:
        """Validate parsed data"""
        if not data:
            return False
        
        required_fields = ['id', 'name']
        
        for record in data:
            if not all(field in record for field in required_fields):
                self.logger.error(f"Missing required fields in: {record}")
                return False
        
        return True

# Usage
json_data = '''[
    {"id": 1, "name": "Item 1", "value": 100},
    {"id": 2, "name": "Item 2", "value": 200}
]'''

parser = JSONParser()
data = parser.parse(json_data)

if parser.validate(data):
    print(f"Successfully parsed and validated {len(data)} records")
```

### XML to Dictionary Parser

```python
class XMLToDictParser(DataParser):
    """Parse XML to dictionary"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def parse(self, raw_data: str) -> Dict:
        """Parse XML to nested dictionary"""
        try:
            root = ET.fromstring(raw_data)
            result = self._element_to_dict(root)
            
            self.logger.info("Converted XML to dictionary")
            return result
        
        except ET.ParseError as e:
            self.logger.error(f"XML parse error: {e}")
            raise
    
    def _element_to_dict(self, element: ET.Element) -> Dict:
        """Recursively convert element to dictionary"""
        result = {
            'tag': element.tag,
            'attributes': element.attrib
        }
        
        # Add text content
        if element.text and element.text.strip():
            result['text'] = element.text.strip()
        
        # Add children
        children = {}
        for child in element:
            child_dict = self._element_to_dict(child)
            
            if child.tag in children:
                if not isinstance(children[child.tag], list):
                    children[child.tag] = [children[child.tag]]
                children[child.tag].append(child_dict)
            else:
                children[child.tag] = child_dict
        
        if children:
            result['children'] = children
        
        return result
    
    def validate(self, data: Dict) -> bool:
        """Validate dictionary structure"""
        return 'tag' in data and 'attributes' in data

# Usage
xml_data = '''<library>
    <book id="001"><title>Python</title></book>
</library>'''

parser = XMLToDictParser()
dict_data = parser.parse(xml_data)

import json
print(json.dumps(dict_data, indent=2))
```

---

## 4. Processor Component

### Purpose

**Processor** applies business logic, transforms data, enriches information, and prepares data for storage.

### Basic Processor Interface

```python
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    """Abstract base class for data processors"""
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process data"""
        pass
    
    @abstractmethod
    def enrich(self, data: Any) -> Any:
        """Enrich data with additional information"""
        pass
```

### Book Processor

```python
from datetime import datetime
from typing import List

class BookProcessor(DataProcessor):
    """Process book data"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.exchange_rate = 1.0  # USD to local currency
    
    def process(self, books: List[Book]) -> List[Dict]:
        """Process books and return transformed data"""
        processed = []
        
        for book in books:
            # Transform book to dictionary
            book_dict = self._transform_book(book)
            
            # Enrich with additional data
            book_dict = self.enrich(book_dict)
            
            processed.append(book_dict)
        
        self.logger.info(f"Processed {len(processed)} books")
        return processed
    
    def _transform_book(self, book: Book) -> Dict:
        """Transform Book object to dictionary"""
        return {
            'book_id': book.id,
            'title': book.title.upper(),  # Normalize to uppercase
            'author': book.author,
            'publication_year': book.year,
            'price_usd': book.price,
            'category': book.category or 'uncategorized',
            'processed_at': datetime.now().isoformat()
        }
    
    def enrich(self, book_dict: Dict) -> Dict:
        """Enrich book data"""
        # Add local price
        book_dict['price_local'] = book_dict['price_usd'] * self.exchange_rate
        
        # Add age category
        current_year = datetime.now().year
        age = current_year - book_dict['publication_year']
        
        if age < 1:
            book_dict['age_category'] = 'new'
        elif age < 5:
            book_dict['age_category'] = 'recent'
        else:
            book_dict['age_category'] = 'classic'
        
        # Add price category
        if book_dict['price_usd'] < 20:
            book_dict['price_category'] = 'budget'
        elif book_dict['price_usd'] < 50:
            book_dict['price_category'] = 'standard'
        else:
            book_dict['price_category'] = 'premium'
        
        return book_dict
    
    def filter_books(self, books: List[Dict], criteria: Dict) -> List[Dict]:
        """Filter books based on criteria"""
        filtered = books
        
        if 'min_price' in criteria:
            filtered = [b for b in filtered if b['price_usd'] >= criteria['min_price']]
        
        if 'max_price' in criteria:
            filtered = [b for b in filtered if b['price_usd'] <= criteria['max_price']]
        
        if 'category' in criteria:
            filtered = [b for b in filtered if b['category'] == criteria['category']]
        
        self.logger.info(f"Filtered to {len(filtered)} books")
        return filtered
    
    def aggregate_stats(self, books: List[Dict]) -> Dict:
        """Calculate aggregate statistics"""
        if not books:
            return {}
        
        prices = [b['price_usd'] for b in books]
        
        return {
            'total_books': len(books),
            'avg_price': sum(prices) / len(prices),
            'min_price': min(prices),
            'max_price': max(prices),
            'categories': list(set(b['category'] for b in books)),
            'category_counts': self._count_by_category(books)
        }
    
    def _count_by_category(self, books: List[Dict]) -> Dict[str, int]:
        """Count books by category"""
        counts = {}
        for book in books:
            category = book['category']
            counts[category] = counts.get(category, 0) + 1
        return counts

# Usage
books = [
    Book('001', 'Python Basics', 'John Doe', 2023, 29.99, 'programming'),
    Book('002', 'Java Advanced', 'Jane Smith', 2020, 49.99, 'programming')
]

processor = BookProcessor()
processed_books = processor.process(books)

# Filter books
filtered = processor.filter_books(processed_books, {'min_price': 30})

# Get statistics
stats = processor.aggregate_stats(processed_books)
print(f"Statistics: {stats}")
```

### Data Transformation Processor

```python
from typing import Callable, List, Dict

class TransformationProcessor(DataProcessor):
    """Apply transformations to data"""
    
    def __init__(self):
        self.transformations: List[Callable] = []
        self.logger = logging.getLogger(__name__)
    
    def add_transformation(self, func: Callable):
        """Add a transformation function"""
        self.transformations.append(func)
    
    def process(self, data: List[Dict]) -> List[Dict]:
        """Apply all transformations"""
        result = data
        
        for transform in self.transformations:
            result = [transform(item) for item in result]
            self.logger.info(f"Applied transformation: {transform.__name__}")
        
        return result
    
    def enrich(self, data: List[Dict]) -> List[Dict]:
        """Enrich data"""
        return data

# Define transformation functions
def normalize_names(item: Dict) -> Dict:
    """Normalize name fields to title case"""
    if 'name' in item:
        item['name'] = item['name'].title()
    return item

def add_timestamp(item: Dict) -> Dict:
    """Add processing timestamp"""
    item['processed_at'] = datetime.now().isoformat()
    return item

def calculate_discount(item: Dict) -> Dict:
    """Calculate discounted price"""
    if 'price' in item:
        item['original_price'] = item['price']
        item['discounted_price'] = item['price'] * 0.9  # 10% discount
    return item

# Usage
processor = TransformationProcessor()
processor.add_transformation(normalize_names)
processor.add_transformation(add_timestamp)
processor.add_transformation(calculate_discount)

data = [
    {'name': 'john doe', 'price': 100},
    {'name': 'jane smith', 'price': 200}
]

processed = processor.process(data)
print(processed)
```

---

## 5. Storage Component

### Purpose

**Storage** persists processed data to databases, files, or external systems.

### Basic Storage Interface

```python
from abc import ABC, abstractmethod
from typing import Any, List

class DataStorage(ABC):
    """Abstract base class for data storage"""
    
    @abstractmethod
    def save(self, data: Any) -> bool:
        """Save data"""
        pass
    
    @abstractmethod
    def load(self, identifier: str) -> Any:
        """Load data"""
        pass
    
    @abstractmethod
    def delete(self, identifier: str) -> bool:
        """Delete data"""
        pass
```

### Database Storage

```python
import sqlite3
from typing import List, Dict, Optional

class DatabaseStorage(DataStorage):
    """Store data in SQLite database"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.logger = logging.getLogger(__name__)
        self._initialize_db()
    
    def _initialize_db(self):
        """Create tables if they don't exist"""
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER,
                price_usd REAL,
                price_local REAL,
                category TEXT,
                age_category TEXT,
                price_category TEXT,
                processed_at TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()
        self.logger.info("Database initialized")
    
    def save(self, books: List[Dict]) -> bool:
        """Save books to database"""
        try:
            cursor = self.conn.cursor()
            
            for book in books:
                cursor.execute('''
                    INSERT OR REPLACE INTO books 
                    (book_id, title, author, publication_year, price_usd, 
                     price_local, category, age_category, price_category, processed_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    book['book_id'],
                    book['title'],
                    book['author'],
                    book['publication_year'],
                    book['price_usd'],
                    book['price_local'],
                    book['category'],
                    book['age_category'],
                    book['price_category'],
                    book['processed_at']
                ))
            
            self.conn.commit()
            self.logger.info(f"Saved {len(books)} books to database")
            return True
        
        except sqlite3.Error as e:
            self.logger.error(f"Database error: {e}")
            self.conn.rollback()
            return False
    
    def load(self, book_id: str) -> Optional[Dict]:
        """Load book by ID"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
        
        row = cursor.fetchone()
        if row:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, row))
        
        return None
    
    def load_all(self, filters: Optional[Dict] = None) -> List[Dict]:
        """Load all books with optional filters"""
        query = 'SELECT * FROM books'
        params = []
        
        if filters:
            conditions = []
            if 'category' in filters:
                conditions.append('category = ?')
                params.append(filters['category'])
            if 'min_price' in filters:
                conditions.append('price_usd >= ?')
                params.append(filters['min_price'])
            
            if conditions:
                query += ' WHERE ' + ' AND '.join(conditions)
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def delete(self, book_id: str) -> bool:
        """Delete book by ID"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
            self.conn.commit()
            
            self.logger.info(f"Deleted book {book_id}")
            return cursor.rowcount > 0
        
        except sqlite3.Error as e:
            self.logger.error(f"Delete error: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

# Usage
storage = DatabaseStorage('books.db')

# Save processed books
books_to_save = [
    {
        'book_id': '001',
        'title': 'PYTHON BASICS',
        'author': 'John Doe',
        'publication_year': 2023,
        'price_usd': 29.99,
        'price_local': 29.99,
        'category': 'programming',
        'age_category': 'new',
        'price_category': 'standard',
        'processed_at': '2023-12-01T10:00:00'
    }
]

if storage.save(books_to_save):
    print("Books saved successfully")

# Load book
book = storage.load('001')
print(f"Loaded book: {book['title']}")

# Load all programming books
programming_books = storage.load_all({'category': 'programming'})
print(f"Found {len(programming_books)} programming books")

storage.close()
```

### File Storage

```python
import json
from pathlib import Path

class FileStorage(DataStorage):
    """Store data in files"""
    
    def __init__(self, directory: str, format: str = 'json'):
        self.directory = Path(directory)
        self.format = format
        self.logger = logging.getLogger(__name__)
        
        # Create directory if it doesn't exist
        self.directory.mkdir(parents=True, exist_ok=True)
    
    def save(self, data: List[Dict], filename: str = None) -> bool:
        """Save data to file"""
        if not filename:
            filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{self.format}"
        
        filepath = self.directory / filename
        
        try:
            if self.format == 'json':
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)
            else:
                with open(filepath, 'w') as f:
                    f.write(str(data))
            
            self.logger.info(f"Saved data to {filepath}")
            return True
        
        except Exception as e:
            self.logger.error(f"Failed to save: {e}")
            return False
    
    def load(self, filename: str) -> Any:
        """Load data from file"""
        filepath = self.directory / filename
        
        try:
            if self.format == 'json':
                with open(filepath, 'r') as f:
                    return json.load(f)
            else:
                with open(filepath, 'r') as f:
                    return f.read()
        
        except Exception as e:
            self.logger.error(f"Failed to load: {e}")
            return None
    
    def delete(self, filename: str) -> bool:
        """Delete file"""
        filepath = self.directory / filename
        
        try:
            filepath.unlink()
            self.logger.info(f"Deleted {filepath}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to delete: {e}")
            return False
    
    def list_files(self) -> List[str]:
        """List all files in directory"""
        return [f.name for f in self.directory.glob(f'*.{self.format}')]

# Usage
storage = FileStorage('./output', format='json')

# Save data
data = [{'id': 1, 'name': 'Item 1'}]
storage.save(data, 'items.json')

# Load data
loaded_data = storage.load('items.json')
print(loaded_data)

# List all files
files = storage.list_files()
print(f"Files: {files}")
```

---

## 6. Complete Pipeline Example

### Full Data Pipeline

```python
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class DataPipeline:
    """Complete data processing pipeline"""
    
    def __init__(
        self,
        collector: DataCollector,
        parser: DataParser,
        processor: DataProcessor,
        storage: DataStorage
    ):
        self.collector = collector
        self.parser = parser
        self.processor = processor
        self.storage = storage
        self.logger = logging.getLogger(__name__)
    
    def run(self, **collector_kwargs) -> Dict:
        """Execute complete pipeline"""
        stats = {
            'collected': 0,
            'parsed': 0,
            'processed': 0,
            'stored': 0,
            'errors': []
        }
        
        try:
            # Step 1: Collect raw data
            self.logger.info("Step 1: Collecting data...")
            if not self.collector.validate_source():
                raise ValueError("Data source validation failed")
            
            raw_data = self.collector.collect(**collector_kwargs)
            stats['collected'] = len(raw_data) if isinstance(raw_data, (list, str)) else 1
            self.logger.info(f"Collected {stats['collected']} items")
            
            # Step 2: Parse data
            self.logger.info("Step 2: Parsing data...")
            parsed_data = self.parser.parse(raw_data)
            
            if not self.parser.validate(parsed_data):
                raise ValueError("Data validation failed")
            
            stats['parsed'] = len(parsed_data)
            self.logger.info(f"Parsed {stats['parsed']} items")
            
            # Step 3: Process data
            self.logger.info("Step 3: Processing data...")
            processed_data = self.processor.process(parsed_data)
            stats['processed'] = len(processed_data)
            self.logger.info(f"Processed {stats['processed']} items")
            
            # Step 4: Store data
            self.logger.info("Step 4: Storing data...")
            if self.storage.save(processed_data):
                stats['stored'] = len(processed_data)
                self.logger.info(f"Stored {stats['stored']} items")
            else:
                raise ValueError("Storage failed")
            
            self.logger.info("Pipeline completed successfully")
            
        except Exception as e:
            self.logger.error(f"Pipeline error: {e}")
            stats['errors'].append(str(e))
        
        return stats

# Complete pipeline usage
def main():
    # Initialize components
    collector = APICollector('https://api.example.com/books')
    parser = XMLParser()
    processor = BookProcessor()
    storage = DatabaseStorage('books.db')
    
    # Create pipeline
    pipeline = DataPipeline(collector, parser, processor, storage)
    
    # Run pipeline
    results = pipeline.run(endpoint='/api/books')
    
    # Print results
    print("\nPipeline Results:")
    print(f"  Collected: {results['collected']}")
    print(f"  Parsed: {results['parsed']}")
    print(f"  Processed: {results['processed']}")
    print(f"  Stored: {results['stored']}")
    
    if results['errors']:
        print(f"  Errors: {results['errors']}")
    
    # Cleanup
    storage.close()

if __name__ == '__main__':
    main()
```

### Pipeline with Error Recovery

```python
class RobustDataPipeline(DataPipeline):
    """Pipeline with error recovery and retry logic"""
    
    def __init__(self, collector, parser, processor, storage, max_retries=3):
        super().__init__(collector, parser, processor, storage)
        self.max_retries = max_retries
    
    def run_with_retry(self, **collector_kwargs) -> Dict:
        """Run pipeline with retry logic"""
        attempt = 0
        
        while attempt < self.max_retries:
            try:
                return self.run(**collector_kwargs)
            
            except Exception as e:
                attempt += 1
                self.logger.warning(f"Attempt {attempt} failed: {e}")
                
                if attempt >= self.max_retries:
                    self.logger.error("Max retries reached, giving up")
                    return {'errors': [f"Failed after {attempt} attempts"]}
                
                # Wait before retry
                import time
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def run_partial(self, **collector_kwargs) -> Dict:
        """Run pipeline, skip failed items"""
        stats = {
            'collected': 0,
            'parsed': 0,
            'processed': 0,
            'stored': 0,
            'skipped': 0,
            'errors': []
        }
        
        try:
            # Collect
            raw_data = self.collector.collect(**collector_kwargs)
            stats['collected'] = 1
            
            # Parse with error handling
            try:
                parsed_data = self.parser.parse(raw_data)
                stats['parsed'] = len(parsed_data)
            except Exception as e:
                self.logger.error(f"Parse error: {e}")
                stats['errors'].append(str(e))
                return stats
            
            # Process each item individually
            processed_items = []
            for item in parsed_data:
                try:
                    processed = self.processor.process([item])
                    processed_items.extend(processed)
                    stats['processed'] += 1
                except Exception as e:
                    self.logger.warning(f"Skipping item due to error: {e}")
                    stats['skipped'] += 1
            
            # Store successfully processed items
            if processed_items:
                if self.storage.save(processed_items):
                    stats['stored'] = len(processed_items)
        
        except Exception as e:
            stats['errors'].append(str(e))
        
        return stats
```

---

## 7. Design Patterns

### Pipeline Pattern

```python
from typing import Callable, List, Any

class Pipeline:
    """Generic pipeline pattern"""
    
    def __init__(self):
        self.stages: List[Callable] = []
    
    def add_stage(self, func: Callable, name: str = None):
        """Add processing stage"""
        func.stage_name = name or func.__name__
        self.stages.append(func)
        return self
    
    def execute(self, initial_data: Any) -> Any:
        """Execute all pipeline stages"""
        data = initial_data
        
        for stage in self.stages:
            print(f"Executing: {stage.stage_name}")
            data = stage(data)
        
        return data

# Usage
pipeline = Pipeline()

pipeline.add_stage(lambda x: x.upper(), "Uppercase")
pipeline.add_stage(lambda x: x.replace(' ', '_'), "Remove Spaces")
pipeline.add_stage(lambda x: f"processed_{x}", "Add Prefix")

result = pipeline.execute("hello world")
print(result)  # processed_HELLO_WORLD
```

### Factory Pattern

```python
from typing import Dict, Type

class ComponentFactory:
    """Factory for creating pipeline components"""
    
    def __init__(self):
        self._collectors: Dict[str, Type] = {}
        self._parsers: Dict[str, Type] = {}
        self._processors: Dict[str, Type] = {}
        self._storages: Dict[str, Type] = {}
    
    def register_collector(self, name: str, cls: Type):
        self._collectors[name] = cls
    
    def register_parser(self, name: str, cls: Type):
        self._parsers[name] = cls
    
    def register_processor(self, name: str, cls: Type):
        self._processors[name] = cls
    
    def register_storage(self, name: str, cls: Type):
        self._storages[name] = cls
    
    def create_collector(self, name: str, **kwargs) -> DataCollector:
        if name not in self._collectors:
            raise ValueError(f"Unknown collector: {name}")
        return self._collectors[name](**kwargs)
    
    def create_parser(self, name: str, **kwargs) -> DataParser:
        if name not in self._parsers:
            raise ValueError(f"Unknown parser: {name}")
        return self._parsers[name](**kwargs)
    
    def create_processor(self, name: str, **kwargs) -> DataProcessor:
        if name not in self._processors:
            raise ValueError(f"Unknown processor: {name}")
        return self._processors[name](**kwargs)
    
    def create_storage(self, name: str, **kwargs) -> DataStorage:
        if name not in self._storages:
            raise ValueError(f"Unknown storage: {name}")
        return self._storages[name](**kwargs)

# Usage
factory = ComponentFactory()

# Register components
factory.register_collector('api', APICollector)
factory.register_parser('xml', XMLParser)
factory.register_processor('book', BookProcessor)
factory.register_storage('database', DatabaseStorage)

# Create pipeline from factory
collector = factory.create_collector('api', base_url='https://api.example.com')
parser = factory.create_parser('xml')
processor = factory.create_processor('book')
storage = factory.create_storage('database', db_path='books.db')

pipeline = DataPipeline(collector, parser, processor, storage)
```

---

## 8. Error Handling

### Comprehensive Error Handling

```python
class PipelineError(Exception):
    """Base exception for pipeline errors"""
    pass

class CollectionError(PipelineError):
    """Error during data collection"""
    pass

class ParsingError(PipelineError):
    """Error during data parsing"""
    pass

class ProcessingError(PipelineError):
    """Error during data processing"""
    pass

class StorageError(PipelineError):
    """Error during data storage"""
    pass

class SafeDataPipeline(DataPipeline):
    """Pipeline with comprehensive error handling"""
    
    def run(self, **collector_kwargs) -> Dict:
        stats = {
            'success': False,
            'stage': None,
            'collected': 0,
            'parsed': 0,
            'processed': 0,
            'stored': 0,
            'errors': []
        }
        
        try:
            # Collection
            stats['stage'] = 'collection'
            self._validate_component(self.collector, 'collector')
            
            raw_data = self.collector.collect(**collector_kwargs)
            stats['collected'] = 1
            self.logger.info("Collection successful")
            
            # Parsing
            stats['stage'] = 'parsing'
            self._validate_component(self.parser, 'parser')
            
            parsed_data = self.parser.parse(raw_data)
            if not self.parser.validate(parsed_data):
                raise ParsingError("Data validation failed")
            
            stats['parsed'] = len(parsed_data)
            self.logger.info("Parsing successful")
            
            # Processing
            stats['stage'] = 'processing'
            self._validate_component(self.processor, 'processor')
            
            processed_data = self.processor.process(parsed_data)
            stats['processed'] = len(processed_data)
            self.logger.info("Processing successful")
            
            # Storage
            stats['stage'] = 'storage'
            self._validate_component(self.storage, 'storage')
            
            if not self.storage.save(processed_data):
                raise StorageError("Failed to save data")
            
            stats['stored'] = len(processed_data)
            stats['success'] = True
            stats['stage'] = 'complete'
            self.logger.info("Pipeline completed successfully")
        
        except CollectionError as e:
            stats['errors'].append(f"Collection failed: {e}")
            self.logger.error(f"Collection error: {e}")
        
        except ParsingError as e:
            stats['errors'].append(f"Parsing failed: {e}")
            self.logger.error(f"Parsing error: {e}")
        
        except ProcessingError as e:
            stats['errors'].append(f"Processing failed: {e}")
            self.logger.error(f"Processing error: {e}")
        
        except StorageError as e:
            stats['errors'].append(f"Storage failed: {e}")
            self.logger.error(f"Storage error: {e}")
        
        except Exception as e:
            stats['errors'].append(f"Unexpected error: {e}")
            self.logger.error(f"Unexpected error in {stats['stage']}: {e}")
        
        return stats
    
    def _validate_component(self, component, name):
        """Validate component is properly initialized"""
        if component is None:
            raise ValueError(f"{name} is not initialized")
```

---

## 9. Scalability and Performance

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List

class ParallelPipeline(DataPipeline):
    """Pipeline with parallel processing"""
    
    def __init__(self, collector, parser, processor, storage, max_workers=4):
        super().__init__(collector, parser, processor, storage)
        self.max_workers = max_workers
    
    def process_parallel(self, parsed_data: List) -> List:
        """Process items in parallel"""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.processor.process, [item])
                for item in parsed_data
            ]
            
            results = []
            for future in futures:
                try:
                    result = future.result()
                    results.extend(result)
                except Exception as e:
                    self.logger.error(f"Parallel processing error: {e}")
            
            return results
```

### Batch Processing

```python
class BatchPipeline(DataPipeline):
    """Pipeline with batch processing"""
    
    def __init__(self, collector, parser, processor, storage, batch_size=100):
        super().__init__(collector, parser, processor, storage)
        self.batch_size = batch_size
    
    def run_batched(self, **collector_kwargs):
        """Process data in batches"""
        stats = {'total': 0, 'batches': 0, 'errors': []}
        
        # Collect and parse
        raw_data = self.collector.collect(**collector_kwargs)
        parsed_data = self.parser.parse(raw_data)
        
        # Process in batches
        for i in range(0, len(parsed_data), self.batch_size):
            batch = parsed_data[i:i + self.batch_size]
            
            try:
                processed = self.processor.process(batch)
                self.storage.save(processed)
                
                stats['total'] += len(processed)
                stats['batches'] += 1
                
            except Exception as e:
                self.logger.error(f"Batch {stats['batches']} failed: {e}")
                stats['errors'].append(str(e))
        
        return stats
```

---

## 10. Best Practices

### Configuration Management

```python
import yaml

class PipelineConfig:
    """Pipeline configuration"""
    
    @staticmethod
    def load_from_file(filepath: str) -> Dict:
        """Load configuration from YAML file"""
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    
    @staticmethod
    def create_pipeline_from_config(config: Dict) -> DataPipeline:
        """Create pipeline from configuration"""
        factory = ComponentFactory()
        
        # Register components (would be done at startup)
        factory.register_collector('api', APICollector)
        factory.register_parser('xml', XMLParser)
        factory.register_processor('book', BookProcessor)
        factory.register_storage('database', DatabaseStorage)
        
        # Create components from config
        collector = factory.create_collector(
            config['collector']['type'],
            **config['collector']['params']
        )
        
        parser = factory.create_parser(config['parser']['type'])
        processor = factory.create_processor(config['processor']['type'])
        
        storage = factory.create_storage(
            config['storage']['type'],
            **config['storage']['params']
        )
        
        return DataPipeline(collector, parser, processor, storage)

# config.yaml:
"""
collector:
  type: api
  params:
    base_url: https://api.example.com
    api_key: your-key

parser:
  type: xml

processor:
  type: book

storage:
  type: database
  params:
    db_path: books.db
"""
```

### Monitoring and Metrics

```python
from time import time
from typing import Dict

class MonitoredPipeline(DataPipeline):
    """Pipeline with monitoring"""
    
    def run(self, **collector_kwargs) -> Dict:
        metrics = {
            'start_time': time(),
            'stages': {}
        }
        
        # Collection
        start = time()
        raw_data = self.collector.collect(**collector_kwargs)
        metrics['stages']['collection'] = time() - start
        
        # Parsing
        start = time()
        parsed_data = self.parser.parse(raw_data)
        metrics['stages']['parsing'] = time() - start
        
        # Processing
        start = time()
        processed_data = self.processor.process(parsed_data)
        metrics['stages']['processing'] = time() - start
        
        # Storage
        start = time()
        self.storage.save(processed_data)
        metrics['stages']['storage'] = time() - start
        
        metrics['total_time'] = time() - metrics['start_time']
        
        # Log metrics
        self.logger.info(f"Pipeline metrics: {metrics}")
        
        return metrics
```

---

## 🎯 Architecture Summary

### Key Principles

```
1. Separation of Concerns
   - Each component has single responsibility
   
2. Interface-Based Design
   - Components implement abstract interfaces
   
3. Dependency Injection
   - Components are injected, not created internally
   
4. Error Handling
   - Comprehensive error handling at each stage
   
5. Logging
   - Detailed logging for debugging and monitoring
   
6. Testability
   - Each component can be tested independently
   
7. Scalability
   - Components can be parallelized or distributed
   
8. Configurability
   - Pipeline behavior controlled by configuration
```

---

**END OF SOFTWARE ARCHITECTURE FUNDAMENTALS**

*You now have a complete understanding of data pipeline architecture!*