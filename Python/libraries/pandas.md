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

# SESSION 8 — MERGE, JOIN & CONCAT (COMBINING TABLES)

## Why This Matters

In real life, you rarely work with one dataset. You usually have:
- One file with customers
- Another file with orders
- Another file with payments

**Your job is to combine them correctly.**

Pandas gives you three main tools:
- **concat** → stack tables
- **merge** → join tables like SQL
- **join** → table joining by index

---

## 1) concat — Stacking Tables (Top to Bottom)

### When to Use
Use this when tables have **the same columns** but different rows.

### Basic Pattern

```python
df_all = pd.concat([df1, df2], ignore_index=True)
```

**Mental Model:**  
> "Glue tables vertically."

### Example

**Table 1 (df1):**
```
   name    city
0  Aditi   Pune
1  Rahul   Delhi
```

**Table 2 (df2):**
```
   name    city
0  Maya    Mumbai
1  Karan   Pune
```

**After concat:**
```python
df_all = pd.concat([df1, df2], ignore_index=True)

# Result:
#    name    city
# 0  Aditi   Pune
# 1  Rahul   Delhi
# 2  Maya    Mumbai
# 3  Karan   Pune
```

### Advanced concat Options

```python
# Keep original indices
df_all = pd.concat([df1, df2])  # Indices: 0,1,0,1

# Concatenate horizontally (side by side)
df_wide = pd.concat([df1, df2], axis=1)

# Concatenate multiple DataFrames
df_all = pd.concat([df1, df2, df3], ignore_index=True)

# Add keys to identify source
df_all = pd.concat([df1, df2], keys=['Table1', 'Table2'])
```

---

## 2) merge — SQL-Style Join (MOST IMPORTANT)

### When to Use
Use this when tables share a **common key column**.

### Basic Pattern

```python
merged = pd.merge(df1, df2, on="id", how="inner")
```

**Mental Model:**  
> "Match rows based on a key column."

---

## Types of Joins

| Join Type | Meaning | Use When |
|-----------|---------|----------|
| **inner** | Keep only matching rows in both tables | Want only complete matches |
| **left** | Keep all from df1, match where possible | Need all left table data |
| **right** | Keep all from df2, match where possible | Need all right table data |
| **outer** | Keep everything from both tables | Need all data from both |

---

## Inner Join Example

```python
# Customers table
customers = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Aditi", "Rahul", "Maya"]
})

# Orders table
orders = pd.DataFrame({
    "id": [2, 3, 4],
    "order": ["Phone", "Laptop", "Tablet"]
})

# Inner join (only matching IDs: 2, 3)
merged = pd.merge(customers, orders, on="id", how="inner")

# Result:
#    id   name   order
# 0   2  Rahul   Phone
# 1   3   Maya  Laptop
```

---

## Left Join Example

```python
# Keep all customers, add order info where available
merged = pd.merge(customers, orders, on="id", how="left")

# Result:
#    id   name    order
# 0   1  Aditi      NaN  ← No order for ID 1
# 1   2  Rahul    Phone
# 2   3   Maya   Laptop
```

---

## Right Join Example

```python
# Keep all orders, add customer info where available
merged = pd.merge(customers, orders, on="id", how="right")

# Result:
#    id    name    order
# 0   2   Rahul    Phone
# 1   3    Maya   Laptop
# 2   4     NaN   Tablet  ← No customer for ID 4
```

---

## Outer Join Example

```python
# Keep everything from both tables
merged = pd.merge(customers, orders, on="id", how="outer")

# Result:
#    id   name    order
# 0   1  Aditi      NaN
# 1   2  Rahul    Phone
# 2   3   Maya   Laptop
# 3   4    NaN   Tablet
```

---

## Advanced Merge Options

### Merge on Multiple Columns

```python
# Match on both product AND city
merged = pd.merge(df1, df2, on=["product", "city"], how="inner")
```

### Merge with Different Column Names

```python
# df1 has "customer_id", df2 has "id"
merged = pd.merge(
    df1, 
    df2, 
    left_on="customer_id", 
    right_on="id", 
    how="left"
)
```

### Specify Suffixes for Overlapping Columns

```python
# Both tables have a "price" column
merged = pd.merge(
    df1, 
    df2, 
    on="product", 
    how="inner",
    suffixes=("_old", "_new")
)
# Results in: price_old, price_new
```

### Validate Merge

```python
# Ensure one-to-one relationship
merged = pd.merge(df1, df2, on="id", validate="one_to_one")

# Ensure one-to-many
merged = pd.merge(df1, df2, on="id", validate="one_to_many")
```

---

## 3) join — Index-Based Join

### When to Use
If both tables share the **same index**, you can use join.

### Basic Pattern

```python
combined = df1.join(df2)
```

### Example

```python
# Both have same index
df1 = pd.DataFrame(
    {"price": [80000, 30000]},
    index=["Laptop", "Phone"]
)

df2 = pd.DataFrame(
    {"stock": [10, 25]},
    index=["Laptop", "Phone"]
)

# Join by index
combined = df1.join(df2)

# Result:
#         price  stock
# Laptop  80000     10
# Phone   30000     25
```

### Join with How Parameter

```python
# Left join
combined = df1.join(df2, how="left")

# Outer join
combined = df1.join(df2, how="outer")
```

---

## 4) Real-World Example

### Sales + Inventory Analysis

```python
# Sales data (facts table)
sales = pd.DataFrame({
    "product": ["Laptop", "Phone", "Laptop", "Tablet"],
    "city": ["Delhi", "Pune", "Mumbai", "Delhi"],
    "revenue": [80000, 30000, 90000, 25000]
})

# Inventory data (lookup table)
inventory = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet"],
    "stock": [10, 25, 15]
})

# Left join: Keep all sales, add stock info
result = pd.merge(sales, inventory, on="product", how="left")

# Result:
#   product    city  revenue  stock
# 0  Laptop   Delhi    80000     10
# 1   Phone    Pune    30000     25
# 2  Laptop  Mumbai    90000     10
# 3  Tablet   Delhi    25000     15
```

---

## When to Use What (Golden Rules)

| Situation | Use |
|-----------|-----|
| Same columns, different rows | `concat` |
| Different tables, common key column | `merge` |
| Same index | `join` |
| Stacking data vertically | `concat` with `axis=0` |
| Combining data horizontally | `concat` with `axis=1` or `merge` |

---

## Common Patterns

### Pattern 1: Combining Monthly Files

```python
# Load multiple months
jan = pd.read_csv("jan_sales.csv")
feb = pd.read_csv("feb_sales.csv")
mar = pd.read_csv("mar_sales.csv")

# Stack them
all_sales = pd.concat([jan, feb, mar], ignore_index=True)
```

### Pattern 2: Enriching Transaction Data

```python
# Transactions
transactions = pd.read_csv("transactions.csv")

# Customer details
customers = pd.read_csv("customers.csv")

# Add customer info to transactions
enriched = pd.merge(
    transactions,
    customers,
    on="customer_id",
    how="left"
)
```

### Pattern 3: Multiple Table Join

```python
# Join three tables
result = (
    pd.merge(sales, customers, on="customer_id", how="left")
      .merge(products, on="product_id", how="left")
)
```

---

## Mental Model

> **concat** = stack tables  
> **merge** = match tables by key  
> **join** = align by index

---

# SESSION 9 — PIVOTING & RESHAPING DATA

## Why Reshaping Matters

Real datasets are often **NOT in the shape you want**.

You frequently need to:
- Turn long tables into summary tables
- Compare cities, months, products in a grid
- Prepare data for charts or dashboards
- Switch between wide and long formats

Pandas gives you three main tools:
- **pivot_table** — summarize into grid
- **pivot** — reshape without aggregation
- **melt** — unpivot (wide → long)

---

## 1) pivot_table — The Workhorse (MOST IMPORTANT)

### Core Concept

**Basic Idea:**  
> "Summarize data into a grid/cross-tab."

### Basic Pattern

```python
df.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum"
)
```

**Read as:**
- Rows = cities
- Columns = products
- Cells = total revenue

---

## Common Aggregations

| Function | Purpose |
|----------|---------|
| `"sum"` | Total |
| `"mean"` | Average |
| `"count"` | Count of records |
| `"max"` | Maximum value |
| `"min"` | Minimum value |
| `"std"` | Standard deviation |

---

## Example — Sales Pivot Table

```python
# Sample data
sales = pd.DataFrame({
    "product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet"],
    "city": ["Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "revenue": [80000, 30000, 90000, 25000, 32000, 27000]
})

# Create pivot table
pivot = sales.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum"
)

# Result:
# product   Laptop  Phone  Tablet
# city                           
# Delhi      80000    NaN   25000
# Mumbai     90000    NaN   27000
# Pune         NaN  62000     NaN
```

---

## Multiple Aggregations

```python
# Multiple statistics
pivot = sales.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc=["sum", "mean", "count"]
)

# Custom aggregations
pivot = sales.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc={"revenue": ["sum", "mean"]}
)
```

---

## Fill Missing Values

```python
# Fill NaN with 0
pivot = sales.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum",
    fill_value=0
)

# Result:
# product   Laptop  Phone  Tablet
# city                           
# Delhi      80000      0   25000
# Mumbai     90000      0   27000
# Pune           0  62000       0
```

---

## Multiple Index/Columns

```python
# Multiple row indices
pivot = sales.pivot_table(
    values="revenue",
    index=["city", "quarter"],
    columns="product",
    aggfunc="sum"
)

# Multiple column levels
pivot = sales.pivot_table(
    values=["revenue", "quantity"],
    index="city",
    columns="product",
    aggfunc="sum"
)
```

---

## Add Margins (Totals)

```python
# Add row and column totals
pivot = sales.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)

# Result includes Total row and column
```

---

## 2) pivot — Simple Reshaping (No Aggregation)

### When to Use
Use `pivot` when each (index, column) combination appears **only once**.

### Basic Pattern

```python
df.pivot(
    index="city",
    columns="product",
    values="revenue"
)
```

### Example

```python
# Data with unique combinations
sales_unique = pd.DataFrame({
    "city": ["Delhi", "Mumbai", "Pune"],
    "product": ["Laptop", "Laptop", "Laptop"],
    "revenue": [80000, 90000, 85000]
})

# Simple pivot (no aggregation needed)
pivoted = sales_unique.pivot(
    index="city",
    columns="product",
    values="revenue"
)
```

### Important Note

**If duplicates exist, use `pivot_table` instead:**

```python
# This will ERROR if duplicates exist
# df.pivot(index="city", columns="product", values="revenue")

# Use this instead
df.pivot_table(
    index="city",
    columns="product",
    values="revenue",
    aggfunc="sum"  # or mean, max, etc.
)
```

---

## 3) melt — Unpivoting (Wide → Long)

### Core Concept

**Melt** converts a wide table into a long (tidy) format.

**Use when:** You need to convert column headers into row values.

---

## Basic melt Example

### Before (Wide):

```python
wide = pd.DataFrame({
    "city": ["Delhi", "Mumbai"],
    "Laptop": [80000, 90000],
    "Phone": [30000, 35000]
})

#      city  Laptop  Phone
# 0   Delhi   80000  30000
# 1  Mumbai   90000  35000
```

### After (Long):

```python
long = wide.melt(
    id_vars=["city"],
    value_vars=["Laptop", "Phone"],
    var_name="product",
    value_name="revenue"
)

#      city product  revenue
# 0   Delhi  Laptop    80000
# 1  Mumbai  Laptop    90000
# 2   Delhi   Phone    30000
# 3  Mumbai   Phone    35000
```

---

## melt Parameters

```python
df.melt(
    id_vars=["cols_to_keep"],      # Identifier columns
    value_vars=["cols_to_unpivot"], # Columns to melt
    var_name="new_column_name",     # Name for variable column
    value_name="new_value_name"     # Name for value column
)
```

---

## melt All Columns Except ID

```python
# Melt all columns except 'city'
long = wide.melt(
    id_vars=["city"],
    var_name="product",
    value_name="revenue"
)
# value_vars automatically includes all other columns
```

---

## Real-World melt Example

### Monthly Sales (Wide Format)

```python
monthly = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet"],
    "Jan": [80000, 30000, 25000],
    "Feb": [85000, 32000, 27000],
    "Mar": [90000, 35000, 30000]
})

#   product    Jan    Feb    Mar
# 0  Laptop  80000  85000  90000
# 1   Phone  30000  32000  35000
# 2  Tablet  25000  27000  30000
```

### Convert to Long Format

```python
long = monthly.melt(
    id_vars=["product"],
    value_vars=["Jan", "Feb", "Mar"],
    var_name="month",
    value_name="revenue"
)

#   product month  revenue
# 0  Laptop   Jan    80000
# 1   Phone   Jan    30000
# 2  Tablet   Jan    25000
# 3  Laptop   Feb    85000
# 4   Phone   Feb    32000
# ... (continues)
```

---

## 4) stack and unstack (Index Manipulation)

### stack — Pivot columns to rows

```python
# Convert column level to row index
stacked = df.stack()
```

### unstack — Pivot rows to columns

```python
# Convert row index to column level
unstacked = df.unstack()
```

### Example

```python
# Create MultiIndex DataFrame
df = pd.DataFrame({
    "product": ["Laptop", "Laptop", "Phone", "Phone"],
    "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "revenue": [80000, 90000, 30000, 35000]
})

pivot = df.pivot(index="product", columns="city", values="revenue")

# Stack: columns → rows
stacked = pivot.stack()

# Unstack: rows → columns
unstacked = stacked.unstack()
```

---

## 5) Practical Reshaping Patterns

### Pattern 1: Create Dashboard Summary

```python
# Sales data
sales = pd.read_csv("sales.csv")

# Pivot for dashboard
dashboard = sales.pivot_table(
    values="revenue",
    index="month",
    columns="product_category",
    aggfunc="sum",
    fill_value=0,
    margins=True
)
```

### Pattern 2: Time Series Analysis

```python
# Wide format with dates as columns
# Convert to long format for analysis
time_series = wide_df.melt(
    id_vars=["product"],
    var_name="date",
    value_name="sales"
)

# Convert date column
time_series["date"] = pd.to_datetime(time_series["date"])
```

### Pattern 3: Comparison Table

```python
# Compare this year vs last year
comparison = sales.pivot_table(
    values="revenue",
    index="product",
    columns="year",
    aggfunc="sum"
)

# Add growth column
comparison["growth"] = (
    (comparison[2024] - comparison[2023]) / comparison[2023] * 100
)
```

---

## When to Use What

| Need | Use |
|------|-----|
| Summarize data into grid | `pivot_table` |
| Reshape unique data | `pivot` |
| Wide → Long format | `melt` |
| Column → Row index | `stack` |
| Row index → Column | `unstack` |

---

## Mental Model

> **pivot_table** = summarize into grid  
> **pivot** = reshape without aggregation  
> **melt** = flatten wide table to long format  
> **stack/unstack** = move data between index levels

---

# SESSION 10 — DATA CLEANING (NaN, DUPLICATES, TEXT)

## Why Cleaning Matters

**Hard Truth:**  
Real data is almost always messy. Professional data work is ~80% cleaning, ~20% analysis.

**Common Real-World Issues:**
- Missing values (NaN, null, empty cells)
- Duplicate rows
- Inconsistent text ("Delhi" vs "delhi" vs " Delhi ")
- Wrong data types (numbers stored as text)
- Outliers and invalid values
- Inconsistent date formats
- Special characters and encoding issues

**Golden Rule:**  
> **Clean first → analyze later.**

**If you don't clean first:**
- Your analysis will be wrong
- Your charts will be misleading
- Your models will fail
- Your automation will break

---

## 1) Detecting Missing Values (NaN)

### Check for Missing Values

```python
# Check if any NaN exists
print(df.isnull().any())

# Count NaN per column
print(df.isnull().sum())

# Percentage of missing values
print(df.isnull().sum() / len(df) * 100)

# Total missing values in entire DataFrame
print(df.isnull().sum().sum())

# Visualize missing data pattern
print(df.isnull())
```

### Example Output

```python
df = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet"],
    "price": [80000, None, 25000],
    "stock": [10, None, None]
})

print(df.isnull().sum())

# Output:
# product    0
# price      1
# stock      2
# dtype: int64
```

---

## 2) Handling Missing Values — Strategy

### Decision Framework

| Situation | Action |
|-----------|--------|
| Few missing values (<5%) | Delete rows |
| Many missing values (>20%) | Fill or keep with flag |
| Missing in critical column | Delete rows |
| Missing in optional column | Fill with default |
| Time series data | Forward fill or interpolate |

---

## 3) Removing Missing Values (dropna)

### Remove Rows with ANY Missing Value

```python
# Drop any row that has at least one NaN
df_clean = df.dropna()

# Drop in-place (modify original)
df.dropna(inplace=True)
```

### Remove Rows Missing SPECIFIC Column

```python
# Only drop if price is missing
df_clean = df.dropna(subset=["price"])

# Drop if either price or stock is missing
df_clean = df.dropna(subset=["price", "stock"])
```

### Remove Rows Missing ALL Values

```python
# Only drop if ALL columns are NaN
df_clean = df.dropna(how="all")
```

### Threshold-Based Removal

```python
# Keep rows that have at least 3 non-NaN values
df_clean = df.dropna(thresh=3)
```

---

## 4) Filling Missing Values (fillna)

### Fill with Specific Value

```python
# Fill all NaN with 0
df_filled = df.fillna(0)

# Fill specific column
df["price"] = df["price"].fillna(0)

# Fill different columns with different values
df = df.fillna({
    "price": 0,
    "stock": df["stock"].mean(),
    "category": "Unknown"
})
```

### Fill with Statistical Measures

```python
# Fill with mean
df["price"] = df["price"].fillna(df["price"].mean())

# Fill with median (better for outliers)
df["price"] = df["price"].fillna(df["price"].median())

# Fill with mode (most common value)
df["category"] = df["category"].fillna(df["category"].mode()[0])
```

### Forward Fill and Backward Fill

```python
# Forward fill (use previous value)
df["price"] = df["price"].fillna(method="ffill")
# or
df["price"] = df["price"].ffill()

# Backward fill (use next value)
df["price"] = df["price"].fillna(method="bfill")
# or
df["price"] = df["price"].bfill()
```

### Interpolate (For Time Series)

```python
# Linear interpolation
df["temperature"] = df["temperature"].interpolate()

# Polynomial interpolation
df["value"] = df["value"].interpolate(method="polynomial", order=2)
```

---

## 5) Detecting Duplicates

### Check for Duplicates

```python
# Check if any duplicates exist
print(df.duplicated().any())

# Count total duplicates
print(df.duplicated().sum())

# Show duplicate rows
duplicates = df[df.duplicated()]
print(duplicates)

# Show all occurrences (including first)
all_duplicates = df[df.duplicated(keep=False)]
```

### Check Duplicates in Specific Columns

```python
# Check duplicates based on product column only
print(df.duplicated(subset=["product"]).sum())

# Based on multiple columns
print(df.duplicated(subset=["product", "city"]).sum())
```

---

## 6) Removing Duplicates

### Remove All Duplicate Rows

```python
# Keep first occurrence, remove rest
df_clean = df.drop_duplicates()

# Keep last occurrence
df_clean = df.drop_duplicates(keep="last")

# Remove all duplicates (including first)
df_clean = df.drop_duplicates(keep=False)

# In-place removal
df.drop_duplicates(inplace=True)
```

### Remove Duplicates Based on Specific Columns

```python
# Remove duplicates based on product only
df_clean = df.drop_duplicates(subset=["product"])

# Based on product AND city combination
df_clean = df.drop_duplicates(subset=["product", "city"])

# Keep the row with highest price among duplicates
df_clean = df.sort_values("price").drop_duplicates(
    subset=["product"], 
    keep="last"
)
```

---

## 7) Cleaning Text Data

### Remove Whitespace

```python
# Remove leading/trailing spaces
df["city"] = df["city"].str.strip()

# Remove leading spaces only
df["city"] = df["city"].str.lstrip()

# Remove trailing spaces only
df["city"] = df["city"].str.rstrip()

# Remove all whitespace (including internal)
df["product"] = df["product"].str.replace(" ", "")
```

### Standardize Case

```python
# Convert to lowercase
df["city"] = df["city"].str.lower()

# Convert to uppercase
df["city"] = df["city"].str.upper()

# Convert to title case
df["name"] = df["name"].str.title()

# Convert to sentence case (first letter capital)
df["name"] = df["name"].str.capitalize()
```

### Replace Text

```python
# Simple replacement
df["city"] = df["city"].str.replace("delhi", "Delhi")

# Multiple replacements
df["product"] = df["product"].str.replace("phone", "mobile")
df["product"] = df["product"].str.replace("laptop", "notebook")

# Using dictionary for multiple replacements
replacements = {
    "delhi": "Delhi",
    "mumbai": "Mumbai",
    "pune": "Pune"
}
df["city"] = df["city"].replace(replacements)

# Regex replacement
df["text"] = df["text"].str.replace(r"\d+", "", regex=True)  # Remove digits
```

### Remove Special Characters

```python
# Remove punctuation
df["text"] = df["text"].str.replace(r'[^\w\s]', '', regex=True)

# Remove numbers
df["text"] = df["text"].str.replace(r'\d+', '', regex=True)

# Keep only letters and spaces
df["text"] = df["text"].str.replace(r'[^a-zA-Z\s]', '', regex=True)
```

---

## 8) Fixing Data Types

### Check Current Types

```python
# See all column types
print(df.dtypes)

# Check specific column
print(df["price"].dtype)

# Get detailed info
print(df.info())
```

### Convert to Numeric

```python
# Basic conversion
df["price"] = df["price"].astype(float)

# Safe conversion (errors become NaN)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Convert with specific handling
df["price"] = pd.to_numeric(df["price"], errors="ignore")  # Keep original if fails
```

### Convert to String

```python
# Convert to string
df["phone"] = df["phone"].astype(str)

# Remove decimal points from converted numbers
df["id"] = df["id"].astype(int).astype(str)
```

### Convert to DateTime

```python
# Basic conversion
df["date"] = pd.to_datetime(df["date"])

# With specific format
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Handle errors
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# With dayfirst (for DD/MM/YYYY)
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
```

### Convert to Category (Save Memory)

```python
# For columns with few unique values
df["city"] = df["city"].astype("category")
df["status"] = df["status"].astype("category")

# Significant memory savings for large datasets
```

---

## 9) Handling Outliers

### Detect Outliers

```python
# Statistical method (IQR)
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

# Z-score method
from scipy import stats
z_scores = stats.zscore(df["price"])
outliers = df[abs(z_scores) > 3]
```

### Handle Outliers

```python
# Remove outliers
df_clean = df[(df["price"] >= lower_bound) & (df["price"] <= upper_bound)]

# Cap outliers
df["price"] = df["price"].clip(lower=lower_bound, upper=upper_bound)

# Replace with median
median = df["price"].median()
df.loc[df["price"] > upper_bound, "price"] = median
```

---

## 10) Complete Cleaning Pipeline

### Professional Cleaning Workflow

```python
def clean_dataframe(df):
    """
    Complete data cleaning pipeline
    """
    # 1. Make a copy
    df_clean = df.copy()
    
    # 2. Remove duplicates
    print(f"Rows before duplicate removal: {len(df_clean)}")
    df_clean = df_clean.drop_duplicates()
    print(f"Rows after duplicate removal: {len(df_clean)}")
    
    # 3. Clean text columns
    text_columns = df_clean.select_dtypes(include=['object']).columns
    for col in text_columns:
        df_clean[col] = df_clean[col].str.strip()
        df_clean[col] = df_clean[col].str.lower()
    
    # 4. Fix data types
    # Convert price columns to numeric
    for col in df_clean.columns:
        if 'price' in col.lower() or 'revenue' in col.lower():
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # 5. Handle missing values
    print(f"\nMissing values before:\n{df_clean.isnull().sum()}")
    
    # Fill numeric columns with median
    numeric_cols = df_clean.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    
    # Fill text columns with 'Unknown'
    for col in text_columns:
        df_clean[col] = df_clean[col].fillna('unknown')
    
    print(f"\nMissing values after:\n{df_clean.isnull().sum()}")
    
    # 6. Remove outliers (optional)
    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        df_clean = df_clean[
            (df_clean[col] >= Q1 - 1.5 * IQR) & 
            (df_clean[col] <= Q3 + 1.5 * IQR)
        ]
    
    print(f"\nFinal row count: {len(df_clean)}")
    
    return df_clean

# Usage
df_cleaned = clean_dataframe(df)
```

---

## 11) Validation After Cleaning

### Check Your Cleaned Data

```python
# 1. Check shape
print(f"Shape: {df_clean.shape}")

# 2. Check data types
print(f"\nData types:\n{df_clean.dtypes}")

# 3. Check for missing values
print(f"\nMissing values:\n{df_clean.isnull().sum()}")

# 4. Check for duplicates
print(f"\nDuplicates: {df_clean.duplicated().sum()}")

# 5. Statistical summary
print(f"\nSummary:\n{df_clean.describe()}")

# 6. Check unique values
for col in df_clean.select_dtypes(include=['object']).columns:
    print(f"\n{col} unique values: {df_clean[col].nunique()}")
    print(df_clean[col].value_counts().head())
```

---

## 12) Common Cleaning Patterns

### Pattern 1: Clean Phone Numbers

```python
# Remove all non-numeric characters
df["phone"] = df["phone"].str.replace(r"\D", "", regex=True)

# Ensure 10 digits
df = df[df["phone"].str.len() == 10]

# Add country code
df["phone"] = "+91" + df["phone"]
```

### Pattern 2: Clean Email Addresses

```python
# Convert to lowercase
df["email"] = df["email"].str.lower().str.strip()

# Validate email format
df["valid_email"] = df["email"].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$")

# Remove invalid emails
df = df[df["valid_email"] == True]
```

### Pattern 3: Clean Currency Values

```python
# Remove currency symbols and commas
df["price"] = df["price"].str.replace(r"[$,₹]", "", regex=True)

# Convert to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
```

### Pattern 4: Standardize Country Names

```python
# Mapping dictionary
country_map = {
    "usa": "United States",
    "u.s.a": "United States",
    "us": "United States",
    "uk": "United Kingdom",
    "u.k": "United Kingdom"
}

df["country"] = df["country"].str.lower().str.strip()
df["country"] = df["country"].replace(country_map)
```

---

## 13) Memory Optimization

### Reduce Memory Usage

```python
# Check current memory usage
print(df.memory_usage(deep=True))

# Convert to category for repeated values
df["city"] = df["city"].astype("category")

# Downcast numeric types
df["age"] = pd.to_numeric(df["age"], downcast="integer")
df["price"] = pd.to_numeric(df["price"], downcast="float")

# Check new memory usage
print(df.memory_usage(deep=True))
```

---

## 14) Export Cleaned Data

### Save Cleaned Dataset

```python
# Save to CSV
df_clean.to_csv("cleaned_data.csv", index=False)

# Save to Excel
df_clean.to_excel("cleaned_data.xlsx", index=False)

# Save with compression
df_clean.to_csv("cleaned_data.csv.gz", index=False, compression="gzip")

# Save specific columns only
df_clean[["product", "price", "city"]].to_csv(
    "cleaned_subset.csv", 
    index=False
)
```

---

## Mental Model for Cleaning

> **Clean first → analyze later**

**Standard Cleaning Order:**
1. **Inspect** — Check shape, types, missing values
2. **Remove Duplicates** — Drop exact duplicates
3. **Clean Text** — Strip, lowercase, replace
4. **Fix Types** — Convert to correct data types
5. **Handle Missing** — Drop or fill NaN
6. **Validate** — Check results
7. **Save** — Export cleaned data

---

## Quick Cleaning Checklist

Use this for every dataset:

```python
# ✅ 1. Initial inspection
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# ✅ 2. Remove duplicates
df = df.drop_duplicates()

# ✅ 3. Clean text
text_cols = df.select_dtypes(include=['object']).columns
for col in text_cols:
    df[col] = df[col].str.strip().str.lower()

# ✅ 4. Handle missing values
df = df.dropna(subset=["critical_column"])
df["price"] = df["price"].fillna(df["price"].median())

# ✅ 5. Fix types
df["date"] = pd.to_datetime(df["date"])
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# ✅ 6. Validate
print(f"Final shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
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
✅ **Merge and join multiple tables**  
✅ **Stack and concatenate DataFrames**  
✅ **Pivot data into summary tables**  
✅ **Reshape data between wide and long formats**  
✅ **Clean messy real-world data professionally**  
✅ **Detect and handle missing values strategically**  
✅ **Remove duplicates intelligently**  
✅ **Standardize text data**  
✅ **Fix data types and handle outliers**  
✅ **Build complete data cleaning pipelines**  
✅ **Work with time series data**  
✅ **Create visualizations with pandas**

**This is professional-level pandas competency ready for real-world projects.**

---

# SESSION 11 — TIME SERIES & DATE/TIME OPERATIONS

## Why Time Series Matters

**Time-based data is everywhere:**
- Sales trends over months
- Stock prices by day
- Website traffic by hour
- Sensor readings by second
- Employee attendance over years

**Pandas is built for time series analysis.**

---

## 1) Converting to DateTime

### Basic Conversion

```python
# Convert string column to datetime
df["date"] = pd.to_datetime(df["date"])

# Example
df = pd.DataFrame({
    "date": ["2024-01-15", "2024-01-16", "2024-01-17"],
    "sales": [100, 150, 120]
})

df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
# date     datetime64[ns]
# sales             int64
```

### Handling Different Date Formats

```python
# Specific format (faster)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Common formats
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")  # 15/01/2024
df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")  # 01-15-2024
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")    # 20240115

# Day first (for European dates)
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Handle errors
df["date"] = pd.to_datetime(df["date"], errors="coerce")  # Invalid → NaT
```

### Date Format Codes Reference

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2024 |
| `%y` | 2-digit year | 24 |
| `%m` | Month (01-12) | 01 |
| `%d` | Day (01-31) | 15 |
| `%H` | Hour (00-23) | 14 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%b` | Month abbr | Jan |
| `%B` | Month full | January |

---

## 2) Extracting Date Components

### Extract Year, Month, Day

```python
df["date"] = pd.to_datetime(df["date"])

# Extract components
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["quarter"] = df["date"].dt.quarter

# Day of week
df["day_of_week"] = df["date"].dt.dayofweek  # 0=Monday, 6=Sunday
df["day_name"] = df["date"].dt.day_name()    # Monday, Tuesday, etc.

# Week of year
df["week"] = df["date"].dt.isocalendar().week

# Example
# date         year  month  day  day_name
# 2024-01-15   2024    1    15   Monday
# 2024-02-20   2024    2    20   Tuesday
```

### Extract Time Components

```python
df["datetime"] = pd.to_datetime(df["datetime"])

# Time components
df["hour"] = df["datetime"].dt.hour
df["minute"] = df["datetime"].dt.minute
df["second"] = df["datetime"].dt.second

# Just date (remove time)
df["date_only"] = df["datetime"].dt.date

# Just time (remove date)
df["time_only"] = df["datetime"].dt.time
```

---

## 3) Date Arithmetic

### Calculate Time Differences

```python
# Difference between dates
df["days_since_start"] = (df["end_date"] - df["start_date"]).dt.days

# Example
df = pd.DataFrame({
    "start": ["2024-01-01", "2024-01-15"],
    "end": ["2024-01-10", "2024-02-01"]
})

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

df["duration"] = (df["end"] - df["start"]).dt.days
# duration: [9, 17]
```

### Add/Subtract Time Periods

```python
# Add days
df["next_week"] = df["date"] + pd.Timedelta(days=7)

# Add months (more complex)
df["next_month"] = df["date"] + pd.DateOffset(months=1)

# Subtract years
df["last_year"] = df["date"] - pd.DateOffset(years=1)

# Add business days (skip weekends)
df["next_business_day"] = df["date"] + pd.offsets.BDay(1)
```

### Time Deltas

```python
# Create time deltas
one_day = pd.Timedelta(days=1)
one_hour = pd.Timedelta(hours=1)
thirty_mins = pd.Timedelta(minutes=30)

# Use in calculations
df["tomorrow"] = df["date"] + one_day
df["in_one_hour"] = df["timestamp"] + one_hour
```

---

## 4) Filtering by Date

### Simple Date Filtering

```python
# After a specific date
recent = df[df["date"] >= "2024-01-01"]

# Before a specific date
old = df[df["date"] < "2024-01-01"]

# Between two dates
jan_sales = df[
    (df["date"] >= "2024-01-01") &
    (df["date"] <= "2024-01-31")
]

# Specific month
january = df[df["date"].dt.month == 1]

# Specific year
year_2024 = df[df["date"].dt.year == 2024]

# Specific day of week (Mondays only)
mondays = df[df["date"].dt.dayofweek == 0]
```

### Advanced Date Filtering

```python
# Last 30 days
cutoff_date = pd.Timestamp.now() - pd.Timedelta(days=30)
recent = df[df["date"] >= cutoff_date]

# This year only
this_year = df[df["date"].dt.year == pd.Timestamp.now().year]

# Weekdays only
weekdays = df[df["date"].dt.dayofweek < 5]

# Weekends only
weekends = df[df["date"].dt.dayofweek >= 5]
```

---

## 5) Resampling Time Series Data

### Concept
**Resampling** = changing the frequency of time series data

**Common uses:**
- Daily → Monthly aggregation
- Hourly → Daily summaries
- Irregular → Regular intervals

### Set Date as Index First

```python
# IMPORTANT: Set datetime column as index
df = df.set_index("date")
```

### Resample to Different Frequencies

```python
# Daily to monthly (sum)
monthly = df.resample("M").sum()

# Daily to weekly (mean)
weekly = df.resample("W").mean()

# Hourly to daily (max)
daily = df.resample("D").max()

# Quarterly summary
quarterly = df.resample("Q").sum()
```

### Resample Frequency Codes

| Code | Meaning |
|------|---------|
| `D` | Day |
| `W` | Week |
| `M` | Month end |
| `MS` | Month start |
| `Q` | Quarter end |
| `QS` | Quarter start |
| `Y` | Year end |
| `YS` | Year start |
| `H` | Hour |
| `T` or `min` | Minute |
| `S` | Second |

### Multiple Aggregations

```python
# Multiple statistics
monthly_summary = df.resample("M").agg({
    "sales": ["sum", "mean", "max"],
    "customers": "count"
})
```

---

## 6) Rolling Window Calculations

### Moving Averages

```python
# 7-day moving average
df["sales_7d_avg"] = df["sales"].rolling(window=7).mean()

# 30-day moving average
df["sales_30d_avg"] = df["sales"].rolling(window=30).mean()

# Example
#   date       sales  sales_7d_avg
# 2024-01-01    100      NaN
# 2024-01-02    120      NaN
# ...
# 2024-01-07    130    115.0  ← average of 7 days
```

### Other Rolling Calculations

```python
# Rolling sum
df["sales_7d_sum"] = df["sales"].rolling(window=7).sum()

# Rolling max
df["sales_7d_max"] = df["sales"].rolling(window=7).max()

# Rolling standard deviation
df["sales_7d_std"] = df["sales"].rolling(window=7).std()

# Center the window (better for smoothing)
df["sales_smooth"] = df["sales"].rolling(window=7, center=True).mean()
```

---

## 7) Shifting Data (Lag/Lead)

### Create Lag Variables

```python
# Previous day's sales
df["sales_yesterday"] = df["sales"].shift(1)

# Sales from 7 days ago
df["sales_last_week"] = df["sales"].shift(7)

# Calculate day-over-day change
df["sales_change"] = df["sales"] - df["sales"].shift(1)

# Percentage change
df["sales_pct_change"] = df["sales"].pct_change() * 100
```

### Lead Variables (Future Values)

```python
# Next day's sales
df["sales_tomorrow"] = df["sales"].shift(-1)

# Sales 7 days ahead
df["sales_next_week"] = df["sales"].shift(-7)
```

---

## 8) Creating Date Ranges

### Generate Date Sequences

```python
# Date range (daily)
dates = pd.date_range(start="2024-01-01", end="2024-01-31", freq="D")

# Date range with periods
dates = pd.date_range(start="2024-01-01", periods=30, freq="D")

# Business days only
business_dates = pd.bdate_range(start="2024-01-01", end="2024-01-31")

# Hourly timestamps
hours = pd.date_range(start="2024-01-01", periods=24, freq="H")

# Create DataFrame with date range
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=30, freq="D"),
    "value": range(30)
})
```

---

## 9) Real-World Time Series Examples

### Example 1: Monthly Sales Analysis

```python
# Load sales data
sales = pd.read_csv("sales.csv")
sales["date"] = pd.to_datetime(sales["date"])

# Extract month and year
sales["month"] = sales["date"].dt.month
sales["year"] = sales["date"].dt.year

# Monthly summary
monthly = sales.groupby(["year", "month"])["revenue"].sum()

# Or using resample
sales = sales.set_index("date")
monthly = sales["revenue"].resample("M").sum()
```

### Example 2: Year-over-Year Comparison

```python
# Pivot for comparison
comparison = sales.pivot_table(
    values="revenue",
    index=sales["date"].dt.month,
    columns=sales["date"].dt.year,
    aggfunc="sum"
)

# Calculate growth
comparison["growth_%"] = (
    (comparison[2024] - comparison[2023]) / comparison[2023] * 100
)
```

### Example 3: Trend Detection

```python
# Set date as index
df = df.set_index("date")

# Add moving average
df["trend"] = df["sales"].rolling(window=30).mean()

# Detect if above or below trend
df["above_trend"] = df["sales"] > df["trend"]
```

---

## 10) Common Time Series Patterns

### Fill Missing Dates

```python
# Create complete date range
full_dates = pd.date_range(
    start=df["date"].min(),
    end=df["date"].max(),
    freq="D"
)

# Reindex to include all dates
df = df.set_index("date")
df = df.reindex(full_dates, fill_value=0)
```

### Working with Timezones

```python
# Convert to timezone-aware
df["datetime"] = pd.to_datetime(df["datetime"])
df["datetime"] = df["datetime"].dt.tz_localize("UTC")

# Convert between timezones
df["datetime_ist"] = df["datetime"].dt.tz_convert("Asia/Kolkata")

# Remove timezone
df["datetime"] = df["datetime"].dt.tz_localize(None)
```

---

## Mental Model for Time Series

> **Convert → Extract → Filter → Aggregate → Analyze**

**Standard Time Series Workflow:**
1. Convert to datetime
2. Extract components (year, month, day)
3. Filter by date ranges
4. Aggregate by time periods (resample)
5. Calculate trends (rolling, shift)
6. Visualize patterns

---

# SESSION 12 — DATA VISUALIZATION WITH PANDAS

## Why Visualization Matters

**"A picture is worth a thousand rows."**

**Visualization helps you:**
- Spot patterns quickly
- Find outliers easily
- Communicate insights effectively
- Validate your analysis
- Make data-driven decisions

**Pandas integrates directly with Matplotlib for quick plots.**

---

## 1) Basic Plotting Setup

### Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

# Set style (optional but recommended)
plt.style.use("seaborn-v0_8-darkgrid")

# For Jupyter notebooks
%matplotlib inline
```

---

## 2) Line Plots

### Basic Line Plot

```python
# Sample data
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=30, freq="D"),
    "sales": [100 + i*2 for i in range(30)]
})

# Simple line plot
df.plot(x="date", y="sales", kind="line")
plt.show()

# Or shorter
df.set_index("date")["sales"].plot()
plt.title("Sales Over Time")
plt.ylabel("Sales")
plt.show()
```

### Multiple Lines

```python
# Multiple columns
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=30),
    "product_A": range(100, 130),
    "product_B": range(80, 110)
})

df.set_index("date").plot()
plt.title("Product Sales Comparison")
plt.ylabel("Sales")
plt.legend()
plt.show()
```

### Customized Line Plot

```python
df.set_index("date").plot(
    figsize=(12, 6),
    title="Sales Trend",
    color=["blue", "red"],
    linewidth=2,
    grid=True
)
plt.ylabel("Revenue")
plt.show()
```

---

## 3) Bar Charts

### Vertical Bar Chart

```python
# Sales by city
df = pd.DataFrame({
    "city": ["Delhi", "Mumbai", "Pune", "Bangalore"],
    "sales": [80000, 90000, 70000, 85000]
})

df.plot(x="city", y="sales", kind="bar")
plt.title("Sales by City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()
```

### Horizontal Bar Chart

```python
df.plot(x="city", y="sales", kind="barh")
plt.title("Sales by City")
plt.xlabel("Revenue")
plt.show()
```

### Grouped Bar Chart

```python
# Multiple products by city
df = pd.DataFrame({
    "city": ["Delhi", "Mumbai", "Pune"],
    "Laptop": [80000, 90000, 70000],
    "Phone": [30000, 35000, 25000]
})

df.set_index("city").plot(kind="bar")
plt.title("Product Sales by City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.legend(title="Product")
plt.show()
```

### Stacked Bar Chart

```python
df.set_index("city").plot(kind="bar", stacked=True)
plt.title("Total Sales by City")
plt.ylabel("Revenue")
plt.show()
```

---

## 4) Histograms (Distribution)

### Basic Histogram

```python
# Distribution of prices
df = pd.DataFrame({
    "price": [10000, 15000, 20000, 25000, 30000, 35000, 40000, 
              15000, 20000, 25000, 30000, 25000, 20000]
})

df["price"].plot(kind="hist", bins=10, edgecolor="black")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
```

### Customized Histogram

```python
df["price"].plot(
    kind="hist",
    bins=20,
    alpha=0.7,
    color="skyblue",
    edgecolor="black"
)
plt.title("Price Distribution")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.grid(axis="y", alpha=0.3)
plt.show()
```

---

## 5) Box Plots (Outlier Detection)

### Basic Box Plot

```python
# Sales across different regions
df = pd.DataFrame({
    "region": ["North", "South", "East", "West"] * 10,
    "sales": [80 + i*5 for i in range(40)]
})

df.boxplot(column="sales", by="region")
plt.title("Sales Distribution by Region")
plt.suptitle("")  # Remove default title
plt.ylabel("Sales")
plt.show()
```

### Multiple Box Plots

```python
df[["product_A", "product_B", "product_C"]].plot(kind="box")
plt.title("Product Sales Distribution")
plt.ylabel("Revenue")
plt.show()
```

---

## 6) Scatter Plots

### Basic Scatter Plot

```python
# Relationship between advertising and sales
df = pd.DataFrame({
    "advertising": [1000, 2000, 3000, 4000, 5000],
    "sales": [10000, 15000, 22000, 28000, 35000]
})

df.plot(x="advertising", y="sales", kind="scatter")
plt.title("Advertising vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.show()
```

### Colored Scatter Plot

```python
# Color by third variable
df.plot(
    x="advertising",
    y="sales",
    kind="scatter",
    c="profit",  # Color by profit
    cmap="viridis",
    s=100  # Size of points
)
plt.title("Sales vs Advertising (colored by profit)")
plt.colorbar(label="Profit")
plt.show()
```

---

## 7) Pie Charts

### Basic Pie Chart

```python
# Market share
df = pd.DataFrame({
    "company": ["Company A", "Company B", "Company C", "Company D"],
    "market_share": [35, 25, 20, 20]
})

df.set_index("company")["market_share"].plot(kind="pie")
plt.title("Market Share Distribution")
plt.ylabel("")  # Remove y-label
plt.show()
```

### Customized Pie Chart

```python
df.set_index("company")["market_share"].plot(
    kind="pie",
    autopct='%1.1f%%',  # Show percentages
    startangle=90,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
)
plt.title("Market Share Distribution")
plt.ylabel("")
plt.show()
```

---

## 8) Area Plots

### Basic Area Plot

```python
# Cumulative sales
df = pd.DataFrame({
    "month": range(1, 13),
    "product_A": [100 + i*10 for i in range(12)],
    "product_B": [80 + i*8 for i in range(12)]
})

df.set_index("month").plot(kind="area", alpha=0.7)
plt.title("Cumulative Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

### Stacked Area Plot

```python
df.set_index("month").plot(kind="area", stacked=True, alpha=0.5)
plt.title("Total Sales Over Time")
plt.ylabel("Total Revenue")
plt.show()
```

---

## 9) Subplots (Multiple Charts)

### Create Subplots

```python
# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line plot
df["sales"].plot(ax=axes[0, 0], title="Sales Trend")

# Plot 2: Bar chart
df["sales"].plot(kind="bar", ax=axes[0, 1], title="Sales by Period")

# Plot 3: Histogram
df["sales"].plot(kind="hist", ax=axes[1, 0], title="Sales Distribution")

# Plot 4: Box plot
df[["sales"]].plot(kind="box", ax=axes[1, 1], title="Sales Box Plot")

plt.tight_layout()
plt.show()
```

---

## 10) Customization & Styling

### Complete Customization Example

```python
# Professional-looking plot
plt.figure(figsize=(12, 6))

df.set_index("date")["sales"].plot(
    color="steelblue",
    linewidth=2,
    marker="o",
    markersize=4
)

plt.title("Daily Sales Performance", fontsize=16, fontweight="bold")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Revenue (₹)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(["Sales"], loc="upper left")

# Add horizontal line for target
plt.axhline(y=df["sales"].mean(), color="red", linestyle="--", 
            label="Average", alpha=0.7)

plt.tight_layout()
plt.show()
```

### Save Plots

```python
# Save as PNG
plt.savefig("sales_chart.png", dpi=300, bbox_inches="tight")

# Save as PDF
plt.savefig("sales_chart.pdf", bbox_inches="tight")

# Save as SVG (vector format)
plt.savefig("sales_chart.svg", bbox_inches="tight")
```

---

## 11) Quick Plotting Patterns

### Pattern 1: Quick Data Overview

```python
# Automatic plotting of all numeric columns
df.plot(subplots=True, figsize=(10, 8))
plt.tight_layout()
plt.show()
```

### Pattern 2: Correlation Heatmap

```python
import seaborn as sns

# Correlation matrix
corr = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()
```

### Pattern 3: Time Series with Trend

```python
df = df.set_index("date")

# Plot sales with moving average
ax = df["sales"].plot(label="Sales", alpha=0.7)
df["sales"].rolling(7).mean().plot(
    ax=ax, 
    label="7-day Average", 
    linewidth=2
)
plt.legend()
plt.title("Sales with Trend")
plt.show()
```

---

## 12) Plot Types Reference

| Plot Type | Use For | pandas Method |
|-----------|---------|---------------|
| Line | Trends over time | `.plot(kind="line")` |
| Bar | Category comparison | `.plot(kind="bar")` |
| Histogram | Distribution | `.plot(kind="hist")` |
| Box | Outliers & quartiles | `.plot(kind="box")` |
| Scatter | Relationships | `.plot(kind="scatter")` |
| Pie | Proportions | `.plot(kind="pie")` |
| Area | Cumulative trends | `.plot(kind="area")` |

---

## 13) Visualization Best Practices

### Do's ✅

```python
# Clear titles and labels
plt.title("Monthly Revenue Trend", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (₹)", fontsize=12)

# Readable font sizes
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add grid for easier reading
plt.grid(True, alpha=0.3)

# Use color strategically
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Include legends
plt.legend(loc="best")
```

### Don'ts ❌

- Don't use 3D charts (hard to read)
- Don't use too many colors
- Don't skip axis labels
- Don't make plots too small
- Don't use pie charts for >5 categories

---

## Mental Model for Visualization

> **Explore → Choose → Create → Customize → Interpret**

**Standard Visualization Workflow:**
1. **Explore data** — Understand what you have
2. **Choose plot type** — Match to your question
3. **Create basic plot** — Get it working
4. **Customize** — Make it clear and professional
5. **Interpret** — What story does it tell?

---

## Quick Visualization Cheat Sheet

```python
# Quick exploration plots

# 1. Distribution
df["column"].plot(kind="hist", bins=20)

# 2. Trend
df.set_index("date")["value"].plot()

# 3. Comparison
df.groupby("category")["value"].sum().plot(kind="bar")

# 4. Correlation
df.plot(x="col1", y="col2", kind="scatter")

# 5. All columns overview
df.plot(subplots=True, figsize=(12, 8))
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
✅ **Merge and join multiple tables**  
✅ **Stack and concatenate DataFrames**  
✅ **Pivot data into summary tables**  
✅ **Reshape data between wide and long formats**  
✅ **Clean messy real-world data professionally**  
✅ **Detect and handle missing values strategically**  
✅ **Remove duplicates intelligently**  
✅ **Standardize text data**  
✅ **Fix data types and handle outliers**  
✅ **Build complete data cleaning pipelines**

**This is professional-level pandas competency ready for real-world projects.**

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

## 📚 Advanced Topics Covered

### ✅ Completed in These Notes:
1. **Merge/Join operations** — Session 8: Combining multiple DataFrames
2. **Pivot tables** — Session 9: Reshaping data for analysis
3. **Time series** — Session 11: Working with dates and times
4. **Visualization** — Session 12: Creating charts with pandas + matplotlib

### 🚀 Beyond These Notes (Next Level):
5. **Performance Optimization**
   - Working with large datasets (>1GB)
   - Memory-efficient data types
   - Chunking for big files
   - Dask for parallel processing

6. **Database Integration**
   - Reading from SQL databases
   - Writing to databases
   - SQLAlchemy integration

7. **Advanced Techniques**
   - Multi-index DataFrames
   - Custom aggregation functions
   - Window functions (expanding, ewm)
   - Categorical data optimization

---

## 🎯 Recommended Practice Projects

### 1. Sales Analysis Dashboard
**Skills Used:** Loading, cleaning, pivot tables, visualization
```
- Load monthly sales data from Excel/CSV
- Clean and prepare data
- Create pivot tables for insights
- Visualize trends and comparisons
- Generate automated reports
```

### 2. Customer Segmentation Analysis
**Skills Used:** Groupby, filtering, custom columns, visualization
```
- Analyze customer purchase behavior
- Group customers by patterns
- Calculate RFM scores (Recency, Frequency, Monetary)
- Visualize customer segments
- Identify high-value customers
```

### 3. Time Series Forecasting
**Skills Used:** DateTime operations, resampling, rolling windows
```
- Load historical sales/stock data
- Identify trends and seasonality
- Calculate moving averages
- Detect anomalies
- Create forecast visualizations
```

### 4. Personal Expense Tracker
**Skills Used:** File handling, groupby, pivot, visualization
```
- Import bank statements/expense data
- Categorize expenses
- Monthly/yearly summaries
- Budget vs actual comparisons
- Spending trend analysis
- Category-wise breakdown
```

### 5. E-commerce Data Pipeline
**Skills Used:** Merging, cleaning, aggregation, visualization
```
- Combine orders, customers, products tables
- Clean inconsistent data
- Calculate metrics (AOV, conversion rate)
- Create sales dashboards
- Identify best-selling products
```

### 6. WhatsApp Contact Automation
**Skills Used:** Text cleaning, duplicates, validation, export
```
- Load contacts from Excel/CSV
- Remove duplicates and invalid entries
- Standardize phone numbers
- Format for WhatsApp API
- Export clean contact lists
```

---

## 📖 Resources for Further Learning

### Official Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

### Practice Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets) — Thousands of real datasets
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Data.gov](https://data.gov/) — US Government data
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [World Bank Open Data](https://data.worldbank.org/)

### Interactive Learning
- **Kaggle Learn** — Free Pandas course with exercises
- **DataCamp** — Interactive pandas courses
- **Real Python** — Comprehensive pandas tutorials
- **YouTube** — Corey Schafer's Pandas series
- **GitHub** — Real pandas projects to study

### Books
- "Python for Data Analysis" by Wes McKinney (Pandas creator)
- "Pandas Cookbook" by Theodore Petrou
- "Effective Pandas" by Matt Harrison

---

## 🎓 Your Learning Journey

**You started with:**
- ❓ No pandas knowledge
- ❓ Basic Python understanding
- ❓ Manual Excel work

**You now have:**
- ✅ Complete pandas fundamentals (Sessions 1-7)
- ✅ Data combination skills (Session 8)
- ✅ Reshaping expertise (Session 9)
- ✅ Professional cleaning workflows (Session 10)
- ✅ Time series mastery (Session 11)
- ✅ Visualization capabilities (Session 12)
- ✅ Real-world project readiness

**Your next milestone:**
Build **3 real projects** using these skills to solidify your knowledge!

---

## 💡 Tips for Continued Success

1. **Practice Daily** — Even 15 minutes with real data
2. **Start Small** — Begin with your own data (expenses, habits, etc.)
3. **Break Problems Down** — Complex analysis = many small steps
4. **Read Others' Code** — Study Kaggle notebooks
5. **Document Your Work** — Write comments explaining your logic
6. **Build a Portfolio** — Share projects on GitHub
7. **Join Communities** — r/learnpython, Stack Overflow, Kaggle forums
8. **Teach Others** — Best way to solidify understanding

---

## 🔥 Final Words

**Remember:**
- Pandas is a tool, not the goal
- Focus on solving real problems
- Clean code > clever code
- Visualization tells the story
- Keep these notes handy as reference

**You're ready for real-world data work!**

Start your first project today. 🚀

---

# END OF PANDAS MASTER NOTES

**Remember:** The best way to learn pandas is by doing.  
Take any dataset and start exploring!

---

**Version:** Complete Edition (Sessions 1-7)  
**Last Updated:** 2024  
**Author:** Prerak (Apex Tutor Method)