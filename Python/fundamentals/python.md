# 🐍 Python Master Notes — From Basics to Advanced (Top 1% Track)

**Author:** Prerak  
**Purpose:** Build deep Python foundations with clarity, examples, and real-world thinking.  
**Version:** Complete Edition with Built-ins, OOP, File Handling, Dicts & Sets

---

## 🎯 FUNDAMENTAL CONCEPTS

---

## 1️⃣ Indentation (Code Blocks)

### Explanation
Python uses **indentation instead of curly braces `{}`** to define blocks of code.
Indentation is not cosmetic — it defines **program logic**.

Standard indentation in Python is **4 spaces per level** and is strictly enforced by the interpreter.

---

### Syntax
```python
if True:
    print("Inside if")
    print("Still inside")
print("Outside")
```

### Output
```
Inside if
Still inside
Outside
```

### Important Points
- Always use 4 spaces per level
- Never mix tabs and spaces (causes IndentationError)
- Wrong indentation = program breaks
- Use consistent indentation throughout your codebase
- Modern IDEs automatically handle indentation

---

## 2️⃣ Variables

### Explanation
Variables are **references to objects in memory**, not containers.
Python decides the data type at runtime (dynamic typing).

Variables don't store values directly; they store references to objects in memory.

---

### Syntax
```python
x = 10
x = "Python"
```

### Output
```
No error (type changes dynamically)
```

### Important Points
- Python is dynamically typed
- Variable names should be descriptive (use snake_case)
- Assignment binds name → object
- Multiple variables can reference the same object
- Use meaningful names: `user_count` not `uc`

### Memory and References (Advanced)
```python
# Variables are references
a = [1, 2, 3]
b = a  # b points to same object
b.append(4)
print(a)  # [1, 2, 3, 4] - both changed!

# Check if same object
print(id(a) == id(b))  # True

# Create independent copy
c = a.copy()
c.append(5)
print(a)  # [1, 2, 3, 4] - not affected
```

### Naming Conventions
- **snake_case**: variables, functions → `user_name`, `calculate_total()`
- **PascalCase**: classes → `UserAccount`, `DatabaseConnection`
- **UPPER_CASE**: constants → `MAX_SIZE`, `API_KEY`
- **_single_leading**: internal use → `_internal_method()`
- **__double_leading**: name mangling → `__private_attr`

---

## 3️⃣ Core Data Types

### Explanation
Data types define how data behaves in memory and what operations can be performed on it.

---

### Syntax
```python
a = 10          # int
b = 3.5         # float
c = "hello"     # str
d = True        # bool
e = None        # NoneType
```

### Example
```python
print(type(a))
print(type(c))
print(type(e))
```

### Output
```
<class 'int'>
<class 'str'>
<class 'NoneType'>
```

### Important Points
- Everything in Python is an object
- Use `type()` to check data type
- Use `id()` to check memory address
- Integers have unlimited precision in Python 3
- Floats are 64-bit double precision

### Type Checking and Conversion
```python
# Type checking
x = 10
print(isinstance(x, int))  # True - preferred method
print(type(x) == int)      # True - works but less flexible

# Type conversion
num_str = "42"
num_int = int(num_str)     # String to int
num_float = float(num_str) # String to float

# Handling conversion errors
try:
    invalid = int("hello")
except ValueError:
    print("Cannot convert to int")
```

### Truthy and Falsy Values
```python
# Falsy values (evaluate to False)
bool(0)         # False
bool(0.0)       # False
bool("")        # False
bool([])        # False
bool({})        # False
bool(None)      # False
bool(False)     # False

# Truthy values (everything else)
bool(1)         # True
bool("hello")   # True
bool([1])       # True
```

---

## 4️⃣ Operators

### Explanation
Operators perform operations on values and variables.

---

### Syntax
```python
a = 10
b = 3

print(a + b)    # Addition
print(a // b)   # Floor division
print(a ** b)   # Exponentiation
print(a % b)    # Modulus
```

### Output
```
13
3
1000
1
```

### Operator Categories
- **Arithmetic:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical:** `and`, `or`, `not`
- **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`
- **Membership:** `in`, `not in`
- **Identity:** `is`, `is not`

### Important Points
- `/` → float division (always returns float)
- `//` → floor division (rounds down)
- `**` → power operator
- `%` → modulus (remainder)
- `==` compares values, `is` compares identity

---

## 5️⃣ Control Flow (if / elif / else)

### Explanation
Controls decision-making in programs based on conditions.

---

### Syntax
```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### Output
```
Adult
```

### Ternary Operator
```python
status = "Adult" if age >= 18 else "Minor"
```

### Important Points
- Conditions end with `:`
- No parentheses required (but allowed)
- Order of conditions matters (first match wins)
- Use `elif`, not `else if`
- Truthy values: non-zero numbers, non-empty sequences
- Falsy values: `0`, `None`, `False`, `""`, `[]`, `{}`

---

## 6️⃣ Loops

### Explanation
Loops allow repeated execution of code blocks.

---

### for loop
```python
for i in range(3):
    print(i)
```

### Output
```
0
1
2
```

### while loop
```python
i = 0
while i < 3:
    print(i)
    i += 1
```

### Output
```
0
1
2
```

### Loop Control
```python
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Exit at 7
    print(i)
```

### else clause with loops
```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

### Important Points
- `break` exits loop completely
- `continue` skips current iteration
- `range(start, stop, step)` generates sequences
- Avoid infinite loops (always ensure exit condition)
- `else` clause executes if loop completes normally (no break)

---

## 7️⃣ Functions

### Explanation
Functions encapsulate logic, enable code reuse, and improve testability.

---

### Syntax
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

### Output
```
7
```

### Default Arguments
```python
def greet(name="User"):
    return f"Hello, {name}"

print(greet())
print(greet("Prerak"))
```

### Output
```
Hello, User
Hello, Prerak
```

### Multiple Return Values
```python
def calculate(a, b):
    return a + b, a - b, a * b

sum_val, diff, prod = calculate(10, 5)
```

### *args and **kwargs
```python
def flexible(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dict of keyword arguments

flexible(1, 2, 3, name="Prerak", age=21)
```

### Important Points
- Use `return`, not `print`, for results
- Functions should do one thing well (Single Responsibility)
- Small functions > large functions
- Document complex functions with docstrings
- Default arguments evaluated once at definition time

### Lambda Functions (Anonymous Functions)
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Common uses
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Sorting with lambda
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
```

### Scope (LEGB Rule)
```python
# Local, Enclosing, Global, Built-in
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

### Global and Nonlocal Keywords
```python
count = 0

def increment():
    global count  # Modify global variable
    count += 1

def outer():
    x = 0
    def inner():
        nonlocal x  # Modify enclosing variable
        x += 1
    inner()
    return x
```

### Docstrings (Documentation)
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: Area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
```

---

## 🔧 CORE DATA STRUCTURES & TEXT PROCESSING

---

## 8️⃣ Strings (str)

### Explanation
Strings are **immutable** sequences of characters.
Every string method returns a **new string**.

---

### Common Methods
```python
text = "  Hello Python World  "

print(text.lower())
print(text.strip())
print(text.replace("Python", "World"))
```

### Output
```
  hello python world  
Hello Python World
  Hello World World  
```

### Splitting & Joining
```python
words = "one two three".split()
print(words)

joined = "-".join(words)
print(joined)
```

### Output
```
['one', 'two', 'three']
one-two-three
```

### String Formatting
```python
name = "Prerak"
age = 21

# f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age}")

# format method
print("My name is {} and I'm {}".format(name, age))

# % formatting (old style)
print("My name is %s and I'm %d" % (name, age))
```

### String Slicing
```python
text = "Python"
print(text[0])      # First character
print(text[-1])     # Last character
print(text[0:3])    # Slice
print(text[::-1])   # Reverse
```

### Important Points
- Strings cannot be modified in place (immutable)
- Slicing is extremely common: `s[start:stop:step]`
- Use f-strings for modern formatting
- Triple quotes for multi-line strings
- Raw strings (`r""`) ignore escape sequences

---

## 9️⃣ Lists

### Explanation
Lists are **mutable** ordered collections that can hold any data type.

---

### Syntax
```python
nums = [1, 2, 3]
nums.append(4)
nums.pop()
print(nums)
```

### Output
```
[1, 2, 3]
```

### List Comprehension
```python
squares = [x*x for x in range(5)]
print(squares)
```

### Output
```
[0, 1, 4, 9, 16]
```

### List Comprehension with Condition
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

### Output
```
[0, 2, 4, 6, 8]
```

### List Slicing
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[::2])    # [0, 2, 4]
print(nums[::-1])   # Reverse
```

### Nested Lists
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6
```

### Important Points
- Lists grow dynamically
- Prefer comprehensions over loops for transformations
- `sort()` modifies list in-place, `sorted()` returns new list
- Lists are passed by reference
- Negative indexing starts from end

### Advanced List Operations
```python
# List unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Flattening nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# List methods comparison
nums = [3, 1, 4, 1, 5]
print(sorted(nums))  # Returns new sorted list: [1, 1, 3, 4, 5]
print(nums)          # Original unchanged: [3, 1, 4, 1, 5]

nums.sort()          # Sorts in-place
print(nums)          # [1, 1, 3, 4, 5]
```

### List Performance Tips
```python
# Efficient: Use comprehension
squares = [x**2 for x in range(1000)]

# Less efficient: Repeated append
squares = []
for x in range(1000):
    squares.append(x**2)

# Efficient: Extend with iterable
nums.extend([4, 5, 6])

# Less efficient: Multiple appends
nums.append(4)
nums.append(5)
nums.append(6)
```

### Common List Patterns
```python
# Remove duplicates (preserves order)
items = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(items))  # [1, 2, 3, 4]

# Find index of max value
nums = [5, 2, 9, 1, 7]
max_index = nums.index(max(nums))  # 2

# Reverse iteration
for item in reversed(nums):
    print(item)

# Count occurrences
count_2 = nums.count(2)
```

---

## 🔟 Tuples

### Explanation
Tuples are **immutable** lists.
Cannot be modified after creation.

---

### Syntax
```python
t = (1, 2, 3)
print(t[0])
```

### Output
```
1
```

### Tuple Unpacking
```python
coordinates = (10, 20)
x, y = coordinates
print(x, y)
```

### Output
```
10 20
```

### Single Element Tuple
```python
single = (5,)  # Comma required
not_tuple = (5)  # This is just an int
```

### Important Points
- Faster than lists (immutable = optimized)
- Used for fixed data (coordinates, RGB values, database records)
- Cannot be changed after creation
- Can be used as dictionary keys (hashable)
- Parentheses optional in many contexts: `t = 1, 2, 3`

---

## 1️⃣1️⃣ Dictionaries

### Explanation
Dictionaries map keys → values using hash tables.
Provide O(1) average lookup time.

---

### Syntax
```python
user = {"name": "Prerak", "age": 21}
print(user["name"])
```

### Output
```
Prerak
```

### Iteration
```python
for k, v in user.items():
    print(k, v)
```

### Output
```
name Prerak
age 21
```

### Dictionary Comprehension
```python
squares = {x: x**2 for x in range(5)}
print(squares)
```

### Output
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Important Points
- Keys must be immutable (strings, numbers, tuples)
- Order preserved (Python 3.7+)
- Extremely fast lookups O(1)
- Use `.get()` for safe access
- Can nest dictionaries for complex structures

### Advanced Dictionary Patterns
```python
# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2

# Merge with update precedence
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}

# Dictionary unpacking
merged = {**dict1, **dict2}

# Invert dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Group items by key
from collections import defaultdict
data = [("a", 1), ("b", 2), ("a", 3)]
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)
# {"a": [1, 3], "b": [2]}
```

### Collections Module (Must Know)
```python
from collections import Counter, defaultdict, OrderedDict, deque

# Counter - count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(word_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict - automatic default values
dd = defaultdict(int)  # Default value is 0
dd["count"] += 1  # No KeyError

dd = defaultdict(list)  # Default value is []
dd["items"].append(1)  # No KeyError

# deque - double-ended queue (efficient from both ends)
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)      # Add to right
dq.appendleft(0)  # Add to left
dq.pop()          # Remove from right
dq.popleft()      # Remove from left
```

---

## 1️⃣2️⃣ Sets

### Explanation
Sets store **unique values only** using hashing.
Unordered collection.

---

### Syntax
```python
s = {1, 2, 2, 3}
print(s)
```

### Output
```
{1, 2, 3}
```

### Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
```

### Output
```
{1, 2, 3, 4, 5}
{3}
{1, 2}
```

### Important Points
- No duplicates (automatic deduplication)
- No indexing (unordered)
- Fast membership testing O(1)
- Used for removing duplicates: `unique = list(set(my_list))`
- Set comprehensions available

---

## 1️⃣3️⃣ File Handling

### Explanation
Read/write external files safely.
Always use context managers (`with`) for automatic resource cleanup.

---

### Write File
```python
with open("data.txt", "w") as f:
    f.write("Hello")
```

### Read File
```python
with open("data.txt") as f:
    print(f.read())
```

### Output
```
Hello
```

### Read Line by Line
```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

### File Modes
| Mode | Meaning |
|------|---------|
| `r` | Read (default) |
| `w` | Write (overwrites) |
| `a` | Append |
| `r+` | Read and write |
| `rb` | Read binary |
| `wb` | Write binary |

### Important Points
- Always use `with` (auto-closes files)
- Files auto-close with context manager
- Handle exceptions in production code
- `.read()` loads entire file into memory
- Use `.readline()` or iteration for large files

### Working with CSV Files
```python
import csv

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# CSV with dictionaries
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

### Working with JSON Files
```python
import json

# Writing JSON
data = {
    "name": "Prerak",
    "skills": ["Python", "Git"],
    "experience": 2
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON
with open("data.json") as f:
    data = json.load(f)
    print(data["name"])

# JSON string operations
json_string = json.dumps(data)  # Object to JSON string
obj = json.loads(json_string)   # JSON string to object
```

### File Path Operations
```python
import os
from pathlib import Path

# Using os module
current_dir = os.getcwd()
file_exists = os.path.exists("data.txt")
file_size = os.path.getsize("data.txt")
dir_contents = os.listdir(".")

# Using pathlib (modern approach)
path = Path("data.txt")
print(path.exists())
print(path.is_file())
print(path.stat().st_size)
print(path.read_text())
path.write_text("Hello World")

# Join paths safely
file_path = Path("folder") / "subfolder" / "file.txt"
```

### Advanced File Handling
```python
# Read specific number of bytes
with open("data.txt", "rb") as f:
    chunk = f.read(1024)  # Read 1KB

# File pointer manipulation
with open("data.txt") as f:
    print(f.tell())    # Current position
    f.seek(0)          # Go to start
    f.seek(10)         # Go to position 10
    
# Writing multiple lines efficiently
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Safe file operations with error handling
def safe_file_read(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
```

---

## 🏗️ ADVANCED PROGRAMMING CONCEPTS

---

## 1️⃣4️⃣ Object-Oriented Programming (OOP)

### Explanation
OOP models real-world entities using classes.
Enables code organization, reusability, and encapsulation.

---

### Basic Class
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Prerak")
print(p.greet())
```

### Output
```
Hi, I'm Prerak
```

### Class Variables vs Instance Variables
```python
class Student:
    school = "ABC School"   # Class variable (shared)

    def __init__(self, name):
        self.name = name    # Instance variable (unique)

s1 = Student("A")
s2 = Student("B")

print(s1.school, s2.school)  # Both access same class variable
```

### Output
```
ABC School ABC School
```

### Inheritance
```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

d = Dog()
print(d.speak())
```

### Output
```
Bark
```

### Encapsulation (Private Attributes)
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

a = Account(1000)
print(a.get_balance())
```

### Output
```
1000
```

### Special (Dunder) Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.pages == other.pages

b = Book("Python Mastery", 500)
print(b)
print(len(b))
```

### Output
```
Python Mastery (500 pages)
500
```

### Important Points
- `self` refers to current object instance
- Classes improve code structure and maintainability
- Essential for large projects and frameworks
- `__init__` is the constructor
- Private attributes use double underscore prefix
- Dunder methods enable operator overloading

### Polymorphism
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphic behavior
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())  # Different implementations
```

### Class Methods and Static Methods
```python
class MathOperations:
    pi = 3.14159  # Class variable
    
    def __init__(self, value):
        self.value = value  # Instance variable
    
    @classmethod
    def from_string(cls, string):
        """Alternative constructor"""
        value = int(string)
        return cls(value)
    
    @staticmethod
    def add(a, b):
        """Utility function, doesn't need instance"""
        return a + b
    
    def multiply(self, other):
        """Instance method"""
        return self.value * other

# Usage
obj = MathOperations(10)
obj2 = MathOperations.from_string("20")  # Class method
result = MathOperations.add(5, 3)        # Static method
```

### Properties and Getters/Setters
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32

# Usage
temp = Temperature(25)
print(temp.celsius)      # 25 (uses getter)
print(temp.fahrenheit)   # 77.0 (computed)
temp.celsius = 30        # Uses setter
```

### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack"

duck = Duck()
print(duck.fly())    # From Flyable
print(duck.swim())   # From Swimmable
print(duck.quack())  # From Duck
```

### More Useful Dunder Methods
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Define + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        """User-friendly representation"""
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Define == operator"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Define len() behavior"""
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # (4, 6)
```

---

## 1️⃣5️⃣ Exception Handling

### Explanation
Prevents crashes and handles errors gracefully.
Essential for robust, production-ready code.

---

### Syntax
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

### Output
```
Error: Division by zero
```

### Multiple Exceptions
```python
try:
    value = int("abc")
except ValueError:
    print("Invalid conversion")
except TypeError:
    print("Type error")
finally:
    print("Cleanup always runs")
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### Custom Exceptions
```python
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @")
```

### Important Points
- Catch specific exceptions (never use bare `except`)
- `finally` block always executes
- Use exceptions for exceptional cases, not control flow
- Critical for reliability and debugging
- Log exceptions in production

---

## 1️⃣6️⃣ Generators

### Explanation
Generators produce values lazily (on-demand).
Memory efficient for large datasets.

---

### Syntax
```python
def count(n):
    for i in range(n):
        yield i

g = count(3)
print(next(g))
print(next(g))
```

### Output
```
0
1
```

### Generator Expression
```python
squares = (x*x for x in range(5))
print(next(squares))
print(next(squares))
```

### Output
```
0
1
```

### Important Points
- Memory efficient (doesn't store all values)
- Used for large data streams
- One-time use (exhausted after iteration)
- `yield` makes a function a generator
- Similar to list comprehension but with `()` instead of `[]`

---

## 1️⃣7️⃣ Decorators

### Explanation
Decorators modify or enhance function behavior.
Functions are first-class objects in Python.

---

### Syntax
```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```

### Output
```
Before
Hello
After
```

### Decorator with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Prerak")
```

### Important Points
- Functions are objects (can be passed as arguments)
- Used heavily in web frameworks (Flask, Django)
- Advanced but powerful concept
- Common use cases: logging, timing, authentication
- `@decorator` is syntactic sugar

### Practical Decorator Examples
```python
import time
import functools

# Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Caching decorator (memoization)
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Authentication decorator
def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def delete_account(user):
    return f"Deleting {user['name']}"
```

### Context Managers (with statement)
```python
# Creating custom context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello")

# Context manager with contextlib
from contextlib import contextmanager

@contextmanager
def temporary_change(obj, attr, value):
    """Temporarily change an attribute"""
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)

# Usage
class Config:
    debug = False

config = Config()
with temporary_change(config, 'debug', True):
    print(config.debug)  # True
print(config.debug)  # False
```

---

## 1️⃣8️⃣ Regular Expressions (re)

### Explanation
Regex enables pattern matching and text processing.
Powerful for validation, parsing, and extraction.

---

### Syntax
```python
import re

text = "My number is 12345"
print(re.findall(r"\d+", text))
```

### Output
```
['12345']
```

### Common Patterns
| Pattern | Meaning |
|---------|---------|
| `\d` | Digit |
| `\w` | Word character |
| `\s` | Whitespace |
| `.` | Any character |
| `^` | Start of string |
| `$` | End of string |
| `+` | One or more |
| `*` | Zero or more |
| `?` | Zero or one |

### Common Methods
```python
import re

# Search for pattern
match = re.search(r"\d+", "Age: 25")

# Find all matches
numbers = re.findall(r"\d+", "1 and 2 and 3")

# Replace
result = re.sub(r"\d", "X", "Room 123")
```

### Important Points
- Always use raw strings: `r"\d+"`
- Powerful but can be complex
- Test patterns carefully (use regex101.com)
- Common use: email validation, phone parsing
- Compile patterns for repeated use

---

# 📦 PYTHON BUILT-IN FUNCTIONS & METHODS (COMPLETE)

This section documents **Python's most important built-in functions and methods**.
Mastering these puts you ahead of ~80% of Python learners.

---

## 🧵 STRING BUILT-IN METHODS (`str`)

### Explanation
Strings are **immutable** — every method returns a **new string**.

---

### Core String Methods

```python
text = "  Hello Python World  "
```

| Method | Example | Output |
|--------|---------|--------|
| `len()` | `len(text)` | `22` |
| `lower()` | `text.lower()` | `"  hello python world  "` |
| `upper()` | `text.upper()` | `"  HELLO PYTHON WORLD  "` |
| `strip()` | `text.strip()` | `"Hello Python World"` |
| `lstrip()` | `text.lstrip()` | `"Hello Python World  "` |
| `rstrip()` | `text.rstrip()` | `"  Hello Python World"` |
| `replace()` | `text.replace("Python","AI")` | `"  Hello AI World  "` |
| `find()` | `text.find("Python")` | `8` |
| `count()` | `text.count("o")` | `3` |
| `startswith()` | `text.startswith(" He")` | `True` |
| `endswith()` | `text.endswith("World ")` | `True` |

### Split & Join (VERY IMPORTANT)
```python
sentence = "learn python fast"
words = sentence.split()
print(words)
```

**Output:**
```
['learn', 'python', 'fast']
```

```python
joined = "-".join(words)
print(joined)
```

**Output:**
```
learn-python-fast
```

### Important Points
- Strings cannot be changed in place
- Use f-strings for modern formatting
- Heavy usage in APIs, files, parsing
- `strip()` removes whitespace from both ends
- `split()` without arguments splits on whitespace

---

## 📋 LIST BUILT-IN METHODS (`list`)

### Explanation
Lists are mutable, ordered collections with dynamic sizing.

---

### Core List Methods
```python
nums = [1, 2, 3]
```

| Method | Example | Output/Effect |
|--------|---------|---------------|
| `append()` | `nums.append(4)` | `[1,2,3,4]` |
| `extend()` | `nums.extend([5,6])` | `[1,2,3,4,5,6]` |
| `insert()` | `nums.insert(1,10)` | `[1,10,2,3]` |
| `remove()` | `nums.remove(2)` | `[1,3]` |
| `pop()` | `nums.pop()` | returns `3`, modifies list |
| `index()` | `nums.index(1)` | `0` |
| `count()` | `nums.count(1)` | `1` |
| `sort()` | `nums.sort()` | modifies list in-place |
| `reverse()` | `nums.reverse()` | modifies list in-place |
| `clear()` | `nums.clear()` | `[]` |
| `copy()` | `nums.copy()` | shallow copy |

### Example with Output
```python
nums = [3, 1, 2]
nums.sort()
print(nums)
```

**Output:**
```
[1, 2, 3]
```

### Important Points
- Lists are passed by reference
- `sort()` is in-place, `sorted()` returns new list
- Prefer list comprehensions for transformations
- `append()` adds one element, `extend()` adds multiple
- `pop()` without argument removes last element

---

## 📦 TUPLE BUILT-IN FUNCTIONS (`tuple`)

### Explanation
Tuples are immutable sequences, faster than lists.

---

### Tuple Functions
```python
t = (1, 2, 2, 3)
```

| Function | Example | Output |
|----------|---------|--------|
| `len()` | `len(t)` | `4` |
| `max()` | `max(t)` | `3` |
| `min()` | `min(t)` | `1` |
| `count()` | `t.count(2)` | `2` |
| `index()` | `t.index(3)` | `3` |

### Important Points
- Cannot modify elements
- Faster than lists (immutable = optimized)
- Used for fixed data & unpacking
- Can be used as dictionary keys
- Parentheses often optional

---

## 🧠 GENERATORS & ITERATION UTILITIES

### Explanation
Generators produce values one at a time using `yield`.
Memory efficient for large datasets.

---

### Generator Example
```python
def squares(n):
    for i in range(n):
        yield i*i

g = squares(3)
print(next(g))
print(next(g))
```

**Output:**
```
0
1
```

### Generator-Related Built-ins

| Function | Purpose |
|----------|---------|
| `next()` | Get next value from iterator |
| `iter()` | Convert iterable to iterator |
| `enumerate()` | Get index + value pairs |
| `zip()` | Combine multiple iterables |
| `map()` | Apply function to iterable |
| `filter()` | Filter iterable by condition |

### enumerate Example
```python
names = ["a", "b", "c"]

for i, v in enumerate(names):
    print(i, v)
```

**Output:**
```
0 a
1 b
2 c
```

### zip Example
```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

**Output:**
```
Alice: 25
Bob: 30
```

### Important Points
- Generators save memory (lazy evaluation)
- One-time consumption (exhausted after iteration)
- Used in data pipelines & streaming
- `enumerate()` better than manual counter
- `zip()` stops at shortest iterable

---

## ⚙️ GLOBAL PYTHON BUILT-IN FUNCTIONS (MUST MASTER)

### Core Built-ins

| Function | Example | Output |
|----------|---------|--------|
| `type()` | `type(10)` | `<class 'int'>` |
| `id()` | `id(x)` | memory address |
| `input()` | `input("Name:")` | user input string |
| `sum()` | `sum([1,2,3])` | `6` |
| `abs()` | `abs(-5)` | `5` |
| `sorted()` | `sorted([3,1,2])` | `[1,2,3]` |
| `any()` | `any([0,1,0])` | `True` |
| `all()` | `all([1,1,1])` | `True` |
| `len()` | `len([1,2,3])` | `3` |
| `range()` | `range(3)` | `range(0,3)` |
| `min()` | `min([1,2,3])` | `1` |
| `max()` | `max([1,2,3])` | `3` |
| `round()` | `round(3.7)` | `4` |
| `pow()` | `pow(2,3)` | `8` |
| `isinstance()` | `isinstance(5, int)` | `True` |

### Type Conversion Functions
```python
int("10")      # String to int
float("3.14")  # String to float
str(100)       # Int to string
list("abc")    # String to list: ['a','b','c']
tuple([1,2])   # List to tuple
set([1,1,2])   # List to set: {1,2}
```

### Important Points
- Built-ins are optimized in C (very fast)
- Use built-ins instead of writing custom versions
- `any()` returns True if at least one element is truthy
- `all()` returns True if all elements are truthy
- `isinstance()` preferred over `type()` for type checking

---

# 🗂️ DICTIONARIES & SETS — DEEP DIVE

These two data structures are **hash-based** and power Python's performance.
Mastering these means understanding how Python really works.

---

# 📘 DICTIONARY (`dict`) — COMPLETE DEEP DIVE

---

## 1️⃣ What is a Dictionary?

### Explanation
A dictionary stores data as **key → value** pairs using a **hash table**.
Lookup, insert, delete → **O(1) average time complexity**.

Dictionaries are the backbone of Python's performance and are used everywhere.

---

### Syntax
```python
student = {
    "name": "Prerak",
    "age": 21,
    "skills": ["Python", "Git"]
}
```

### Important Points
- Keys must be immutable (str, int, tuple)
- Values can be anything (mutable or immutable)
- Insertion order preserved (Python 3.7+)
- Fast lookups due to hashing
- Cannot have duplicate keys

---

## 2️⃣ Creating Dictionaries (ALL WAYS)

```python
# Literal syntax
d1 = {"a": 1, "b": 2}

# dict constructor
d2 = dict(a=1, b=2)

# from list of tuples
d3 = dict([("a", 1), ("b", 2)])

# from keys with default value
d4 = dict.fromkeys(["a", "b"], 0)

# dictionary comprehension
d5 = {x: x**2 for x in range(5)}
```

**Output for d4:**
```python
print(d4)
```
```
{'a': 0, 'b': 0}
```

---

## 3️⃣ Accessing Data

### Syntax
```python
user = {"name": "Prerak", "age": 21}

print(user["name"])
print(user.get("age"))
print(user.get("salary", "Not Found"))
```

### Output
```
Prerak
21
Not Found
```

### Important Points
- `[]` → raises `KeyError` if key missing
- `get()` → safe access, returns `None` or default
- Always prefer `get()` in production code
- Can check existence with `in`: `if "name" in user:`

---

## 4️⃣ Adding & Updating Elements

```python
user = {"name": "Prerak"}

user["city"] = "Mumbai"      # Add new key
user["age"] = 22             # Add new key
user["age"] = 23             # Update existing key
```

**Alternative with update():**
```python
user.update({"city": "Delhi", "country": "India"})
```

### Important Points
- Assignment creates or updates keys
- No duplicate keys allowed (last value wins)
- `update()` merges multiple key-value pairs
- Dictionary unpacking: `{**dict1, **dict2}`

---

## 5️⃣ Removing Elements

```python
user = {"name": "Prerak", "age": 21, "city": "Mumbai"}

# Remove and return value
city = user.pop("city")

# Remove last inserted pair (returns tuple)
item = user.popitem()

# Delete key
del user["age"]

# Clear all items
user.clear()
```

### Important Points
- `pop(key)` removes key and returns value
- `pop(key, default)` returns default if key missing
- `popitem()` removes last inserted pair (LIFO in 3.7+)
- `del` removes key completely
- `clear()` empties dictionary but keeps reference

---

## 6️⃣ Dictionary Methods (CORE)

```python
d = {"a": 1, "b": 2, "c": 3}
```

| Method | Purpose | Returns |
|--------|---------|---------|
| `keys()` | All keys | dict_keys object |
| `values()` | All values | dict_values object |
| `items()` | Key-value pairs | dict_items object |
| `update()` | Merge dictionaries | None |
| `copy()` | Shallow copy | New dict |
| `get()` | Safe access | Value or None |
| `setdefault()` | Get or set default | Value |
| `pop()` | Remove and return | Value |
| `popitem()` | Remove last item | (key, value) tuple |

### Example
```python
for k, v in d.items():
    print(k, v)
```

**Output:**
```
a 1
b 2
c 3
```

### setdefault() Example
```python
d = {"a": 1}
value = d.setdefault("b", 0)  # Sets b=0 and returns 0
print(d)
```

**Output:**
```
{'a': 1, 'b': 0}
```

---

## 7️⃣ Dictionary Comprehension

### Explanation
Fast, clean dictionary creation using comprehension syntax.

---

### Syntax
```python
squares = {x: x*x for x in range(5)}
print(squares)
```

### Output
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### With Condition
```python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)
```

### Output
```
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Important Points
- Faster than loops
- More readable than traditional dict creation
- Used heavily in data processing
- Can transform keys and values simultaneously

---

## 8️⃣ Nested Dictionaries

```python
company = {
    "emp1": {"name": "A", "salary": 50000},
    "emp2": {"name": "B", "salary": 60000}
}
```

### Access
```python
print(company["emp1"]["salary"])
```

### Output
```
50000
```

### Safe Access with get()
```python
salary = company.get("emp1", {}).get("salary", 0)
```

### Important Points
- Common in JSON / API responses
- Validate keys before access to avoid errors
- Use `.get()` for safety in nested structures
- Can represent complex hierarchical data

---

## 9️⃣ Shallow vs Deep Copy (VERY IMPORTANT)

```python
import copy

a = {"x": [1, 2]}

# Shallow copy
b = a.copy()

# Deep copy
c = copy.deepcopy(a)

# Modify nested list
a["x"].append(3)

print(b)
print(c)
```

### Output
```
{'x': [1, 2, 3]}
{'x': [1, 2]}
```

### Important Points
- `.copy()` → shallow (nested objects shared)
- `deepcopy()` → full independent clone
- Shallow copy faster but can cause unexpected behavior
- Deep copy needed for nested mutable structures
- **Interview favorite question**

---

## 🔥 Dictionary Performance (INTERVIEW GOLD)

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Lookup | O(1) | Average case |
| Insert | O(1) | Average case |
| Delete | O(1) | Average case |
| Iterate | O(n) | All keys/values |
| Copy | O(n) | Shallow copy |
| Deep Copy | O(n) | Recursive |

### Important Points
- Hash table based = extremely fast
- Worst case O(n) due to collisions (rare)
- Space complexity O(n)
- Memory overhead higher than lists
- Perfect for lookups and mappings

---

# 🧮 SET (`set`) — DEEP DIVE

---

## 1️⃣ What is a Set?

### Explanation
A set stores **unique, unordered values** using hashing.
Fast membership testing and mathematical set operations.

---

### Syntax
```python
s = {1, 2, 3, 3}
print(s)
```

### Output
```
{1, 2, 3}
```

### Important Points
- No duplicates (automatic deduplication)
- No indexing (unordered)
- Extremely fast lookups O(1)
- Elements must be immutable
- Cannot contain lists or dictionaries

---

## 2️⃣ Creating Sets

```python
# Literal
s1 = {1, 2, 3}

# Constructor
s2 = set([3, 4, 5])

# From string
s3 = set("hello")  # {'h', 'e', 'l', 'o'}

# Empty set
empty = set()  # NOT {}
```

### Important Points
- `{}` creates dict, not set
- Use `set()` for empty set
- Can convert lists to sets for deduplication
- Set comprehensions available: `{x for x in range(5)}`

---

## 3️⃣ Adding & Removing Elements

```python
s = {1, 2}

# Add single element
s.add(3)

# Remove element (error if missing)
s.remove(2)

# Remove element (no error)
s.discard(10)

# Remove and return arbitrary element
element = s.pop()

# Clear all elements
s.clear()
```

### Important Points
- `add()` adds one element
- `remove()` → raises `KeyError` if missing
- `discard()` → safe removal (no error)
- `pop()` removes arbitrary element (sets unordered)
- Sets are mutable

---

## 4️⃣ Set Operations (VERY IMPORTANT)

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

| Operation | Syntax | Result | Alternative |
|-----------|--------|--------|-------------|
| Union | `a \| b` | `{1,2,3,4,5}` | `a.union(b)` |
| Intersection | `a & b` | `{3}` | `a.intersection(b)` |
| Difference | `a - b` | `{1,2}` | `a.difference(b)` |
| Symmetric Diff | `a ^ b` | `{1,2,4,5}` | `a.symmetric_difference(b)` |

### Visual Explanation
- **Union**: All elements from both sets
- **Intersection**: Only common elements
- **Difference**: Elements in first but not second
- **Symmetric Difference**: Elements in either but not both

---

## 5️⃣ Set Methods

```python
a = {1, 2}
b = {1, 2, 3}
```

| Method | Purpose | Example |
|--------|---------|---------|
| `issubset()` | Check if subset | `a.issubset(b)` → `True` |
| `issuperset()` | Check if superset | `b.issuperset(a)` → `True` |
| `isdisjoint()` | No common elements | `a.isdisjoint({4,5})` → `True` |
| `update()` | Add multiple elements | `a.update([3,4])` |
| `intersection_update()` | Keep only common | Modifies set |
| `difference_update()` | Remove common | Modifies set |

### Important Points
- Used in mathematical and logical operations
- Fast relationship checks
- Cleaner than manual loops
- Methods with `_update` modify in-place

---

## 6️⃣ Set Comprehension

```python
squares = {x*x for x in range(5)}
print(squares)
```

### Output
```
{0, 1, 4, 9, 16}
```

### With Condition
```python
even_squares = {x*x for x in range(10) if x % 2 == 0}
```

---

## 7️⃣ Frozen Sets (IMMUTABLE SETS)

### Explanation
Frozen sets are immutable versions of sets.
Can be used as dictionary keys.

---

### Syntax
```python
fs = frozenset([1, 2, 3])

# Cannot modify
# fs.add(4)  # AttributeError
```

### Important Points
- Hashable (can be dict keys)
- Immutable (cannot add/remove)
- Used in advanced scenarios
- All set operations available (return new frozensets)

---

## 🔥 Set Performance

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| Add | O(1) | Average |
| Remove | O(1) | Average |
| Lookup (membership) | O(1) | Average |
| Union | O(n+m) | n, m = sizes |
| Intersection | O(min(n,m)) | Smaller set |
| Difference | O(n) | First set |

### Important Points
- Hash table based = very fast
- Perfect for uniqueness and membership
- More efficient than list for lookups
- Common use: removing duplicates from lists
- Great for mathematical operations

---

## 🧠 FINAL DICT & SET RULES (MEMORIZE)

1. **Dict** → key-value mapping, O(1) lookups
2. **Set** → uniqueness & mathematical operations, O(1) membership
3. **Hashing drives performance** in both
4. **Use sets to remove duplicates** from sequences
5. **Use dicts for structured data** and fast access
6. **`.get()` > `[]`** in production (safety)
7. **Shallow vs deep copy** matters for nested structures
8. **Both are mutable** (except frozenset)
9. **Keys/elements must be immutable** (hashable)
10. **Order preserved in dicts** since Python 3.7+

---

## 🚀 FINAL PRINCIPLES FOR MASTERY

1. **Read code daily** — Study Python's standard library
2. **Write small programs daily** — Build muscle memory
3. **Debug more than you code** — Understanding errors makes you stronger
4. **Understand memory behavior** — Know when objects are copied vs referenced
5. **Build projects early** — Apply concepts to real problems
6. **Master built-ins** — They're optimized and battle-tested
7. **Use comprehensions** — More Pythonic and often faster
8. **Handle exceptions** — Robust code survives edge cases
9. **Practice OOP** — Essential for frameworks and large systems
10. **Learn time/space complexity** — Write efficient code from the start

---

## 📦 MODULES, PACKAGES & VIRTUAL ENVIRONMENTS

---

### Modules

#### Explanation
A module is a file containing Python code that can be imported and reused.

**Creating and Using Modules:**

**my_module.py:**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a + b

PI = 3.14159
```

**main.py:**
```python
# Import entire module
import my_module
print(my_module.greet("Prerak"))
print(my_module.PI)

# Import specific items
from my_module import greet, add
print(greet("Prerak"))

# Import with alias
import my_module as mm
print(mm.add(5, 3))

# Import all (not recommended)
from my_module import *
```

**Important Points:**
- One file = one module
- `__name__` is `"__main__"` when script is run directly
- Use `if __name__ == "__main__":` for executable scripts
- Modules are imported once (cached)

---

### Packages

#### Explanation
A package is a directory containing multiple modules with an `__init__.py` file.

**Package Structure:**
```
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

**Using Packages:**
```python
# Import from package
from my_package import module1
from my_package.sub_package import module3

# Import specific function
from my_package.module1 import some_function
```

---

### Virtual Environments

#### Explanation
Virtual environments create isolated Python environments for projects.

**Creating Virtual Environment:**
```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Deactivate
deactivate
```

**Managing Dependencies:**
```bash
# Install package
pip install requests

# Install from requirements.txt
pip install -r requirements.txt

# Generate requirements.txt
pip freeze > requirements.txt
```

---

### The Standard Library (Important Modules)

```python
# Operating system interface
import os
print(os.getcwd())

# File paths
from pathlib import Path
path = Path("file.txt")

# Date and time
from datetime import datetime, timedelta
now = datetime.now()

# Random numbers
import random
print(random.randint(1, 10))

# JSON
import json
data = {"name": "Prerak"}
json_str = json.dumps(data)

# Math operations
import math
print(math.sqrt(16))

# Collections
from collections import Counter, defaultdict, deque

# Itertools
from itertools import cycle, chain, combinations
```

---

## 🧪 TESTING IN PYTHON

---

### Unit Testing with unittest

```python
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py
import unittest
from calculator import add, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Testing with pytest
```bash
pip install pytest
```

```python
# test_calculator_pytest.py
from calculator import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

## ⚡ PERFORMANCE & OPTIMIZATION

---

### Time Complexity Reference

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Access | O(1) | O(1) | - |
| Search | O(n) | O(1) | O(1) |
| Insert | O(1)* | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

### Optimization Tips
```python
# Use list comprehension
squares = [x**2 for x in range(1000)]

# Use generators for large datasets
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Use set for membership testing (O(1))
unique_ids = set([1, 2, 3, 4, 5])
if user_id in unique_ids:
    pass

# Use Counter for counting
from collections import Counter
counts = Counter(items)
```

---

## 🚀 FINAL PRINCIPLES FOR MASTERY

1. **Read code daily** — Study Python's standard library
2. **Write small programs daily** — Build muscle memory
3. **Debug more than you code** — Understanding errors makes you stronger
4. **Understand memory behavior** — Know when objects are copied vs referenced
5. **Build projects early** — Apply concepts to real problems
6. **Master built-ins** — They're optimized and battle-tested
7. **Use comprehensions** — More Pythonic and often faster
8. **Handle exceptions** — Robust code survives edge cases
9. **Practice OOP** — Essential for frameworks and large systems
10. **Learn time/space complexity** — Write efficient code from the start

---

## 📊 Quick Reference: Data Structure Selection

| Need | Use |
|------|-----|
| Ordered collection | List |
| Unique elements | Set |
| Key-value mapping | Dictionary |
| Fixed data | Tuple |
| Fast lookups | Dictionary or Set |
| Stack (LIFO) | List with append/pop |
| Queue (FIFO) | `collections.deque` |
| Remove duplicates | Set |
| Count occurrences | `collections.Counter` |

---

## 🎯 What Makes a Top 1% Python Developer

**Syntax makes you capable.**  
**Practice makes you dangerous.**  
**Projects make you professional.**

### Key Differentiators:
- ✅ Deep understanding of data structures
- ✅ Mastery of built-in functions
- ✅ Clean, readable, Pythonic code
- ✅ Proper exception handling
- ✅ Understanding of memory and performance
- ✅ Ability to debug complex issues
- ✅ Knowledge of OOP principles
- ✅ Real project experience
- ✅ Understanding of time/space complexity
- ✅ Consistent daily practice

---

**End of Python Master Notes — Complete Edition**

*Keep learning, keep building, keep improving.* 🚀