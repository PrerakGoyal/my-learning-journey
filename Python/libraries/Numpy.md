# NumPy Complete Guide: From Beginner to Industry Expert

> **Course Duration:** 8-10 weeks  
> **Skill Level:** Beginner → Advanced  
> **Goal:** Achieve top 1% NumPy proficiency for industrial applications

---

## Table of Contents

1. [Introduction & Setup](#1-introduction--setup)
2. [Phase 1: Foundations](#phase-1-foundations-week-1-2)
3. [Phase 2: Intermediate Operations](#phase-2-intermediate-operations-week-3-4)
4. [Phase 3: Advanced Techniques](#phase-3-advanced-techniques-week-5-6)
5. [Phase 4: Industrial Applications](#phase-4-industrial-applications-week-7-8)
6. [Major Projects](#major-projects)
7. [Best Practices & Optimization](#industrial-best-practices)
8. [Learning Resources](#learning-resources)

---

## 1. Introduction & Setup

### What is NumPy?

**Simple Definition:** NumPy is like a supercharged calculator for Python that works with lists of numbers (called arrays) really, really fast.

**Why You Need NumPy:**
- **Speed:** 10-100x faster than regular Python lists
- **Memory:** Uses less memory for large datasets
- **Convenience:** One line of code replaces dozens of loops
- **Industry Standard:** Used in AI, data science, finance, engineering

**Real-World Analogy:**
```
Python Lists = Using a calculator, one number at a time
NumPy Arrays = Using Excel formulas on entire columns at once
```

### Installation

```bash
# Install NumPy
pip install numpy

# Verify installation
python -c "import numpy; print(numpy.__version__)"
```

### Your First NumPy Program

```python
import numpy as np  # 'np' is the standard abbreviation

# Create your first array
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(type(my_array))

# Do math on ALL numbers at once!
doubled = my_array * 2
print(doubled)  # [2, 4, 6, 8, 10]
```

**🎯 Learning Objective:** Understand that NumPy operates on entire arrays at once (vectorization).

---

## PHASE 1: FOUNDATIONS (Week 1-2)

### 1.1 Understanding Arrays - The Core Concept

#### What is an Array?

Think of an array as a:
- **1D array** = A single row of boxes with numbers
- **2D array** = A spreadsheet (rows and columns)
- **3D array** = A stack of spreadsheets

```
1D Array: [1, 2, 3, 4, 5]

2D Array (Matrix):
┌─────────────┐
│ 1  2  3  4  │
│ 5  6  7  8  │
│ 9 10 11 12  │
└─────────────┘

3D Array (Cube):
Layer 1:        Layer 2:
[1  2]          [9  10]
[3  4]          [11 12]
```

#### Arrays vs Lists - Key Differences

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| **Speed** | Slow | Fast (10-100x) |
| **Data Types** | Mixed (1, "hello", True) | Homogeneous (all int or all float) |
| **Size** | Dynamic | Fixed |
| **Math Operations** | Not built-in | Built-in |
| **Memory** | More | Less |

**Example - Speed Comparison:**

```python
import numpy as np
import time

# Python list approach
python_list = list(range(1000000))
start = time.time()
result_list = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy array approach
numpy_array = np.arange(1000000)
start = time.time()
result_array = numpy_array * 2
numpy_time = time.time() - start

print(f"Python: {python_time:.4f} seconds")
print(f"NumPy:  {numpy_time:.4f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")
```

**Expected Output:**
```
Python: 0.0856 seconds
NumPy:  0.0012 seconds
NumPy is 71.3x faster!
```

---

### 1.2 Creating Arrays - 10 Essential Methods

#### Method 1: From Python Lists

```python
import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
# Output: [1 2 3 4 5]

# 2D array (list of lists)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)
# Output: (2, 2, 2)
```

**💡 Tip:** Shape (2, 2, 2) means: 2 layers, 2 rows, 2 columns

#### Method 2: Arrays Full of Zeros

```python
# All zeros - useful for initializing
zeros_1d = np.zeros(5)
# Output: [0. 0. 0. 0. 0.]

zeros_2d = np.zeros((3, 4))
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Specify data type
zeros_int = np.zeros(5, dtype=int)
# Output: [0 0 0 0 0]
```

**Use Case:** Pre-allocating space for results in loops

#### Method 3: Arrays Full of Ones

```python
ones = np.ones((2, 3))
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

#### Method 4: Arrays with Specific Value

```python
# Fill with 7
sevens = np.full((3, 3), 7)
# Output:
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]
```

#### Method 5: Identity Matrix (Eye)

```python
# Identity matrix (1s on diagonal, 0s elsewhere)
identity = np.eye(4)
# Output:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
```

**Use Case:** Linear algebra operations, solving equations

#### Method 6: Range of Numbers (arange)

```python
# Like Python's range()
arr = np.arange(10)
# Output: [0 1 2 3 4 5 6 7 8 9]

# With start and step
arr = np.arange(5, 15, 2)
# Output: [ 5  7  9 11 13]

# With floats
arr = np.arange(0, 1, 0.1)
# Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
```

#### Method 7: Evenly Spaced Numbers (linspace)

```python
# 5 numbers between 0 and 1 (INCLUDES endpoint)
arr = np.linspace(0, 1, 5)
# Output: [0.   0.25 0.5  0.75 1.  ]

# Great for plotting
x = np.linspace(0, 2*np.pi, 100)  # 100 points for smooth curve
y = np.sin(x)
```

**Key Difference:**
- `arange(0, 1, 0.1)` → step size is 0.1
- `linspace(0, 1, 5)` → 5 numbers total

#### Method 8: Random Numbers

```python
# Random floats between 0 and 1
random_floats = np.random.random((3, 3))

# Random integers
random_ints = np.random.randint(0, 100, size=(5, 5))

# Random from normal distribution (mean=0, std=1)
normal = np.random.randn(1000)

# Set seed for reproducibility
np.random.seed(42)
arr = np.random.random(5)  # Always same result
```

#### Method 9: Empty Array (Faster but Uninitialized)

```python
# ⚠️ Contains garbage values - use carefully
empty = np.empty((2, 3))
# Then fill it:
empty[:] = 5
```

#### Method 10: Array Like Another Array

```python
arr = np.array([[1, 2], [3, 4]])

zeros_like = np.zeros_like(arr)
ones_like = np.ones_like(arr)
random_like = np.random.random(arr.shape)
```

---

### 1.3 Array Attributes - Know Your Data

Every NumPy array has these important properties:

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Shape: dimensions (rows, columns, ...)
print(arr.shape)      # (3, 4) - 3 rows, 4 columns

# Number of dimensions
print(arr.ndim)       # 2

# Total number of elements
print(arr.size)       # 12

# Data type of elements
print(arr.dtype)      # dtype('int64')

# Size of each element in bytes
print(arr.itemsize)   # 8 bytes

# Total bytes consumed
print(arr.nbytes)     # 96 (12 elements × 8 bytes)
```

**Visual Representation:**
```
arr.shape = (3, 4)
       ↓
    [4 columns]
    ──────────
    1  2  3  4  ┐
    5  6  7  8  │ 3 rows
    9 10 11 12  ┘
```

---

### 1.4 Data Types (dtype) - Critical for Performance

#### Common Data Types

```python
# Integers
int8_arr    = np.array([1, 2], dtype=np.int8)     # -128 to 127
int16_arr   = np.array([1, 2], dtype=np.int16)    # -32,768 to 32,767
int32_arr   = np.array([1, 2], dtype=np.int32)    # -2B to 2B
int64_arr   = np.array([1, 2], dtype=np.int64)    # Default

# Unsigned integers (no negative)
uint8_arr   = np.array([1, 2], dtype=np.uint8)    # 0 to 255
uint16_arr  = np.array([1, 2], dtype=np.uint16)   # 0 to 65,535

# Floats
float16_arr = np.array([1.0], dtype=np.float16)   # Half precision
float32_arr = np.array([1.0], dtype=np.float32)   # Single precision
float64_arr = np.array([1.0], dtype=np.float64)   # Double (default)

# Boolean
bool_arr    = np.array([True, False], dtype=np.bool_)

# String (fixed length)
str_arr     = np.array(['a', 'b'], dtype='U10')   # Unicode, 10 chars
```

#### Why Data Types Matter

```python
# Memory usage example
small_arr = np.zeros(1000000, dtype=np.float32)
large_arr = np.zeros(1000000, dtype=np.float64)

print(f"float32: {small_arr.nbytes / 1e6} MB")  # 4 MB
print(f"float64: {large_arr.nbytes / 1e6} MB")  # 8 MB
```

**💰 Real Cost:**
- 100 million numbers as float64 = 800 MB
- 100 million numbers as float32 = 400 MB
- **50% memory savings!**

#### Choosing the Right dtype

```python
# Images (pixel values 0-255)
image = np.zeros((1920, 1080, 3), dtype=np.uint8)  # ✅ Perfect

# Prices (need decimals, not huge range)
prices = np.array([19.99, 29.99], dtype=np.float32)  # ✅ Good

# Counts (whole numbers, can be large)
counts = np.zeros(10000, dtype=np.int32)  # ✅ Sufficient

# Scientific calculations (need precision)
calculations = np.zeros(1000, dtype=np.float64)  # ✅ Necessary
```

#### Type Conversion

```python
# Convert types
float_arr = np.array([1.7, 2.3, 3.9])
int_arr = float_arr.astype(np.int32)
# Output: [1 2 3] - truncates decimals!

# Check type
print(int_arr.dtype)  # int32
```

---

### 1.5 Indexing & Slicing - Accessing Elements

#### 1D Array Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

# Positive indexing (from start)
print(arr[0])    # 10 - first element
print(arr[2])    # 30 - third element

# Negative indexing (from end)
print(arr[-1])   # 50 - last element
print(arr[-2])   # 40 - second to last
```

**Visual:**
```
Index:     0   1   2   3   4
Array:    10  20  30  40  50
Index:    -5  -4  -3  -2  -1
```

#### 1D Array Slicing

**Syntax:** `arr[start:stop:step]`

```python
arr = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

print(arr[2:5])      # [20 30 40] - index 2 to 4
print(arr[:5])       # [ 0 10 20 30 40] - start to 4
print(arr[5:])       # [50 60 70 80 90] - 5 to end
print(arr[::2])      # [ 0 20 40 60 80] - every 2nd element
print(arr[::-1])     # [90 80 70 60 50 40 30 20 10 0] - reversed!
```

**Memory Trick:** "Start Where, Stop Before, Step By"

#### 2D Array Indexing

```python
arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12]])

# Single element
print(arr[0, 0])      # 1 - row 0, column 0
print(arr[1, 2])      # 7 - row 1, column 2
print(arr[-1, -1])    # 12 - last row, last column

# Entire row
print(arr[0])         # [1 2 3 4] - first row
print(arr[1, :])      # [5 6 7 8] - second row (explicit)

# Entire column
print(arr[:, 0])      # [1 5 9] - first column
print(arr[:, 2])      # [ 3  7 11] - third column
```

**Visual:**
```
       Column 0  1  2  3
Row 0:        1  2  3  4
Row 1:        5  6  7  8
Row 2:        9 10 11 12

arr[1, 2] = 7
    ↑  ↑
  row  col
```

#### 2D Array Slicing

```python
arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12]])

# Rows 0-1, all columns
print(arr[0:2, :])
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]

# All rows, columns 1-2
print(arr[:, 1:3])
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

# Subset: rows 0-1, columns 1-2
print(arr[0:2, 1:3])
# Output:
# [[2 3]
#  [6 7]]
```

#### Boolean Indexing (Super Powerful!)

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create boolean mask
mask = arr > 5
print(mask)
# Output: [False False False False False  True  True  True  True  True]

# Use mask to filter
filtered = arr[mask]
print(filtered)
# Output: [ 6  7  8  9 10]

# One line
result = arr[arr > 5]  # Same as above

# Multiple conditions
result = arr[(arr > 3) & (arr < 8)]  # Note: & not 'and'
print(result)
# Output: [4 5 6 7]
```

**Real-World Example:**
```python
# Temperature data
temps = np.array([72, 68, 75, 82, 79, 65, 71, 88, 90, 67])

# Find hot days (> 80°F)
hot_days = temps[temps > 80]
print(f"Hot days: {hot_days}")  # [82 88 90]

# Count hot days
print(f"Number of hot days: {(temps > 80).sum()}")  # 3
```

#### Fancy Indexing (Index with Arrays)

```python
arr = np.array([10, 20, 30, 40, 50])

# Select specific indices
indices = [0, 2, 4]
selected = arr[indices]
print(selected)  # [10 30 50]

# 2D fancy indexing
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
rows = [0, 2]
cols = [1, 0]
result = arr_2d[rows, cols]
print(result)  # [2 5] - elements at (0,1) and (2,0)
```

---

### 1.6 Modifying Arrays

#### Changing Values

```python
arr = np.array([1, 2, 3, 4, 5])

# Single element
arr[0] = 99
print(arr)  # [99  2  3  4  5]

# Multiple elements via slicing
arr[1:4] = [20, 30, 40]
print(arr)  # [99 20 30 40  5]

# Broadcast single value
arr[1:4] = 0
print(arr)  # [99  0  0  0  5]

# Boolean indexing
arr[arr < 50] = 0
print(arr)  # [99  0  0  0  0]
```

#### Important: Views vs Copies

```python
arr = np.array([1, 2, 3, 4, 5])

# Slicing creates a VIEW (shares memory)
view = arr[1:4]
view[0] = 999
print(arr)  # [1 999 3 4 5] - ORIGINAL CHANGED!

# Create a COPY (independent)
copy = arr[1:4].copy()
copy[0] = 777
print(arr)  # [1 999 3 4 5] - original unchanged

# Check if view or copy
print(view.base is arr)   # True - it's a view
print(copy.base is None)  # True - it's a copy
```

**⚠️ Critical Concept:**
```
View:  Modifying view → modifies original
Copy:  Modifying copy → original stays same
```

---

### 1.7 Basic Array Operations

#### Arithmetic Operations (Element-wise)

```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# Element-wise operations
print(arr1 + arr2)   # [11 22 33 44]
print(arr1 - arr2)   # [-9 -18 -27 -36]
print(arr1 * arr2)   # [ 10  40  90 160]
print(arr1 / arr2)   # [0.1 0.1 0.1 0.1]
print(arr1 ** 2)     # [ 1  4  9 16]

# With scalars
print(arr1 + 10)     # [11 12 13 14]
print(arr1 * 2)      # [2 4 6 8]
```

#### Comparison Operations

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr > 3)       # [False False False  True  True]
print(arr == 3)      # [False False  True False False]
print(arr != 3)      # [ True  True False  True  True]
```

#### Array-Scalar Operations

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Add 10 to every element
result = arr + 10
# Output:
# [[11 12 13]
#  [14 15 16]]

# Multiply every element by 2
result = arr * 2
# Output:
# [[ 2  4  6]
#  [ 8 10 12]]
```

---

### 🎯 PHASE 1 EXERCISES

#### Beginner Exercises

**Exercise 1: Array Creation**
```python
# Create the following arrays:
# 1. Array of numbers from 1 to 20
# 2. 5x5 matrix of zeros
# 3. 3x3 identity matrix
# 4. Array of 10 random numbers between 0 and 1
# 5. Array of even numbers from 0 to 50
```

<details>
<summary>Solution</summary>

```python
# 1
arr1 = np.arange(1, 21)

# 2
arr2 = np.zeros((5, 5))

# 3
arr3 = np.eye(3)

# 4
arr4 = np.random.random(10)

# 5
arr5 = np.arange(0, 51, 2)
```
</details>

**Exercise 2: Indexing Practice**
```python
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

# Extract:
# 1. The number 60
# 2. The last row
# 3. The first column
# 4. The 2x2 subarray in the top-left
# 5. Every other element in the second row
```

<details>
<summary>Solution</summary>

```python
# 1
print(arr[1, 1])  # 60

# 2
print(arr[-1])  # or arr[2]

# 3
print(arr[:, 0])

# 4
print(arr[0:2, 0:2])

# 5
print(arr[1, ::2])
```
</details>

**Exercise 3: Boolean Indexing**
```python
temperatures = np.array([72, 68, 75, 82, 79, 65, 71, 88, 90, 67])

# Find:
# 1. All temperatures above 75
# 2. All temperatures between 70 and 80 (inclusive)
# 3. Replace all temperatures below 70 with 70
```

<details>
<summary>Solution</summary>

```python
# 1
hot_temps = temperatures[temperatures > 75]

# 2
moderate = temperatures[(temperatures >= 70) & (temperatures <= 80)]

# 3
temperatures[temperatures < 70] = 70
```
</details>

---

## PHASE 2: INTERMEDIATE OPERATIONS (Week 3-4)

### 2.1 Broadcasting - The Secret Weapon

#### What is Broadcasting?

**Simple Explanation:** Broadcasting is NumPy's way of performing operations on arrays of different shapes without copying data.

**Analogy:** 
Imagine you want to add $10 to each person's salary:
- Bad way: Write $10 ten thousand times
- Good way (Broadcasting): Just say "add $10 to everyone"

#### Broadcasting Rules

NumPy compares array shapes element-wise:

```
Rule 1: If arrays have different dimensions, pad with 1s on the left
Rule 2: Arrays are compatible if dimensions are equal OR one is 1
Rule 3: Result shape is element-wise maximum
```

#### Example 1: Scalar Broadcasting

```python
arr = np.array([1, 2, 3])
result = arr + 5

# What happens:
# arr:    [1, 2, 3]  shape (3,)
# 5:      5          shape ()
# Result: [6, 7, 8]  shape (3,)
```

#### Example 2: 1D + 1D Broadcasting

```python
# These must have same shape - NO broadcasting
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2  # [11, 22, 33]

# Different shapes - ERROR
arr3 = np.array([1, 2])
# arr1 + arr3  # ValueError!
```

#### Example 3: 2D + 1D Broadcasting (Row-wise)

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])  # Shape: (2, 3)

row = np.array([10, 20, 30])   # Shape: (3,)

result = matrix + row
# Output:
# [[11 22 33]
#  [14 25 36]]

# Visualization:
# [[1, 2, 3]    [10, 20, 30]    [[11, 22, 33]
#  [4, 5, 6]]  + [10, 20, 30]  =  [14, 25, 36]]
#                  ↑ broadcasts
```

#### Example 4: 2D + 1D Broadcasting (Column-wise)

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])     # Shape: (2, 3)

col = np.array([[10],
                [20]])             # Shape: (2, 1)

result = matrix + col
# Output:
# [[11 12 13]
#  [24 25 26]]

# Visualization:
# [[1, 2, 3]    [[10, 10, 10]    [[11, 12, 13]
#  [4, 5, 6]]  +  [20, 20, 20]]  =  [24, 25, 26]]
#                  ↑ broadcasts
```

#### Example 5: 2D + 2D Broadcasting

```python
a = np.array([[1, 2, 3]])     # Shape: (1, 3)
b = np.array([[10],
              [20],
              [30]])          # Shape: (3, 1)

result = a + b
# Output:
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# Visualization of shapes:
# (1, 3) + (3, 1) → (3, 3)
```

#### Real-World Example: Normalize Data

```python
# Dataset: 100 samples, 5 features
data = np.random.randn(100, 5) * 10 + 50

# Calculate mean for each feature
mean = data.mean(axis=0)  # Shape: (5,)
print(mean.shape)         # (5,)

# Calculate std for each feature
std = data.std(axis=0)    # Shape: (5,)

# Normalize (subtract mean, divide by std)
normalized = (data - mean) / std  # Broadcasting!

print(normalized.mean(axis=0))  # [~0, ~0, ~0, ~0, ~0]
print(normalized.std(axis=0))   # [~1, ~1, ~1, ~1, ~1]
```

**Without Broadcasting (Bad):**
```python
# DON'T DO THIS!
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        normalized[i, j] = (data[i, j] - mean[j]) / std[j]
```

#### Common Broadcasting Patterns

```python
# Pattern 1: Add row vector to matrix
matrix = np.ones((3, 4))
row = np.array([1, 2, 3, 4])
result = matrix + row  # (3, 4) + (4,) → (3, 4)

# Pattern 2: Add column vector to matrix
col = np.array([[1], [2], [3]])
result = matrix + col  # (3, 4) + (3, 1) → (3, 4)

# Pattern 3: Outer product-like operation
a = np.array([1, 2, 3])[:, np.newaxis]  # (3, 1)
b = np.array([4, 5, 6, 7])              # (4,)
result = a * b  # (3, 1) * (4,) → (3, 4)
```

#### keepdims Parameter (Important!)

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Without keepdims
mean1 = arr.mean(axis=0)
print(mean1.shape)  # (3,)

# With keepdims
mean2 = arr.mean(axis=0, keepdims=True)
print(mean2.shape)  # (1, 3) - preserves 2D structure!

# Why this matters:
centered1 = arr - mean1       # Works (broadcasting)
centered2 = arr - mean2       # Also works, more explicit
```

---

### 2.2 Universal Functions (ufuncs)

#### What are ufuncs?

**Definition:** Functions that operate element-wise on arrays, optimized in C.

#### Mathematical ufuncs

```python
arr = np.array([1, 4, 9, 16, 25])

# Square root
print(np.sqrt(arr))
# Output: [1. 2. 3. 4. 5.]

# Exponential
print(np.exp(arr))
# Output: [2.71828183e+00 5.45981500e+01 8.10308393e+03 ...]

# Natural log
print(np.log(arr))
# Output: [0.         1.38629436 2.19722458 2.77258872 3.21887582]

# Base-10 log
print(np.log10(arr))

# Power
print(np.power(arr, 2))  # Same as arr ** 2

# Absolute value
arr2 = np.array([-1, -2, 3, -4])
print(np.abs(arr2))
# Output: [1 2 3 4]
```

#### Trigonometric ufuncs

```python
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))

# Inverse trig
print(np.arcsin([0, 0.5, 1]))
print(np.arccos([1, 0.5, 0]))
print(np.arctan([0, 1, np.inf]))

# Convert degrees/radians
degrees = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(degrees)
back = np.rad2deg(radians)
```

#### Rounding ufuncs

```python
arr = np.array([1.2, 1.5, 1.7, 2.3, 2.5, 2.8])

print(np.round(arr))      # [1. 2. 2. 2. 2. 3.]
print(np.floor(arr))      # [1. 1. 1. 2. 2. 2.]
print(np.ceil(arr))       # [2. 2. 2. 3. 3. 3.]
print(np.trunc(arr))      # [1. 1. 1. 2. 2. 2.]

# Round to decimal places
print(np.round(arr, decimals=1))  # [1.2 1.5 1.7 2.3 2.5 2.8]
```

#### Comparison ufuncs

```python
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Element-wise maximum
print(np.maximum(arr1, arr2))
# Output: [5 4 3 4 5]

# Element-wise minimum
print(np.minimum(arr1, arr2))
# Output: [1 2 3 2 1]

# Clip values to range
arr = np.array([1, 5, 10, 15, 20])
print(np.clip(arr, 5, 15))
# Output: [ 5  5 10 15 15]
```

#### Conditional ufuncs

```python
# np.where: like ternary operator for arrays
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3, 'big', 'small')
# Output: ['small' 'small' 'small' 'big' 'big']

# With numbers
result = np.where(arr > 3, arr * 10, arr)
# Output: [ 1  2  3 40 50]

# np.select: multiple conditions
conditions = [arr < 2, arr < 4, arr >= 4]
choices = ['tiny', 'small', 'large']
result = np.select(conditions, choices)
# Output: ['tiny' 'small' 'small' 'large' 'large']
```

#### Custom ufuncs

```python
# Vectorize Python function
def my_function(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

# Create vectorized version
vectorized = np.vectorize(my_function)

arr = np.array([-1, 0.5, 1.5, 2])
result = vectorized(arr)
# Output: [0.  0.5 1.  1. ]
```

---

### 2.3 Aggregations & Statistics

#### Basic Aggregations

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Sum of all elements
print(arr.sum())           # 45

# Minimum and maximum
print(arr.min())           # 1
print(arr.max())           # 9

# Mean, median, std
print(arr.mean())          # 5.0
print(np.median(arr))      # 5.0
print(arr.std())           # 2.581988897471611

# Variance
print(arr.var())           # 6.666666666666667
```

#### Axis-based Aggregations

**Understanding axis:**
```
2D Array:
axis=0 ↓ (down columns)
axis=1 → (across rows)

Example:
[[1, 2, 3]
 [4, 5, 6]]

axis=0: [5, 7, 9]  (sum down each column)
axis=1: [6, 15]    (sum across each row)
```

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Sum along axis 0 (down columns)
print(arr.sum(axis=0))
# Output: [12 15 18]

# Sum along axis 1 (across rows)
print(arr.sum(axis=1))
# Output: [ 6 15 24]

# Mean of each column
print(arr.mean(axis=0))
# Output: [4. 5. 6.]

# Max of each row
print(arr.max(axis=1))
# Output: [3 6 9]
```

#### Cumulative Operations

```python
arr = np.array([1, 2, 3, 4, 5])

# Cumulative sum
print(np.cumsum(arr))
# Output: [ 1  3  6 10 15]

# Cumulative product
print(np.cumprod(arr))
# Output: [  1   2   6  24 120]

# 2D cumulative sum
arr2d = np.array([[1, 2], [3, 4]])
print(np.cumsum(arr2d, axis=0))
# Output:
# [[1 2]
#  [4 6]]
```

#### Percentiles & Quantiles

```python
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Percentiles
print(np.percentile(data, 25))   # 3.25 (25th percentile)
print(np.percentile(data, 50))   # 5.5  (median)
print(np.percentile(data, 75))   # 7.75 (75th percentile)

# Multiple percentiles at once
print(np.percentile(data, [25, 50, 75]))
# Output: [3.25 5.5  7.75]

# Quantiles (0-1 instead of 0-100)
print(np.quantile(data, 0.25))  # Same as 25th percentile
```

#### Correlation & Covariance

```python
# Two variables
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Correlation coefficient
correlation = np.corrcoef(x, y)
print(correlation)
# Output:
# [[1.   0.78]
#  [0.78 1.  ]]

# Covariance
covariance = np.cov(x, y)
print(covariance)

# For multiple variables (common in ML)
data = np.random.randn(100, 5)  # 100 samples, 5 features
correlation_matrix = np.corrcoef(data.T)
print(correlation_matrix.shape)  # (5, 5)
```

#### Finding Indices

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Index of minimum/maximum
print(np.argmin(arr))  # 1
print(np.argmax(arr))  # 5

# Indices that would sort array
print(np.argsort(arr))
# Output: [1 3 6 0 2 4 7 5]

# 2D argmax
arr2d = np.array([[1, 2, 3],
                  [6, 5, 4]])
print(np.argmax(arr2d, axis=0))  # [1 1 1] - max in each column
print(np.argmax(arr2d, axis=1))  # [2 0] - max in each row
```

---

### 2.4 Array Manipulation

#### Reshaping Arrays

```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]

# Reshape to 2D
arr_2d = arr.reshape(3, 4)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Reshape to 3D
arr_3d = arr.reshape(2, 3, 2)
print(arr_3d.shape)  # (2, 3, 2)

# Use -1 to auto-calculate dimension
arr_2d = arr.reshape(3, -1)  # Auto-calculates 4 columns
arr_2d = arr.reshape(-1, 4)  # Auto-calculates 3 rows

# Flatten to 1D
flattened = arr_2d.flatten()
# or
flattened = arr_2d.ravel()  # Returns view if possible
```

#### Transposing

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Transpose
transposed = arr.T
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# 3D transpose
arr3d = np.random.randn(2, 3, 4)
print(arr3d.shape)         # (2, 3, 4)
print(arr3d.T.shape)       # (4, 3, 2)

# Custom transpose
print(arr3d.transpose(2, 0, 1).shape)  # (4, 2, 3)
```

#### Stacking Arrays

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical stack (rows)
vstacked = np.vstack([arr1, arr2])
# Output:
# [[1 2 3]
#  [4 5 6]]

# Horizontal stack (columns)
hstacked = np.hstack([arr1, arr2])
# Output: [1 2 3 4 5 6]

# 2D example
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])

horizontal = np.hstack([a, b])
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# Depth stack (3D)
dstacked = np.dstack([arr1, arr2])
print(dstacked.shape)  # (1, 3, 2)

# General concatenate
concatenated = np.concatenate([arr1, arr2])
# Output: [1 2 3 4 5 6]
```

#### Splitting Arrays

```python
arr = np.arange(12)

# Split into 3 equal parts
split = np.split(arr, 3)
# Output: [array([0, 1, 2, 3]), array([4, 5, 6, 7]), array([ 8,  9, 10, 11])]

# Split at specific indices
split = np.split(arr, [3, 7])
# Output: [array([0, 1, 2]), array([3, 4, 5, 6]), array([ 7,  8,  9, 10, 11])]

# 2D split
arr2d = np.arange(16).reshape(4, 4)
vsplit = np.vsplit(arr2d, 2)  # Split rows
hsplit = np.hsplit(arr2d, 2)  # Split columns
```

#### Adding/Removing Elements

```python
arr = np.array([1, 2, 3, 4, 5])

# Append (creates new array)
new_arr = np.append(arr, [6, 7])
# Output: [1 2 3 4 5 6 7]

# Insert at position
new_arr = np.insert(arr, 2, 99)
# Output: [ 1  2 99  3  4  5]

# Delete elements
new_arr = np.delete(arr, [1, 3])
# Output: [1 3 5]

# ⚠️ These create new arrays - inefficient in loops!
```

#### Repeating & Tiling

```python
arr = np.array([1, 2, 3])

# Repeat each element
repeated = np.repeat(arr, 3)
# Output: [1 1 1 2 2 2 3 3 3]

# Tile entire array
tiled = np.tile(arr, 3)
# Output: [1 2 3 1 2 3 1 2 3]

# 2D tiling
tiled_2d = np.tile(arr, (2, 3))
# Output:
# [[1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]]
```

---

### 🎯 PHASE 2 EXERCISES

**Exercise 1: Broadcasting**
```python
# You have test scores for 5 students across 4 exams
scores = np.array([[78, 85, 92, 88],
                   [92, 88, 84, 90],
                   [75, 80, 85, 82],
                   [88, 92, 95, 91],
                   [82, 78, 88, 85]])

# 1. Curve all scores by adding 5 points
# 2. Calculate average score for each student
# 3. Calculate average score for each exam
# 4. Normalize each exam's scores (subtract exam mean, divide by exam std)
```

**Exercise 2: Real-World Data Processing**
```python
# Monthly sales data for 12 months, 5 products
sales = np.random.randint(100, 1000, size=(12, 5))

# Tasks:
# 1. Find total sales for each product
# 2. Find which month had highest total sales
# 3. Find which product had most consistent sales (lowest std)
# 4. Calculate year-over-year growth if next year's data is:
next_year = np.random.randint(120, 1200, size=(12, 5))
```

---

## PHASE 3: ADVANCED TECHNIQUES (Week 5-6)

### 3.1 Linear Algebra

#### Matrix Multiplication

```python
# DOT PRODUCT (1D arrays)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)  # 1*4 + 2*5 + 3*6 = 32

# MATRIX MULTIPLICATION
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Three equivalent ways:
C = np.dot(A, B)
C = A @ B           # Preferred (Python 3.5+)
C = np.matmul(A, B)

print(C)
# Output:
# [[19 22]
#  [43 50]]

# Calculation:
# C[0,0] = 1*5 + 2*7 = 19
# C[0,1] = 1*6 + 2*8 = 22
# C[1,0] = 3*5 + 4*7 = 43
# C[1,1] = 3*6 + 4*8 = 50
```

**Shape Rules:**
```
(m, n) @ (n, p) → (m, p)
(3, 4) @ (4, 2) → (3, 2) ✅
(3, 4) @ (5, 2) → ERROR   ❌
```

#### Matrix Operations

```python
A = np.array([[1, 2],
              [3, 4]])

# Transpose
print(A.T)
# Output:
# [[1 3]
#  [2 4]]

# Inverse (only for square, non-singular matrices)
A_inv = np.linalg.inv(A)
print(A @ A_inv)  # Identity matrix (approximately)
# Output:
# [[1. 0.]
#  [0. 1.]]

# Determinant
det = np.linalg.det(A)
print(det)  # -2.0

# Trace (sum of diagonal)
trace = np.trace(A)
print(trace)  # 5

# Rank
rank = np.linalg.matrix_rank(A)
print(rank)  # 2
```

#### Solving Linear Systems

**Problem:** Solve Ax = b

```python
# System of equations:
# 2x + 3y = 8
# 4x + 5y = 14

A = np.array([[2, 3],
              [4, 5]])
b = np.array([8, 14])

# Solve
x = np.linalg.solve(A, b)
print(x)  # [1. 2.]

# Verify
print(A @ x)  # [8. 14.] ✅
```

**Overdetermined System (least squares):**

```python
# More equations than unknowns
A = np.array([[1, 1],
              [1, 2],
              [1, 3]])
b = np.array([2, 3, 4])

# Least squares solution
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
print(x)  # Best fit solution
```

#### Eigenvalues & Eigenvectors

```python
A = np.array([[4, 2],
              [1, 3]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Verify: A @ v = λ @ v
v1 = eigenvectors[:, 0]
lambda1 = eigenvalues[0]
print(A @ v1)           # A times first eigenvector
print(lambda1 * v1)     # Should be equal
```

#### Singular Value Decomposition (SVD)

```python
# Any matrix can be decomposed: A = U @ S @ Vt
A = np.random.randn(5, 3)

U, s, Vt = np.linalg.svd(A)

print(U.shape)   # (5, 5)
print(s.shape)   # (3,) - singular values
print(Vt.shape)  # (3, 3)

# Reconstruct original matrix
S = np.zeros((5, 3))
S[:3, :3] = np.diag(s)
A_reconstructed = U @ S @ Vt
print(np.allclose(A, A_reconstructed))  # True

# Low-rank approximation (compression)
k = 2  # Keep top 2 singular values
S_compressed = S.copy()
S_compressed[k:, :] = 0
A_compressed = U @ S_compressed @ Vt
```

---

### 3.2 Advanced Indexing Techniques

#### np.where - Conditional Selection

```python
arr = np.array([1, -2, 3, -4, 5, -6])

# Replace negatives with 0
result = np.where(arr < 0, 0, arr)
# Output: [1 0 3 0 5 0]

# Multiple conditions (nested where)
# Positive → 1, Negative → -1, Zero → 0
result = np.where(arr > 0, 1, np.where(arr < 0, -1, 0))

# Get indices of True values
indices = np.where(arr > 0)
print(indices)  # (array([0, 2, 4]),)
print(arr[indices])  # [1 3 5]
```

#### np.argmax / np.argmin

```python
arr = np.array([10, 25, 15, 30, 20])

# Index of maximum
max_idx = np.argmax(arr)
print(max_idx)  # 3
print(arr[max_idx])  # 30

# 2D array
arr_2d = np.array([[1, 5, 3],
                   [9, 2, 8],
                   [4, 7, 6]])

# Flat index of maximum
print(np.argmax(arr_2d))  # 3 (element at row 1, col 0)

# Index in each row
print(np.argmax(arr_2d, axis=1))  # [1 0 1]

# Index in each column
print(np.argmax(arr_2d, axis=0))  # [1 2 1]
```

#### np.argsort - Sorting Indices

```python
arr = np.array([30, 10, 50, 20, 40])

# Indices that would sort array (ascending)
sorted_indices = np.argsort(arr)
print(sorted_indices)  # [1 3 0 4 2]
print(arr[sorted_indices])  # [10 20 30 40 50]

# Descending order
desc_indices = np.argsort(arr)[::-1]
print(arr[desc_indices])  # [50 40 30 20 10]

# Practical: Get top 3 students by score
students = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
scores = np.array([85, 92, 78, 95, 88])

top_3_indices = np.argsort(scores)[-3:][::-1]
print(students[top_3_indices])
# Output: ['David' 'Bob' 'Eve']
```

#### np.unique - Unique Values

```python
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Get unique values
unique = np.unique(arr)
print(unique)  # [1 2 3 4]

# With counts
values, counts = np.unique(arr, return_counts=True)
print(values)  # [1 2 3 4]
print(counts)  # [1 2 3 4]

# Most frequent value
most_frequent = values[np.argmax(counts)]
print(most_frequent)  # 4

# With indices
values, indices = np.unique(arr, return_inverse=True)
print(indices)
# Indices to reconstruct original: [0 1 1 2 2 2 3 3 3 3]
print(values[indices])  # Reconstructs original array
```

#### np.searchsorted - Binary Search

```python
# Sorted array (required!)
sorted_arr = np.array([1, 3, 5, 7, 9, 11])

# Find insertion index
idx = np.searchsorted(sorted_arr, 6)
print(idx)  # 3 (6 would go between 5 and 7)

# Multiple values
values = [2, 4, 8, 12]
indices = np.searchsorted(sorted_arr, values)
print(indices)  # [1 2 4 6]

# 'right' side insertion
idx_right = np.searchsorted(sorted_arr, 5, side='right')
print(idx_right)  # 3 (after 5)
```

#### Advanced Boolean Indexing

```python
# Multiple conditions
arr = np.arange(20)

# AND condition (&)
result = arr[(arr > 5) & (arr < 15)]
print(result)  # [ 6  7  8  9 10 11 12 13 14]

# OR condition (|)
result = arr[(arr < 5) | (arr > 15)]
print(result)  # [ 0  1  2  3  4 16 17 18 19]

# NOT condition (~)
result = arr[~((arr > 5) & (arr < 15))]
print(result)  # [ 0  1  2  3  4  5 15 16 17 18 19]

# 2D boolean indexing
matrix = np.random.randn(5, 5)

# Set all negatives to 0
matrix[matrix < 0] = 0

# Find rows where all elements > 0
rows_all_positive = (matrix > 0).all(axis=1)
positive_rows = matrix[rows_all_positive]
```

---

### 3.3 Memory Optimization & Performance

#### Understanding Views vs Copies

```python
arr = np.arange(10)

# VIEW (shares memory)
view = arr[::2]
print(view.base is arr)  # True

view[0] = 999
print(arr)  # [999   1   2   3   4   5   6   7   8   9]

# COPY (independent)
copy = arr[::2].copy()
print(copy.base is None)  # True

copy[0] = 777
print(arr)  # Unchanged

# Operations that create views:
# - Slicing: arr[1:5]
# - Reshaping: arr.reshape(2, 5)
# - Transposing: arr.T

# Operations that create copies:
# - arr.copy()
# - Fancy indexing: arr[[1, 3, 5]]
# - Boolean indexing: arr[arr > 5]
```

#### Memory-Mapped Files (Huge Datasets)

```python
# Create huge array on disk (not in RAM)
shape = (10000, 10000)
mmap = np.memmap('huge_data.dat', dtype='float32', 
                 mode='w+', shape=shape)

# Fill with data
mmap[:] = np.random.randn(*shape).astype('float32')
del mmap  # Flush to disk

# Read back (only loads what you need)
mmap = np.memmap('huge_data.dat', dtype='float32',
                 mode='r', shape=shape)

# Access subset (doesn't load entire array into RAM)
subset = mmap[:100, :100]
print(subset.mean())
```

#### Stride Tricks (Advanced)

```python
# Create sliding windows without copying data
from numpy.lib.stride_tricks import as_strided

arr = np.arange(10)
# Create windows of size 3 with stride 1
# [0,1,2], [1,2,3], [2,3,4], ...

windows = as_strided(arr, shape=(8, 3), strides=(8, 8))
print(windows)
# Output:
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]
#  [4 5 6]
#  [5 6 7]
#  [6 7 8]
#  [7 8 9]]

# ⚠️ Modifying windows modifies original!
```

#### Performance Best Practices

```python
import time

# ❌ BAD: Growing arrays in loop
def bad_way(n):
    arr = np.array([])
    for i in range(n):
        arr = np.append(arr, i)
    return arr

# ✅ GOOD: Preallocate
def good_way(n):
    arr = np.zeros(n)
    for i in range(n):
        arr[i] = i
    return arr

# ✅ BEST: Vectorize
def best_way(n):
    return np.arange(n)

# Test
n = 10000
start = time.time()
bad_way(n)
print(f"Bad:  {time.time() - start:.4f}s")

start = time.time()
good_way(n)
print(f"Good: {time.time() - start:.4f}s")

start = time.time()
best_way(n)
print(f"Best: {time.time() - start:.4f}s")
```

**Output (approximate):**
```
Bad:  0.5234s
Good: 0.0123s
Best: 0.0001s
```

#### Vectorization Examples

```python
# ❌ BAD: Explicit loops
def distance_loop(points1, points2):
    n = len(points1)
    distances = np.zeros(n)
    for i in range(n):
        distances[i] = np.sqrt((points1[i,0] - points2[i,0])**2 + 
                               (points1[i,1] - points2[i,1])**2)
    return distances

# ✅ GOOD: Vectorized
def distance_vectorized(points1, points2):
    diff = points1 - points2
    return np.sqrt((diff**2).sum(axis=1))

# Test
points1 = np.random.randn(100000, 2)
points2 = np.random.randn(100000, 2)

# Time comparison shows ~100x speedup!
```

---

### 3.4 Working with NaN and Infinity

```python
# Create array with NaN
arr = np.array([1, 2, np.nan, 4, 5, np.nan])

# Check for NaN
print(np.isnan(arr))
# Output: [False False  True False False  True]

# Count NaNs
print(np.isnan(arr).sum())  # 2

# Remove NaNs
clean = arr[~np.isnan(arr)]
print(clean)  # [1. 2. 4. 5.]

# NaN-aware functions
print(np.nanmean(arr))    # 3.0 (ignores NaN)
print(np.nanstd(arr))     # Std ignoring NaN
print(np.nansum(arr))     # 12.0

# Replace NaN
arr_filled = np.where(np.isnan(arr), 0, arr)
# Or
arr_filled = np.nan_to_num(arr, nan=0.0)

# Infinity
arr_inf = np.array([1, 2, np.inf, -np.inf, 5])
print(np.isinf(arr_inf))
# Output: [False False  True  True False]

print(np.isfinite(arr_inf))
# Output: [ True  True False False  True]
```

---

## PHASE 4: INDUSTRIAL APPLICATIONS (Week 7-8)

### 4.1 Image Processing with NumPy

#### Loading and Basic Operations

```python
from PIL import Image
import numpy as np

# Load image as array
img = np.array(Image.open('photo.jpg'))
print(img.shape)  # (height, width, 3) for RGB

# Image properties
print(f"Height: {img.shape[0]}")
print(f"Width: {img.shape[1]}")
print(f"Channels: {img.shape[2]}")
print(f"Data type: {img.dtype}")  # Usually uint8

# Access specific pixel
pixel = img[100, 200]  # [R, G, B]
print(pixel)

# Separate color channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]
```

#### Image Transformations

```python
# Grayscale conversion
gray = img.mean(axis=2)
# Or weighted (more accurate)
gray = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]

# Flip vertically
flipped_v = img[::-1, :, :]

# Flip horizontally
flipped_h = img[:, ::-1, :]

# Rotate 90 degrees
rotated = np.rot90(img)

# Crop
cropped = img[100:400, 200:500, :]

# Resize (simple nearest neighbor)
def resize_simple(img, new_height, new_width):
    h, w = img.shape[:2]
    row_indices = (np.arange(new_height) * h / new_height).astype(int)
    col_indices = (np.arange(new_width) * w / new_width).astype(int)
    return img[row_indices[:, np.newaxis], col_indices, :]
```

#### Image Adjustments

```python
# Brightness
def adjust_brightness(img, factor):
    result = img.astype(float) * factor
    return np.clip(result, 0, 255).astype(np.uint8)

bright = adjust_brightness(img, 1.5)  # 50% brighter
dark = adjust_brightness(img, 0.7)    # 30% darker

# Contrast
def adjust_contrast(img, factor):
    mean = img.mean()
    result = mean + factor * (img - mean)
    return np.clip(result, 0, 255).astype(np.uint8)

# Negative
negative = 255 - img

# Threshold (create binary image)
gray = img.mean(axis=2)
binary = (gray > 128).astype(np.uint8) * 255
```

#### Simple Filters

```python
# Box blur (averaging)
def box_blur(img, kernel_size=5):
    k = kernel_size
    blurred = np.zeros_like(img)
    
    for i in range(k//2, img.shape[0] - k//2):
        for j in range(k//2, img.shape[1] - k//2):
            blurred[i, j] = img[i-k//2:i+k//2+1, 
                                j-k//2:j+k//2+1].mean(axis=(0,1))
    return blurred

# Edge detection (simple gradient)
def edge_detection(gray_img):
    # Horizontal gradient
    gx = np.diff(gray_img, axis=1)
    # Vertical gradient
    gy = np.diff(gray_img, axis=0)
    
    # Combine
    edges = np.sqrt(gx[:-1, :]**2 + gy[:, :-1]**2)
    return edges
```

---

### 4.2 Signal Processing

#### Signal Generation

```python
# Time array
duration = 1  # seconds
sample_rate = 1000  # Hz
t = np.linspace(0, duration, sample_rate * duration)

# Sine wave
freq = 5  # Hz
signal = np.sin(2 * np.pi * freq * t)

# Complex signal (multiple frequencies)
signal = (np.sin(2*np.pi*5*t) + 
          0.5*np.sin(2*np.pi*10*t) + 
          0.3*np.sin(2*np.pi*20*t))

# Add noise
noise = np.random.randn(len(signal)) * 0.2
noisy_signal = signal + noise
```

#### Moving Average Filter

```python
def moving_average(signal, window_size):
    """Simple moving average filter"""
    kernel = np.ones(window_size) / window_size
    return np.convolve(signal, kernel, mode='same')

# Apply filter
filtered = moving_average(noisy_signal, window_size=20)
```

#### Fourier Transform (Frequency Analysis)

```python
# Perform FFT
fft = np.fft.fft(noisy_signal)
frequencies = np.fft.fftfreq(len(noisy_signal), 1/sample_rate)

# Power spectrum
power = np.abs(fft)**2

# Find dominant frequencies (positive side only)
positive_freq = frequencies[:len(frequencies)//2]
positive_power = power[:len(power)//2]

# Get top 5 frequencies
top_indices = np.argsort(positive_power)[-5:]
dominant_freqs = positive_freq[top_indices]

print(f"Dominant frequencies: {dominant_freqs} Hz")

# Inverse FFT (reconstruct signal)
reconstructed = np.fft.ifft(fft).real
```

#### Peak Detection

```python
def find_peaks(signal, threshold):
    """Find local maxima above threshold"""
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > threshold:
            if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
                peaks.append(i)
    return np.array(peaks)

# Find peaks
peak_indices = find_peaks(signal, threshold=0.8)
peak_values = signal[peak_indices]
peak_times = t[peak_indices]
```

---

### 4.3 Machine Learning Utilities

#### Data Preprocessing

```python
# Train/Test Split
def train_test_split(X, y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)
    
    n = len(X)
    indices = np.random.permutation(n)
    test_size = int(n * test_size)
    
    test_idx = indices[:test_size]
    train_idx = indices[test_size:]
    
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

# Standardization
def standardize(X):
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    return (X - mean) / std, mean, std

# Min-Max Normalization
def normalize(X, feature_range=(0, 1)):
    min_val = X.min(axis=0)
    max_val = X.max(axis=0)
    scaled = (X - min_val) / (max_val - min_val)
    
    if feature_range != (0, 1):
        a, b = feature_range
        scaled = a + scaled * (b - a)
    
    return scaled, min_val, max_val
```

#### One-Hot Encoding

```python
def one_hot_encode(labels, num_classes=None):
    """Convert integer labels to one-hot vectors"""
    if num_classes is None:
        num_classes = labels.max() + 1
    
    n_samples = len(labels)
    one_hot = np.zeros((n_samples, num_classes))
    one_hot[np.arange(n_samples), labels] = 1
    
    return one_hot

# Example
labels = np.array([0, 1, 2, 1, 0])
one_hot = one_hot_encode(labels)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]]
```

#### Batch Generation

```python
def batch_generator(X, y, batch_size=32, shuffle=True):
    """Generate batches for training"""
    n_samples = len(X)
    indices = np.arange(n_samples)
    
    if shuffle:
        np.random.shuffle(indices)
    
    for start in range(0, n_samples, batch_size):
        end = min(start + batch_size, n_samples)
        batch_idx = indices[start:end]
        yield X[batch_idx], y[batch_idx]

# Usage
X = np.random.randn(1000, 10)
y = np.random.randint(0, 5, 1000)

for X_batch, y_batch in batch_generator(X, y, batch_size=32):
    # Train on batch
    pass
```

#### Confusion Matrix

```python
def confusion_matrix(y_true, y_pred, num_classes):
    """Compute confusion matrix"""
    matrix = np.zeros((num_classes, num_classes), dtype=int)
    
    for true, pred in zip(y_true, y_pred):
        matrix[true, pred] += 1
    
    return matrix

# Example
y_true = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
y_pred = np.array([0, 1, 2, 0, 2, 2, 0, 1, 1])

cm = confusion_matrix(y_true, y_pred, num_classes=3)
print(cm)
# Output:
# [[3 0 0]
#  [0 2 1]
#  [0 1 2]]

# Accuracy from confusion matrix
accuracy = np.diag(cm).sum() / cm.sum()
print(f"Accuracy: {accuracy:.2%}")
```

#### Accuracy Metrics

```python
def accuracy(y_true, y_pred):
    return (y_true == y_pred).mean()

def precision_recall_f1(y_true, y_pred, class_label):
    # True Positives
    tp = ((y_pred == class_label) & (y_true == class_label)).sum()
    # False Positives
    fp = ((y_pred == class_label) & (y_true != class_label)).sum()
    # False Negatives
    fn = ((y_pred != class_label) & (y_true == class_label)).sum()
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    if precision + recall > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0
    
    return precision, recall, f1
```

---

### 4.4 Financial Analysis

```python
# Stock price simulation
def simulate_stock_prices(S0, mu, sigma, days, n_simulations):
    """
    Simulate stock prices using Geometric Brownian Motion
    
    S0: Initial price
    mu: Expected return (annual)
    sigma: Volatility (annual)
    days: Number of trading days
    n_simulations: Number of paths to simulate
    """
    dt = 1/252  # Daily timestep
    
    # Generate random returns
    returns = np.random.normal(
        (mu - 0.5 * sigma**2) * dt,
        sigma * np.sqrt(dt),
        (days, n_simulations)
    )
    
    # Convert to prices
    price_paths = S0 * np.exp(np.cumsum(returns, axis=0))
    
    return price_paths

# Simulate
prices = simulate_stock_prices(S0=100, mu=0.1, sigma=0.2, 
                                days=252, n_simulations=1000)

# Portfolio metrics
def portfolio_metrics(returns):
    """Calculate common portfolio metrics"""
    # Returns should be a (time, assets) array
    
    # Expected returns
    mean_returns = returns.mean(axis=0)
    
    # Volatility
    volatility = returns.std(axis=0)
    
    # Sharpe ratio (assuming risk-free rate = 0)
    sharpe = mean_returns / volatility
    
    # Correlation matrix
    correlation = np.corrcoef(returns.T)
    
    # Maximum drawdown
    cumulative = (1 + returns).cumprod(axis=0)
    running_max = np.maximum.accumulate(cumulative, axis=0)
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min(axis=0)
    
    return {
        'mean_returns': mean_returns,
        'volatility': volatility,
        'sharpe_ratio': sharpe,
        'correlation': correlation,
        'max_drawdown': max_drawdown
    }

# Calculate daily returns
daily_returns = np.diff(prices, axis=0) / prices[:-1]
metrics = portfolio_metrics(daily_returns)
```

---

## MAJOR PROJECTS

### Project 1: Image Compression using SVD

```python
def compress_image_svd(image_path, n_components):
    """
    Compress image using Singular Value Decomposition
    
    Returns compressed image and compression ratio
    """
    from PIL import Image
    
    # Load image
    img = np.array(Image.open(image_path))
    
    # Process each color channel
    compressed_channels = []
    
    for channel in range(3):  # RGB
        # Get channel data
        channel_data = img[:, :, channel]
        
        # Perform SVD
        U, s, Vt = np.linalg.svd(channel_data, full_matrices=False)
        
        # Keep only top n components
        U_reduced = U[:, :n_components]
        s_reduced = s[:n_components]
        Vt_reduced = Vt[:n_components, :]
        
        # Reconstruct
        compressed = U_reduced @ np.diag(s_reduced) @ Vt_reduced
        compressed_channels.append(compressed)
    
    # Stack channels
    compressed_img = np.stack(compressed_channels, axis=2)
    compressed_img = np.clip(compressed_img, 0, 255).astype(np.uint8)
    
    # Calculate compression ratio
    original_size = img.size
    compressed_size = (U_reduced.size + s_reduced.size + Vt_reduced.size) * 3
    compression_ratio = original_size / compressed_size
    
    print(f"Original size: {original_size:,} values")
    print(f"Compressed size: {compressed_size:,} values")
    print(f"Compression ratio: {compression_ratio:.2f}x")
    print(f"Space saved: {(1 - 1/compression_ratio)*100:.1f}%")
    
    return compressed_img, compression_ratio

# Usage
# compressed, ratio = compress_image_svd('photo.jpg', n_components=50)
# Image.fromarray(compressed).save('compressed.jpg')
```

### Project 2: K-Means Clustering from Scratch

```python
def kmeans(X, n_clusters, max_iters=100, random_state=None):
    """
    K-Means clustering algorithm
    
    X: Data array (n_samples, n_features)
    n_clusters: Number of clusters
    max_iters: Maximum iterations
    random_state: Random seed
    
    Returns: labels, centroids, inertia
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    # Initialize centroids randomly
    n_samples = X.shape[0]
    indices = np.random.choice(n_samples, n_clusters, replace=False)
    centroids = X[indices].copy()
    
    for iteration in range(max_iters):
        # Assign clusters
        # Calculate distances to all centroids
        distances = np.sqrt(((X[:, np.newaxis, :] - centroids) ** 2).sum(axis=2))
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([
            X[labels == k].mean(axis=0) for k in range(n_clusters)
        ])
        
        # Check convergence
        if np.allclose(centroids, new_centroids):
            print(f"Converged in {iteration + 1} iterations")
            break
        
        centroids = new_centroids
    
    # Calculate inertia (sum of squared distances to nearest centroid)
    final_distances = np.sqrt(((X - centroids[labels]) ** 2).sum(axis=1))
    inertia = (final_distances ** 2).sum()
    
    return labels, centroids, inertia

# Example usage
# Generate sample data
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=300, centers=4, random_state=42)

# Apply K-Means
labels, centroids, inertia = kmeans(X, n_clusters=4, random_state=42)

print(f"Inertia: {inertia:.2f}")
print(f"Centroids:\n{centroids}")
```

### Project 3: Simple Neural Network

```python
class NeuralNetwork:
    """Simple feedforward neural network"""
    
    def __init__(self, layer_sizes):
        """
        layer_sizes: List of layer sizes
        Example: [784, 128, 64, 10] for MNIST
        """
        self.weights = []
        self.biases = []
        
        # Initialize weights and biases
        for i in range(len(layer_sizes) - 1):
            # He initialization
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * \
                np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            
            self.weights.append(w)
            self.biases.append(b)
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def relu_derivative(self, x):
        return (x > 0).astype(float)
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / exp_x.sum(axis=1, keepdims=True)
    
    def forward(self, X):
        """Forward pass"""
        activations = [X]
        zs = []
        
        # Hidden layers
        for i in range(len(self.weights) - 1):
            z = activations[-1] @ self.weights[i] + self.biases[i]
            zs.append(z)
            a = self.relu(z)
            activations.append(a)
        
        # Output layer
        z = activations[-1] @ self.weights[-1] + self.biases[-1]
        zs.append(z)
        output = self.softmax(z)
        activations.append(output)
        
        return activations, zs
    
    def backward(self, X, y, learning_rate=0.01):
        """Backward pass (one training step)"""
        m = X.shape[0]
        
        # Forward pass
        activations, zs = self.forward(X)
        
        # Compute output layer gradient
        dz = activations[-1] - y  # For cross-entropy + softmax
        
        # Backpropagate
        for i in reversed(range(len(self.weights))):
            # Gradients
            dw = activations[i].T @ dz / m
            db = dz.sum(axis=0, keepdims=True) / m
            
            # Update weights
            self.weights[i] -= learning_rate * dw
            self.biases[i] -= learning_rate * db
            
            # Propagate error to previous layer
            if i > 0:
                dz = (dz @ self.weights[i].T) * self.relu_derivative(zs[i-1])
    
    def train(self, X, y, epochs, batch_size=32, learning_rate=0.01):
        """Train the network"""
        n_samples = X.shape[0]
        
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            # Mini-batch training
            for start in range(0, n_samples, batch_size):
                end = min(start + batch_size, n_samples)
                X_batch = X_shuffled[start:end]
                y_batch = y_shuffled[start:end]
                
                self.backward(X_batch, y_batch, learning_rate)
            
            # Print progress
            if (epoch + 1) % 10 == 0:
                activations, _ = self.forward(X)
                predictions = np.argmax(activations[-1], axis=1)
                y_labels = np.argmax(y, axis=1)
                accuracy = (predictions == y_labels).mean()
                print(f"Epoch {epoch+1}/{epochs}, Accuracy: {accuracy:.4f}")
    
    def predict(self, X):
        """Make predictions"""
        activations, _ = self.forward(X)
        return np.argmax(activations[-1], axis=1)

# Example usage:
# Generate dummy data
# X_train = np.random.randn(1000, 20)
# y_train = one_hot_encode(np.random.randint(0, 3, 1000), 3)
# 
# nn = NeuralNetwork([20, 64, 32, 3])
# nn.train(X_train, y_train, epochs=100, learning_rate=0.01)
```

### Project 4: Principal Component Analysis (PCA)

```python
def pca(X, n_components):
    """
    Principal Component Analysis
    
    X: Data matrix (n_samples, n_features)
    n_components: Number of components to keep
    
    Returns: transformed data, components, explained variance
    """
    # Center the data
    mean = X.mean(axis=0)
    X_centered = X - mean
    
    # Covariance matrix
    cov_matrix = np.cov(X_centered.T)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sort by eigenvalue (descending)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Select top n components
    components = eigenvectors[:, :n_components]
    
    # Transform data
    X_transformed = X_centered @ components
    
    # Explained variance ratio
    explained_variance = eigenvalues / eigenvalues.sum()
    
    return X_transformed, components, explained_variance[:n_components], mean

# Example usage
# data = np.random.randn(1000, 50)  # 1000 samples, 50 features
# reduced, components, var_ratio, mean = pca(data, n_components=10)
# 
# print(f"Explained variance: {var_ratio.sum():.2%}")
# print(f"Shape before: {data.shape}")
# print(f"Shape after: {reduced.shape}")
```

---

## INDUSTRIAL BEST PRACTICES

### Code Organization

```python
# ✅ GOOD: Type hints, docstrings, clear names
def normalize_features(
    X: np.ndarray, 
    method: str = 'standardize'
) -> tuple[np.ndarray, dict]:
    """
    Normalize features using specified method.
    
    Parameters
    ----------
    X : np.ndarray
        Input array of shape (n_samples, n_features)
    method : str
        Normalization method ('standardize' or 'minmax')
    
    Returns
    -------
    X_normalized : np.ndarray
        Normalized data
    params : dict
        Normalization parameters for inverse transform
    
    Examples
    --------
    >>> X = np.random.randn(100, 5)
    >>> X_norm, params = normalize_features(X)
    >>> X_norm.mean(axis=0)  # Should be ~0
    array([0., 0., 0., 0., 0.])
    """
    if method == 'standardize':
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X_normalized = (X - mean) / std
        params = {'mean': mean, 'std': std, 'method': method}
    
    elif method == 'minmax':
        min_val = X.min(axis=0)
        max_val = X.max(axis=0)
        X_normalized = (X - min_val) / (max_val - min_val)
        params = {'min': min_val, 'max': max_val, 'method': method}
    
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return X_normalized, params
```

### Testing

```python
def test_pca():
    """Test PCA implementation"""
    # Generate known data
    X = np.random.randn(100, 10)
    
    # Apply PCA
    transformed, components, var_ratio, mean = pca(X, n_components=5)
    
    # Test shapes
    assert transformed.shape == (100, 5), "Wrong output shape"
    assert components.shape == (10, 5), "Wrong component shape"
    assert len(var_ratio) == 5, "Wrong variance ratio length"
    
    # Test orthogonality
    assert np.allclose(
        components.T @ components, 
        np.eye(5), 
        atol=1e-10
    ), "Components not orthogonal"
    
    # Test variance explained sum <= 1
    assert var_ratio.sum() <= 1.0, "Variance ratio > 1"
    
    print("✅ All PCA tests passed!")

test_pca()
```

### Performance Profiling

```python
import time
from functools import wraps

def timer(func):
    """Decorator to time functions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function(n):
    return sum([i**2 for i in range(n)])

@timer
def fast_function(n):
    return (np.arange(n)**2).sum()

# Test
slow_function(1000000)
fast_function(1000000)
```

### Error Handling

```python
def safe_divide(a, b):
    """Safely divide arrays, handling division by zero"""
    try:
        result = np.divide(
            a, b, 
            out=np.zeros_like(a, dtype=float),
            where=(b != 0)
        )
        return result
    except Exception as e:
        print(f"Error in division: {e}")
        return None

# Example
a = np.array([1, 2, 3, 4])
b = np.array([2, 0, 2, 0])
result = safe_divide(a, b)
# Output: [0.5 0.  1.5 0. ]
```

---

## LEARNING RESOURCES

### Official Documentation
- **NumPy Docs**: https://numpy.org/doc/
- **NumPy User Guide**: https://numpy.org/doc/stable/user/
- **NumPy API Reference**: https://numpy.org/doc/stable/reference/

### Books
1. **"From Python to NumPy"** by Nicolas P. Rougier (Free online)
2. **"Python Data Science Handbook"** by Jake VanderPlas
3. **"Numerical Python"** by Robert Johansson

### Online Courses
- **DataCamp**: NumPy courses
- **Coursera**: Scientific Computing with Python
- **Real Python**: NumPy tutorials

### Practice Platforms
- **LeetCode**: Array problems
- **HackerRank**: Python NumPy section
- **Project Euler**: Mathematical problems
- **Kaggle**: Data science competitions

### Advanced Topics
- SciPy (builds on NumPy)
- Pandas (uses NumPy)
- Scikit-learn (ML with NumPy)
- TensorFlow/PyTorch (Deep learning)

---

## DAILY PRACTICE SCHEDULE

### Week 1-2: Foundations
- **Day 1-2**: Array creation, attributes, data types
- **Day 3-4**: Indexing and slicing
- **Day 5-6**: Basic operations, broadcasting intro
- **Day 7**: Review + 10 practice problems

### Week 3-4: Intermediate
- **Day 8-9**: Broadcasting deep dive
- **Day 10-11**: Universal functions
- **Day 12-13**: Aggregations, statistics
- **Day 14**: Mini-project (financial analysis)

### Week 5-6: Advanced
- **Day 15-16**: Linear algebra
- **Day 17-18**: Advanced indexing
- **Day 19-20**: Memory optimization
- **Day 21**: Project (PCA or K-Means)

### Week 7-8: Applications
- **Day 22-23**: Image processing
- **Day 24-25**: Signal processing
- **Day 26-27**: ML utilities
- **Day 28**: Final project (Neural Network)

---

## QUICK REFERENCE CHEAT SHEET

### Array Creation
```python
np.array([1,2,3])              # From list
np.zeros((3,4))                # Zeros
np.ones((2,3))                 # Ones
np.arange(0, 10, 2)            # Range
np.linspace(0, 1, 5)           # Linear space
np.random.random((3,3))        # Random
np.eye(4)                      # Identity
```

### Indexing
```python
arr[0]                         # First element
arr[-1]                        # Last element
arr[1:5]                       # Slice
arr[arr > 5]                   # Boolean
arr[[0,2,4]]                   # Fancy
```

### Operations
```python
arr1 + arr2                    # Element-wise add
arr1 * arr2                    # Element-wise multiply
arr @ arr2                     # Matrix multiplication
arr.T                          # Transpose
arr.reshape(3,4)               # Reshape
```

### Aggregations
```python
arr.sum()                      # Sum all
arr.mean()                     # Mean
arr.std()                      # Standard deviation
arr.min(), arr.max()           # Min, max
np.median(arr)                 # Median
```

### Common Patterns
```python
# Normalize
(arr - arr.mean()) / arr.std()

# Find outliers
arr[np.abs(arr - arr.mean()) > 3*arr.std()]

# Replace negatives
np.where(arr < 0, 0, arr)

# Sort
arr[np.argsort(arr)]
```

---

## 🎯 FINAL TIPS FOR SUCCESS

1. **Practice Daily**: 30-60 minutes every day beats 8 hours once a week
2. **Type, Don't Copy**: Write code yourself, even examples
3. **Visualize**: Draw arrays on paper to understand operations
4. **Time Yourself**: Compare your solutions vs vectorized NumPy
5. **Read Source Code**: Check pandas, scikit-learn implementations
6. **Join Community**: Stack Overflow, Reddit r/learnpython
7. **Build Projects**: Apply to real problems you care about
8. **Teach Others**: Best way to solidify understanding

**Remember**: NumPy mastery comes from consistent practice, not cramming!

---
