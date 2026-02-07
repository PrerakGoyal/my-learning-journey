# 🐼 PANDAS MASTER NOTES — APEX TUTOR EDITION

**Author:** Prerak  
**Purpose:** Complete pandas guide from foundations to advanced analytics  
**Learning Approach:** Theory → Examples → Practice → Real-world Applications

---

## 📋 TABLE OF CONTENTS

1. [Session 1 — Pandas Foundations](#session-1--pandas-foundations)
2. [Session 2 — DataFrame Anatomy](#session-2--what-is-df--dataframe-anatomy)
3. [Session 3 — Data Storage & Types](#session-3--how-pandas-stores-data)
4. [Session 3.5 — iloc (Position-Based Indexing)](#session-35--iloc-position-based-indexing)
5. [Session 4 — Boolean Filtering](#session-4--boolean-filtering)
6. [Session 5 — loc + Boolean Filtering](#session-5--loc--boolean-filtering)
7. [Session 6 — Creating & Transforming Columns](#session-6--creating--transforming-columns)
8. [Session 7 — apply(), lambda, and groupby](#session-7--apply-lambda-and-groupby)
9. [Quick Reference Guide](#quick-reference-guide)
10. [Common Patterns & Best Practices](#common-patterns--best-practices)

---

# SESSION 1 — PANDAS FOUNDATIONS

## 1) What is pandas?

**Definition:**  
Pandas is a Python library for working with structured, table-like data (like Excel, but programmable and more powerful).

**Mental Model:**  
> Excel inside Python + superpowers + automation capabilities

**Why pandas matters:**
- Handles large datasets efficiently (millions of rows)
- Automates repetitive Excel tasks
- Integrates with data visualization libraries
- Essential for data science, analytics, and automation

---

## 2) Two Core Objects in Pandas

| Object | Meaning | Use Case |
|--------|---------|----------|
| **Series** | One column (1D) | Single metric, time series, column operations |
| **DataFrame** | Many columns together (2D table) | Complete datasets, multi-column analysis |

### Example — Series

```python
import pandas as pd

# Creating a Series
ages = pd.Series([21, 23, 20])
print(ages)

# Output:
# 0    21
# 1    23
# 2    20
# dtype: int64

# Series with custom index
ages = pd.Series([21, 23, 20], index=['Alice', 'Bob', 'Charlie'])
print(ages)

# Output:
# Alice      21
# Bob        23
# Charlie    20
# dtype: int64
```

### Example — DataFrame

```python
# Method 1: From dictionary
data = {
    "name": ["Aditi", "Rahul", "Maya"],
    "age": [21, 23, 20],
    "city": ["Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

# Output:
#     name  age    city
# 0  Aditi   21    Pune
# 1  Rahul   23   Delhi
# 2   Maya   20  Mumbai

# Method 2: From list of lists
data = [
    ["Aditi", 21, "Pune"],
    ["Rahul", 23, "Delhi"],
    ["Maya", 20, "Mumbai"]
]

df = pd.DataFrame(data, columns=["name", "age", "city"])
```

---

## 3) Reading Real Files

### From Excel

```python
# Basic read
df = pd.read_excel("data.xlsx")

# Read specific sheet
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Read with specific columns
df = pd.read_excel("data.xlsx", usecols=["name", "age"])
```

### From CSV

```python
# Basic read
df = pd.read_csv("data.csv")

# Read with custom delimiter
df = pd.read_csv("data.tsv", sep="\t")

# Read with specific encoding
df = pd.read_csv("data.csv", encoding="utf-8")

# Skip rows
df = pd.read_csv("data.csv", skiprows=2)
```

### Essential Inspection Commands

```python
# First 5 rows
df.head()

# Last 5 rows
df.tail()

# First 10 rows
df.head(10)

# Shape (rows, columns)
print(df.shape)  # e.g., (100, 5)

# Column names
print(df.columns)

# Data types
print(df.dtypes)

# Statistical summary
print(df.describe())

# Basic info
print(df.info())

# Check for missing values
print(df.isnull().sum())
```

**Professional Habit:**  
Always inspect your data immediately after loading:
```python
df = pd.read_excel("data.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)
```

---

## 4) Selecting Columns

### Single Column → Series

```python
# Returns Series
ages = df["age"]
print(type(ages))  # <class 'pandas.core.series.Series'>
```

### Multiple Columns → DataFrame

```python
# Returns DataFrame
subset = df[["name", "age"]]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>

# Order matters
subset = df[["age", "name"]]  # Different column order
```

### Important Rules

| Selection | Returns | Use When |
|-----------|---------|----------|
| `df["age"]` | Series | Need single column for calculations |
| `df[["age"]]` | DataFrame | Need to maintain table structure |
| `df[["name", "age"]]` | DataFrame | Need multiple columns |

---

# SESSION 2 — WHAT IS `df` + DATAFRAME ANATOMY

## 1) What is `df`?

**Important Truth:**  
`df` is just a **variable name**, NOT a special keyword.

You could write:
```python
students = pd.DataFrame(...)
table = pd.DataFrame(...)
data = pd.DataFrame(...)
my_data = pd.DataFrame(...)
```

**Convention:**  
`df` stands for "DataFrame" and is widely used in documentation and tutorials, but it's not required.

---

## 2) What is a DataFrame?

A DataFrame has **three main parts:**

| Part | Meaning | Example |
|------|---------|---------|
| **Data** | The actual table values | "Aditi", 21, "Pune" |
| **Columns** | Column names (headers) | "name", "age", "city" |
| **Index** | Row labels | 0, 1, 2, ... |

### Visual Example

```
       name   age    city
    0  Aditi   21    Pune
    1  Rahul   23   Delhi
    2   Maya   20  Mumbai
    
    ↑         ↑      ↑
  Index   Columns  Data
```

### Working with Parts

```python
# Access columns
print(df.columns)
# Index(['name', 'age', 'city'], dtype='object')

# Access index
print(df.index)
# RangeIndex(start=0, stop=3, step=1)

# Access values (as NumPy array)
print(df.values)
# [['Aditi' 21 'Pune']
#  ['Rahul' 23 'Delhi']
#  ['Maya' 20 'Mumbai']]

# Rename columns
df.columns = ["student_name", "years", "location"]

# Set custom index
df.index = ["a", "b", "c"]

# Reset index back to 0,1,2
df = df.reset_index(drop=True)
```

---

## 3) Series vs DataFrame (Crystal Clear Difference)

| Selection | Type Returned | Shape |
|-----------|---------------|-------|
| `df["age"]` | Series | (n,) |
| `df[["age"]]` | DataFrame | (n, 1) |
| `df[["name", "age"]]` | DataFrame | (n, 2) |

### Visual Comparison

```python
# Series (1D)
ages = df["age"]
# 0    21
# 1    23
# 2    20
# Name: age, dtype: int64

# DataFrame (2D)
ages_df = df[["age"]]
#    age
# 0   21
# 1   23
# 2   20
```

**Key Insight:**  
Think of Series as a **single column** and DataFrame as a **table** (even if it's one column).

---

# SESSION 3 — HOW PANDAS STORES DATA

## 1) Pandas is Built on NumPy

**Core Concept:**  
Under the hood, pandas uses fast NumPy arrays for data storage.

**Why This Matters:**
- ✅ pandas is extremely fast (C-optimized)
- ✅ Vectorized operations (no loops needed)
- ⚠️ pandas is strict about data types
- ⚠️ Type mismatches cause errors

```python
# NumPy array underneath
print(df["age"].values)  # array([21, 23, 20])
print(type(df["age"].values))  # <class 'numpy.ndarray'>
```

---

## 2) Data Types Matter

### Check Data Types

```python
# See all column types
print(df.dtypes)

# Output:
# name     object
# age       int64
# city     object
# dtype: object
```

### Common Data Types

| Type | Meaning | Examples |
|------|---------|----------|
| `int64` | Integer numbers | 21, 23, 20 |
| `float64` | Decimal numbers | 21.5, 23.0, 20.7 |
| `object` | Text/strings | "Pune", "Delhi" |
| `bool` | True/False | True, False |
| `datetime64` | Dates/times | 2024-01-15 |

### Type Restrictions

```python
# ❌ This fails (cannot do math on text)
df["name"] + 5  # TypeError

# ✅ This works
df["age"] + 5   # [26, 28, 25]

# ❌ This fails (mixing types)
df["age"] + df["name"]  # TypeError
```

---

## 3) NaN (Missing Values) — Very Important

**Definition:**  
`NaN` = "Not a Number" = pandas' way of representing missing/unknown values.

### Creating Data with NaN

```python
# Using None creates NaN
df = pd.DataFrame({
    "age": [21, None, 20],
    "city": ["Pune", "Delhi", None]
})

print(df)
#     age   city
# 0  21.0   Pune
# 1   NaN  Delhi
# 2  20.0    NaN
```

### Detecting Missing Values

```python
# Check for NaN
print(df.isnull())
#      age   city
# 0  False  False
# 1   True  False
# 2  False   True

# Count missing values per column
print(df.isnull().sum())
# age     1
# city    1

# Check any missing values
print(df.isnull().any())
# age     True
# city    True
```

### Cleaning Missing Values

```python
# Method 1: Remove rows with ANY missing values
df_clean = df.dropna()

# Method 2: Remove rows with missing values in SPECIFIC column
df_clean = df.dropna(subset=["age"])

# Method 3: Fill missing values
df_filled = df.fillna(0)  # Replace NaN with 0
df_filled = df.fillna({"age": 0, "city": "Unknown"})

# Method 4: Forward fill (use previous value)
df_filled = df.fillna(method="ffill")

# Method 5: Backward fill
df_filled = df.fillna(method="bfill")
```

### NaN in Calculations

```python
# NaN spreads through calculations
df["age"] + 5
# 0    26.0
# 1     NaN  ← NaN + 5 = NaN
# 2    25.0

# Mean automatically ignores NaN
print(df["age"].mean())  # 20.5 (only counts 21 and 20)
```

**Important Rule:**  
Always clean your data before analysis!

---

## 4) Converting Types

### Basic Type Conversion

```python
# Convert to string
df["phone"] = df["phone"].astype(str)

# Convert to integer
df["age"] = df["age"].astype(int)

# Convert to float
df["price"] = df["price"].astype(float)

# Convert to datetime
df["date"] = pd.to_datetime(df["date"])
```

### Safe Conversion (Handle Errors)

```python
# This might fail if data has non-numeric values
# df["age"] = df["age"].astype(int)  # ValueError possible

# Safe conversion
df["age"] = pd.to_numeric(df["age"], errors="coerce")
# Converts invalid values to NaN instead of crashing
```

### Common Conversion Patterns

```python
# String to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# String to datetime
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Categorical data (saves memory)
df["category"] = df["category"].astype("category")
```

---

# SESSION 3.5 — iloc (POSITION-BASED INDEXING)

## What is `iloc`?

**Definition:**  
`iloc` = **position-based selection** (uses numbers only, like Python lists)

**Basic Form:**
```python
df.iloc[row_position, column_position]
```

**Mental Model:**  
> iloc = "where things are" (positions), not "what they are" (names)

---

## Examples

### 1) Select Single Row

```python
# First row (position 0)
print(df.iloc[0])

# Output (returns Series):
# name    Aditi
# age        21
# city     Pune
# Name: 0, dtype: object

# Second row
print(df.iloc[1])

# Last row (negative indexing works)
print(df.iloc[-1])
```

### 2) Select Multiple Rows (Slicing)

```python
# First three rows (0, 1, 2)
print(df.iloc[0:3])

# Rows 2 to 4 (positions 2, 3)
print(df.iloc[2:4])

# Every other row
print(df.iloc[::2])

# Reverse order
print(df.iloc[::-1])
```

### 3) Select Single Cell

```python
# Row 0, Column 1
value = df.iloc[0, 1]
print(value)  # 21

# Last row, first column
value = df.iloc[-1, 0]
```

### 4) Select Rows and Columns Together

```python
# First 3 rows, first 2 columns
subset = df.iloc[0:3, 0:2]

# All rows, first 2 columns
subset = df.iloc[:, 0:2]

# First 3 rows, all columns
subset = df.iloc[0:3, :]
```

### 5) Select Specific Rows and Columns (Lists)

```python
# Rows 0 and 2, columns 0 and 2
subset = df.iloc[[0, 2], [0, 2]]

# Non-contiguous selections
subset = df.iloc[[0, 2, 4], [1, 3]]
```

---

## loc vs iloc (Critical Contrast)

| Tool | Thinks In | Example |
|------|-----------|---------|
| `iloc` | Numbers (positions) | `df.iloc[0]` = first row |
| `loc` | Names (labels) | `df.loc[0]` = row labeled 0 |

### Important Difference

```python
# If index is custom:
df.index = ['a', 'b', 'c']

# iloc uses position (always 0,1,2...)
df.iloc[0]  # Gets first row (labeled 'a')

# loc uses label
df.loc['a']  # Gets row labeled 'a'
df.loc[0]    # KeyError! (no row labeled 0)
```

**Remember:**  
> iloc = where things are (position)  
> loc = what they are called (label)

---

# SESSION 4 — BOOLEAN FILTERING

## Core Concept

**Boolean filtering** = asking a True/False question for each row, then keeping only True rows.

**Pattern:**
1. Create a boolean mask (True/False for each row)
2. Apply the mask to filter the DataFrame

---

## 1) Create a Boolean Mask

```python
# Example DataFrame
df = pd.DataFrame({
    "name": ["Aditi", "Rahul", "Maya", "Karan"],
    "age": [21, 23, 20, 23],
    "city": ["Pune", "Delhi", "Mumbai", "Pune"]
})

# Create mask
mask = df["city"] == "Pune"
print(mask)

# Output:
# 0     True
# 1    False
# 2    False
# 3     True
# Name: city, dtype: bool
```

---

## 2) Apply the Mask

```python
# Use mask to filter
pune_df = df[mask]
print(pune_df)

# Output:
#     name  age   city
# 0  Aditi   21   Pune
# 3  Karan   23   Pune
```

---

## 3) One-Line Form (Most Common)

```python
# Combined in one step
pune_df = df[df["city"] == "Pune"]
```

**Read as:**  
"Give me all rows where city equals Pune"

---

## 4) Numeric Filtering

```python
# People older than 21
older = df[df["age"] > 21]

# People exactly 23 years old
age_23 = df[df["age"] == 23]

# People 21 or younger
young = df[df["age"] <= 21]
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

---

## 5) Multiple Conditions

### AND Logic (both conditions must be True)

```python
# Pune AND age >= 23
filtered = df[
    (df["city"] == "Pune") &
    (df["age"] >= 23)
]

# Multiple AND conditions
filtered = df[
    (df["city"] == "Pune") &
    (df["age"] >= 20) &
    (df["age"] <= 25)
]
```

### OR Logic (at least one condition must be True)

```python
# Pune OR Mumbai
filtered = df[
    (df["city"] == "Pune") |
    (df["city"] == "Mumbai")
]

# Age < 21 OR age > 22
filtered = df[
    (df["age"] < 21) |
    (df["age"] > 22)
]
```

### Combining AND & OR

```python
# (Pune OR Mumbai) AND age >= 21
filtered = df[
    ((df["city"] == "Pune") | (df["city"] == "Mumbai")) &
    (df["age"] >= 21)
]
```

---

## 6) String Filtering

```python
# Contains substring (case-sensitive)
filtered = df[df["name"].str.contains("a")]

# Case-insensitive
filtered = df[df["name"].str.contains("a", case=False)]

# Starts with
filtered = df[df["name"].str.startswith("A")]

# Ends with
filtered = df[df["name"].str.endswith("i")]

# Exact match (case-insensitive)
filtered = df[df["name"].str.lower() == "aditi"]
```

---

## 7) NOT Logic (Negation)

```python
# NOT Pune (all cities except Pune)
not_pune = df[~(df["city"] == "Pune")]

# Alternative
not_pune = df[df["city"] != "Pune"]

# NOT (age > 21)
not_old = df[~(df["age"] > 21)]
```

---

## 8) isin() Method (Multiple Values)

```python
# City is either Pune or Mumbai
cities = ["Pune", "Mumbai"]
filtered = df[df["city"].isin(cities)]

# Age is 20, 21, or 23
ages = [20, 21, 23]
filtered = df[df["age"].isin(ages)]

# NOT in list
not_in_cities = df[~df["city"].isin(["Delhi", "Mumbai"])]
```

---

## Critical Rules for Multiple Conditions

1. **Use `&` for AND** (not `and`)
2. **Use `|` for OR** (not `or`)
3. **Use `~` for NOT** (not `not`)
4. **Each condition MUST be in parentheses `()`**

**Why parentheses matter:**
```python
# ❌ WRONG (will error)
df[df["city"] == "Pune" & df["age"] > 21]

# ✅ CORRECT
df[(df["city"] == "Pune") & (df["age"] > 21)]
```

---

# SESSION 5 — loc + BOOLEAN FILTERING

## Basic Structure

```python
df.loc[ROW_CONDITION, COLUMN_SELECTION]
```

**Read as:**  
"From df, give me these rows AND these columns"

---

## 1) Filter Rows Only

```python
# All Pune rows (all columns)
pune_df = df.loc[df["city"] == "Pune"]

# Same as:
pune_df = df[df["city"] == "Pune"]
```

**When to use:**  
When you want all columns but filtered rows.

---

## 2) Filter Rows + Select Columns

```python
# Pune people, show only name and age
result = df.loc[
    df["city"] == "Pune",
    ["name", "age"]
]

# Output:
#     name  age
# 0  Aditi   21
# 3  Karan   23
```

**Read as:**  
"Give me Pune rows, but only show name and age columns"

---

## 3) Multiple Conditions with loc

```python
# Pune AND age >= 23, show only names
result = df.loc[
    (df["city"] == "Pune") &
    (df["age"] >= 23),
    ["name"]
]

# Complex filtering
result = df.loc[
    (df["city"].isin(["Pune", "Mumbai"])) &
    (df["age"] > 20),
    ["name", "age", "city"]
]
```

---

## 4) All Rows, Specific Columns

```python
# All rows, but only name and city
result = df.loc[:, ["name", "city"]]

# Using colon (:) means "all rows"
```

---

## 5) Series vs DataFrame in loc

### Returns Series (single column)

```python
# Returns Series
ages = df.loc[df["city"] == "Pune", "age"]

# Output:
# 0    21
# 3    23
# Name: age, dtype: int64
```

### Returns DataFrame (list of columns)

```python
# Returns DataFrame
ages_df = df.loc[df["city"] == "Pune", ["age"]]

# Output:
#    age
# 0   21
# 3   23
```

**Remember:**
- String → Series
- List → DataFrame

---

## 6) loc with Index Labels

```python
# If you have custom index
df.index = ['a', 'b', 'c', 'd']

# Select by index label
row = df.loc['a']

# Multiple index labels
rows = df.loc[['a', 'c']]

# Slice by labels (INCLUSIVE!)
rows = df.loc['a':'c']  # Includes 'c' (unlike iloc)
```

---

## 7) Setting Values with loc

```python
# Change single value
df.loc[0, "age"] = 22

# Change multiple values in a column
df.loc[df["city"] == "Pune", "age"] = 25

# Change multiple columns
df.loc[0, ["age", "city"]] = [22, "Delhi"]

# Create new column with condition
df.loc[df["age"] > 21, "status"] = "Adult"
```

---

## Professional Pattern

```python
# Clean, readable multi-condition filtering
result = df.loc[
    (df["city"] == "Pune") &
    (df["age"] >= 20) &
    (df["age"] <= 25),
    ["name", "age"]
]
```

**Why this is better:**
- Easy to read
- Easy to debug
- Easy to modify
- Follows PEP 8 style guide

---

# SESSION 6 — CREATING & TRANSFORMING COLUMNS

## Core Concept

**Creating a column** = adding a new Series to your DataFrame

**Pattern:**
```python
df["new_column"] = computation
```

---

## 1) Columns from Math Operations

### Simple Arithmetic

```python
# Add 10% tax
df["price_after_tax"] = df["price"] * 1.10

# Flat discount
df["discounted_price"] = df["price"] - 5000

# Percentage calculation
df["discount_percent"] = (df["original_price"] - df["sale_price"]) / df["original_price"] * 100

# Combine multiple columns
df["total"] = df["quantity"] * df["unit_price"]
```

### Key Insight

Pandas applies operations **row-by-row automatically** — no loops needed!

```python
# This happens automatically for all rows:
price	price_after_tax
80000	88000
30000	33000
25000	27500
```

---

## 2) Columns from Text Operations

**Critical Rule:**  
Text columns require `.str` before string methods

### Common String Operations

```python
# Lowercase
df["product_lower"] = df["product"].str.lower()

# Uppercase
df["product_upper"] = df["product"].str.upper()

# Title case
df["name_title"] = df["name"].str.title()

# Check if contains substring
df["has_phone"] = df["product"].str.contains("phone", case=False)

# Starts with
df["starts_with_L"] = df["product"].str.startswith("L")

# Ends with
df["ends_with_top"] = df["product"].str.endswith("top")

# Length of string
df["name_length"] = df["name"].str.len()

# Extract substring
df["first_3_chars"] = df["name"].str[:3]

# Replace text
df["product_clean"] = df["product"].str.replace("phone", "mobile")

# Split string
df["first_name"] = df["full_name"].str.split(" ").str[0]

# Strip whitespace
df["name_clean"] = df["name"].str.strip()
```

### String Concatenation

```python
# Combine columns
df["full_address"] = df["street"] + ", " + df["city"]

# With formatting
df["display_name"] = df["first_name"] + " " + df["last_name"]

# Add prefix
df["whatsapp"] = "+91" + df["phone"].astype(str)
```

---

## 3) Boolean (True/False) Columns

### Simple Conditions

```python
# Price-based classification
df["is_expensive"] = df["price"] >= 50000

# Result:
# price    is_expensive
# 80000    True
# 30000    False
```

### Multiple Conditions

```python
# Combined conditions
df["is_premium"] = (
    (df["price"] >= 50000) &
    (df["rating"] >= 4.5)
)

# Complex logic
df["needs_review"] = (
    (df["age"] > 5) |
    (df["condition"] == "Used") |
    (df["price"] < 10000)
)
```

### Why This Is Powerful

```python
# Use later for filtering
premium_items = df[df["is_premium"]]

# Count how many
print(df["is_expensive"].sum())  # True = 1, False = 0

# Percentage
pct = df["is_expensive"].mean() * 100
print(f"{pct:.1f}% are expensive")
```

---

## 4) Conditional Values (np.where & map)

### Using np.where (if-else logic)

```python
import numpy as np

# Simple if-else
df["status"] = np.where(
    df["age"] >= 18,
    "Adult",
    "Minor"
)

# Nested conditions
df["category"] = np.where(
    df["price"] >= 60000,
    "Premium",
    np.where(
        df["price"] >= 30000,
        "Mid",
        "Budget"
    )
)
```

### Using map (dictionary mapping)

```python
# Map values
city_map = {
    "Pune": "Western",
    "Mumbai": "Western",
    "Delhi": "Northern",
    "Kolkata": "Eastern"
}

df["region"] = df["city"].map(city_map)

# Map with default
df["region"] = df["city"].map(city_map).fillna("Unknown")
```

---

## 5) Modifying Existing Columns

### Overwrite Column

```python
# Increase all prices by 10%
df["price"] = df["price"] * 1.10

# Convert to uppercase
df["city"] = df["city"].str.upper()

# Round values
df["price"] = df["price"].round(2)
```

**⚠️ Warning:**  
This permanently changes your data! Make a copy first if needed:

```python
df_modified = df.copy()
df_modified["price"] = df_modified["price"] * 1.10
```

---

## 6) Combining Operations

```python
# Create multiple columns at once
df["price_after_tax"] = df["price"] * 1.18
df["discounted_price"] = df["price"] * 0.80
df["final_price"] = df["price_after_tax"] - df["discount_amount"]

# Chain operations
df["category"] = (
    df["price"]
    .apply(lambda x: "Premium" if x >= 60000 else "Budget")
)
```

---

## 7) Combining with loc

### Filter + Select + Create

```python
# Update only Pune products
df.loc[df["city"] == "Pune", "shipping"] = "Free"

# Create column for specific rows
df.loc[df["price"] > 50000, "vip"] = True
df["vip"] = df["vip"].fillna(False)  # Fill rest with False
```

### Professional Example

```python
# Complex transformation
result = df.loc[
    (df["city"] == "Pune") &
    (df["price"] >= 30000),
    ["product", "price", "price_after_tax"]
]
```

---

## Mental Model

> "New columns = transformations of old columns, applied row-wise automatically."

---

# SESSION 7 — apply(), lambda, and groupby

## Why This Session Matters

**Previously you could:**
- Add columns with simple math
- Filter rows
- Select columns

**Now you'll learn:**
- Custom row-wise logic
- Intelligent data classification
- Automatic data summarization

**This is what real analysts actually use daily.**

---

## 1) apply() — Custom Logic

### Basic Pattern

```python
df["new_column"] = df["old_column"].apply(function)
```

### Example with Function

```python
# Define function
def classify_price(price):
    if price >= 60000:
        return "Premium"
    elif price >= 30000:
        return "Mid"
    else:
        return "Budget"

# Apply to column
df["category"] = df["price"].apply(classify_price)

# Result:
# price    category
# 80000    Premium
# 30000    Mid
# 25000    Budget
```

### Apply with Multiple Columns

```python
# Use axis=1 for row-wise operations
def calculate_total(row):
    return row["quantity"] * row["unit_price"] * (1 - row["discount"])

df["total"] = df.apply(calculate_total, axis=1)

# Access multiple columns
def full_address(row):
    return f"{row['street']}, {row['city']}, {row['zipcode']}"

df["address"] = df.apply(full_address, axis=1)
```

---

## 2) lambda — Short Anonymous Functions

### Basic Syntax

```python
lambda arguments: expression
```

### Common Use Cases

```python
# Single condition
df["category"] = df["price"].apply(
    lambda x: "Premium" if x >= 50000 else "Budget"
)

# Complex ternary
df["status"] = df["age"].apply(
    lambda x: "Senior" if x >= 60 else ("Adult" if x >= 18 else "Minor")
)

# Mathematical operations
df["price_k"] = df["price"].apply(lambda x: x / 1000)

# String operations
df["initials"] = df["name"].apply(lambda x: x[0].upper())
```

### With Multiple Columns

```python
# Row-wise lambda
df["discount_amount"] = df.apply(
    lambda row: row["price"] * row["discount_rate"],
    axis=1
)
```

### When to Use Lambda vs Function

| Use Lambda | Use Function |
|------------|--------------|
| Simple one-liners | Complex logic |
| Single transformation | Multiple steps |
| Quick operations | Reusable code |

---

## 3) groupby — Data Summarization

### Basic Concept

**groupby** = "Split data into groups, then summarize each group"

### Single Aggregation

```python
# Average price per city
avg_price = df.groupby("city")["price"].mean()

# Output:
# city
# Delhi     52500.0
# Mumbai    90000.0
# Pune      31000.0
# Name: price, dtype: float64
```

### Common Aggregations

```python
# Count
df.groupby("city")["product"].count()

# Sum
df.groupby("city")["price"].sum()

# Maximum
df.groupby("city")["price"].max()

# Minimum
df.groupby("city")["price"].min()

# Standard deviation
df.groupby("city")["price"].std()

# Multiple stats
df.groupby("city")["price"].describe()
```

---

## 4) Multiple Aggregations

### Using agg()

```python
# Multiple metrics on same column
summary = df.groupby("city")["price"].agg(["mean", "max", "min", "count"])

# Output:
#          mean    max    min  count
# city                              
# Delhi   52500  80000  25000      2
# Mumbai  90000  90000  90000      1
# Pune    31000  32000  30000      2
```

### Different Aggregations per Column

```python
summary = df.groupby("city").agg({
    "price": ["mean", "max"],
    "quantity": "sum",
    "rating": ["mean", "count"]
})
```

### Custom Aggregation Functions

```python
# Custom function
def price_range(prices):
    return prices.max() - prices.min()

summary = df.groupby("city")["price"].agg([
    "mean",
    ("range", price_range)
])
```

---

## 5) Group by Multiple Columns

```python
# Group by city AND category
summary = df.groupby(["city", "category"])["price"].mean()

# Output (MultiIndex):
# city    category
# Delhi   Budget      25000
#         Premium     80000
# Mumbai  Premium     90000
# Pune    Mid         31000
# Name: price, dtype: float64

# Reset index to normal DataFrame
summary = summary.reset_index()
```

---

## 6) Filter → groupby Pattern (VERY IMPORTANT)

**Common Real-World Pattern:**
1. Filter the data you care about
2. Summarize with groupby

### Example — Premium Products Only

```python
# Step 1: Filter
premium_df = df[df["category"] == "premium"]

# Step 2: Summarize
premium_summary = premium_df.groupby("city")["price"].mean()

# Combined (professional style)
premium_summary = (
    df[df["category"] == "premium"]
      .groupby("city")
      .agg({
          "price": "mean",
          "price_after_tax": "mean",
          "discount_amount": "sum"
      })
)
```

### More Examples

```python
# High-value customers only
high_value = (
    df[df["total_spent"] > 100000]
      .groupby("region")["revenue"]
      .sum()
)

# Recent orders
recent_summary = (
    df[df["date"] >= "2024-01-01"]
      .groupby("product_category")["sales"]
      .agg(["sum", "mean", "count"])
)
```

---

## 7) Sorting Grouped Results

```python
# Sort by values
summary = df.groupby("city")["price"].mean().sort_values(ascending=False)

# Sort by index
summary = df.groupby("city")["price"].mean().sort_index()

# Top N groups
top_cities = df.groupby("city")["revenue"].sum().nlargest(5)
```

---

## Mental Model

> **apply** = custom row logic  
> **lambda** = short logic  
> **groupby** = summarize by category

**Pattern:**
```
subset → summarize
```

---

# QUICK REFERENCE GUIDE

## Essential Commands Cheat Sheet

### Loading Data

```python
# CSV
df = pd.read_csv("file.csv")

# Excel
df = pd.read_excel("file.xlsx", sheet_name="Sheet1")

# With specific columns
df = pd.read_csv("file.csv", usecols=["col1", "col2"])
```

### Inspecting Data

```python
df.head(n)           # First n rows (default 5)
df.tail(n)           # Last n rows
df.shape             # (rows, columns)
df.columns           # Column names
df.dtypes            # Data types
df.info()            # Overview
df.describe()        # Statistics
df.isnull().sum()    # Count missing values
```

### Selecting Data

```python
df["col"]            # Single column (Series)
df[["col"]]          # Single column (DataFrame)
df[["col1", "col2"]] # Multiple columns
df.iloc[0]           # First row by position
df.iloc[0:3]         # Rows 0-2
df.iloc[0, 1]        # Cell at row 0, col 1
df.loc[condition]    # Rows matching condition
df.loc[cond, cols]   # Filtered rows, specific columns
```

### Filtering

```python
df[df["col"] > 5]                    # Simple filter
df[df["col"] == "value"]             # Exact match
df[(df["a"] > 5) & (df["b"] < 10)]   # AND
df[(df["a"] > 5) | (df["b"] < 10)]   # OR
df[~(df["col"] == "value")]          # NOT
df[df["col"].isin(list)]             # Multiple values
```

### Creating Columns

```python
df["new"] = df["old"] * 2            # Math
df["new"] = df["col"].str.lower()    # String
df["new"] = df["col"] >= 50          # Boolean
df["new"] = df["col"].apply(func)    # Custom function
```

### Cleaning Data

```python
df.dropna()                  # Remove missing
df.fillna(value)            # Fill missing
df.drop_duplicates()        # Remove duplicates
df["col"].astype(type)      # Convert type
```

### Grouping & Aggregation

```python
df.groupby("col")["val"].mean()      # Average by group
df.groupby("col").agg({"val": "sum"}) # Custom aggregation
df.groupby(["a", "b"])["c"].count()   # Multiple groups
```

### Saving Data

```python
df.to_csv("file.csv", index=False)
df.to_excel("file.xlsx", index=False)
```

---

## The 5 Golden Rules

1. **One column** → Series
2. **List of columns** → DataFrame
3. **Always quote column names:** `df["age"]`
4. **Use parentheses in multiple conditions:** `(df["a"] > 5) & (df["b"] < 10)`
5. **loc pattern:** rows first, columns second

---

# COMMON PATTERNS & BEST PRACTICES

## 1) Loading and Inspecting

```python
# Always follow this pattern
df = pd.read_excel("data.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
```

## 2) Cleaning Pipeline

```python
# Standard cleaning workflow
df = df.dropna(subset=["critical_column"])
df = df.drop_duplicates()
df["phone"] = df["phone"].astype(str)
df["date"] = pd.to_datetime(df["date"])
```

## 3) Filter → Transform → Save

```python
# Professional workflow
filtered = df[
    (df["date"] >= "2024-01-01") &
    (df["status"] == "Active")
]

filtered["revenue_k"] = filtered["revenue"] / 1000

filtered.to_excel("output.xlsx", index=False)
```

## 4) Analysis Pattern

```python
# Standard analysis
summary = (
    df[df["category"] == "Premium"]
      .groupby("region")
      .agg({
          "revenue": ["sum", "mean"],
          "customers": "count"
      })
      .round(2)
)

print(summary)
summary.to_excel("analysis.xlsx")
```

## 5) Error Prevention

```python
# Make copies before modifying
df_clean = df.copy()
df_clean["price"] = df_clean["price"] * 1.10

# Check results before saving
print(df_clean.head())
print(df_clean.shape)

# Use try-except for type conversion
try:
    df["age"] = df["age"].astype(int)
except ValueError:
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
```

## 6) Performance Tips

```python
# Use category for repeated strings (saves memory)
df["category"] = df["category"].astype("category")

# Read only needed columns
df = pd.read_csv("large.csv", usecols=["col1", "col2"])

# Use chunksize for very large files
for chunk in pd.read_csv("huge.csv", chunksize=10000):
    process(chunk)
```

---

# ADDITIONAL ADVANCED TOPICS

## Date/Time Operations

```python
# Convert to datetime
df["date"] = pd.to_datetime(df["date"])

# Extract components
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()

# Date arithmetic
df["days_since"] = (pd.Timestamp.now() - df["date"]).dt.days

# Filter by date
df[df["date"] >= "2024-01-01"]
df[df["date"].dt.year == 2024]
```

## Merge and Join

```python
# Merge two DataFrames
merged = pd.merge(df1, df2, on="key_column")

# Different join types
merged = pd.merge(df1, df2, on="key", how="left")   # Left join
merged = pd.merge(df1, df2, on="key", how="right")  # Right join
merged = pd.merge(df1, df2, on="key", how="outer")  # Outer join
merged = pd.merge(df1, df2, on="key", how="inner")  # Inner join (default)

# Merge on multiple columns
merged = pd.merge(df1, df2, on=["col1", "col2"])
```

## Pivot Tables

```python
# Create pivot table
pivot = df.pivot_table(
    values="price",
    index="city",
    columns="category",
    aggfunc="mean"
)

# Multiple aggregations
pivot = df.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc=["sum", "mean", "count"]
)
```

## Sorting

```python
# Sort by single column
df.sort_values("price")

# Sort descending
df.sort_values("price", ascending=False)

# Sort by multiple columns
df.sort_values(["city", "price"])

# Sort index
df.sort_index()
```

## Renaming

```python
# Rename columns
df.rename(columns={"old_name": "new_name"}, inplace=True)

# Rename multiple
df.rename(columns={
    "old1": "new1",
    "old2": "new2"
}, inplace=True)

# Set column names directly
df.columns = ["col1", "col2", "col3"]
```

---

# WHAT YOU'VE MASTERED

After completing these sessions, you can:

✅ Load data from Excel/CSV files  
✅ Inspect and understand DataFrame structure  
✅ Select rows and columns precisely  
✅ Filter data with complex conditions  
✅ Handle missing values (NaN)  
✅ Create and transform columns  
✅ Apply custom logic with functions  
✅ Summarize data with groupby  
✅ Combine multiple operations efficiently  

**This is professional-level pandas competency.**

---

# NEXT STEPS

## Continue Learning

1. **Merge/Join operations** — Combining multiple DataFrames
2. **Pivot tables** — Reshaping data for analysis
3. **Time series** — Working with dates and times
4. **Visualization** — Creating charts with pandas + matplotlib
5. **Real projects** — Apply to actual datasets

## Practice Projects

1. **Sales Analysis** — Analyze monthly sales data
2. **Customer Segmentation** — Group customers by behavior
3. **Expense Tracker** — Personal finance analysis
4. **Web Scraping + Pandas** — Collect and analyze web data
5. **WhatsApp Automation** — Clean contacts for messaging

---

# END OF PANDAS MASTER NOTES

**Remember:** The best way to learn pandas is by doing.  
Take any dataset and start exploring!

---

**Version:** Complete Edition (Sessions 1-7)  
**Last Updated:** 2024  
**Author:** Prerak (Apex Tutor Method)