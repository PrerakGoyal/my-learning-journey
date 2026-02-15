# 🚀 PYTHON AUTOMATION LIBRARIES - COMPLETE REVISION NOTES

**Quick Reference Guide for Professional Automation**

---

## 📋 TABLE OF CONTENTS

1. [Pandas - Data Manipulation](#pandas)
2. [OS - File System Operations](#os)
3. [Time - Delays & Timing](#time)
4. [Pathlib - Modern Path Handling](#pathlib)
5. [Requests - HTTP & APIs](#requests)
6. [Selenium - Browser Automation](#selenium)
7. [Integration Patterns](#integration-patterns)
8. [Golden Rules](#golden-rules)
9. [Quick Debugging Checklist](#quick-debugging-checklist)

---

# PANDAS

## Core Objects
```python
import pandas as pd

# Series = 1 column
ages = pd.Series([21, 23, 20])

# DataFrame = table (multiple Series)
df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [21, 23, 20]
})
```

## Reading/Writing Files
```python
# Read
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")

# Write
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

## DataFrame Anatomy
| Component | Access | Example |
|-----------|--------|---------|
| Columns | `df.columns` | Column names |
| Index | `df.index` | Row labels |
| Shape | `df.shape` | (rows, cols) |
| Types | `df.dtypes` | Data types |
| Info | `df.info()` | Overview |
| Stats | `df.describe()` | Summary stats |

## Selection
```python
# Columns
df["age"]                    # Series
df[["name", "age"]]         # DataFrame

# Rows by position (iloc)
df.iloc[0]                   # First row
df.iloc[0:3]                # First 3 rows
df.iloc[0, 1]               # Cell by position

# Rows by label (loc)
df.loc[:, "age"]            # All rows, age column
df.loc[:, ["name", "age"]]  # All rows, multiple cols
```

## Filtering (Boolean Indexing)
```python
# Single condition
df[df["age"] > 21]

# Multiple conditions - AND
df[(df["age"] > 20) & (df["city"] == "Pune")]

# Multiple conditions - OR
df[(df["city"] == "Pune") | (df["city"] == "Mumbai")]

# loc with filtering
df.loc[df["age"] > 21, ["name", "age"]]
```

## Column Operations
```python
# Create new column
df["age_next"] = df["age"] + 1
df["category"] = df["price"].apply(lambda x: "premium" if x >= 60000 else "budget")

# String operations (must use .str)
df["city_lower"] = df["city"].str.lower()
df["city_clean"] = df["city"].str.strip()

# Boolean column
df["is_expensive"] = df["price"] >= 50000
```

## Cleaning Data
```python
# Missing values
df.isna().sum()              # Count NaN
df.dropna()                  # Remove rows with NaN
df.dropna(subset=["price"])  # Remove only if price is NaN
df["price"].fillna(df["price"].mean())  # Fill with mean

# Duplicates
df.duplicated().sum()        # Count duplicates
df.drop_duplicates()         # Remove all duplicates
df.drop_duplicates(subset=["product"])  # Based on column

# Type conversion
df["price"] = df["price"].astype(int)
df["phone"] = df["phone"].astype(str)
pd.to_numeric(df["price"], errors="coerce")  # Convert safely
```

## Grouping & Aggregation
```python
# Single metric
df.groupby("city")["price"].mean()
df.groupby("city")["price"].sum()
df.groupby("city")["price"].count()

# Multiple metrics
df.groupby("city").agg({
    "price": "mean",
    "revenue": "sum"
})

# Filter then group
premium = df[df["category"] == "premium"]
premium.groupby("city")["price"].mean()
```

## Merging Tables
```python
# Concat (stack vertically)
pd.concat([df1, df2], ignore_index=True)

# Merge (SQL-like join)
pd.merge(df1, df2, on="id", how="inner")   # Inner join
pd.merge(df1, df2, on="id", how="left")    # Left join
pd.merge(df1, df2, on="id", how="right")   # Right join
pd.merge(df1, df2, on="id", how="outer")   # Outer join

# Join by index
df1.join(df2)
```

## Reshaping
```python
# Pivot table (summarize into grid)
df.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum"
)

# Melt (wide → long)
df.melt(
    id_vars=["city"],
    value_vars=["Laptop", "Phone"],
    var_name="product",
    value_name="revenue"
)
```

## Quick Reference
```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.shape            # (rows, cols)
df.columns          # Column names
df.info()           # Data types + memory
df.describe()       # Statistics
df.sort_values("age")  # Sort by column
```

---

# OS

## Core Operations
```python
import os

# Current directory
os.getcwd()                    # Get current working directory
os.chdir("path")              # Change directory

# List files
os.listdir(".")               # List current directory
os.listdir("C:/Users")        # List specific directory

# Create folders
os.mkdir("folder")            # Single folder
os.makedirs("path/to/folder", exist_ok=True)  # Nested folders

# Check existence
os.path.exists("file.txt")    # File/folder exists?
os.path.isfile("file.txt")    # Is it a file?
os.path.isdir("folder")       # Is it a directory?

# Join paths safely
os.path.join("folder", "file.txt")  # Works cross-platform

# Remove
os.remove("file.txt")         # Delete file
os.rmdir("folder")            # Delete empty folder
```

## Path Operations
```python
import os

path = "C:/Users/Name/file.txt"

os.path.dirname(path)   # "C:/Users/Name"
os.path.basename(path)  # "file.txt"
os.path.split(path)     # ("C:/Users/Name", "file.txt")
os.path.splitext(path)  # ("C:/Users/Name/file", ".txt")
os.path.abspath(".")    # Absolute path
```

## Real Automation Patterns
```python
# Find latest file in Downloads
import os
from pathlib import Path

download_dir = Path.home() / "Downloads"
files = list(download_dir.glob("*.csv"))
latest = max(files, key=lambda f: f.stat().st_mtime)

# Organize by extension
for file in os.listdir("."):
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1]
        folder = ext.replace(".", "")
        os.makedirs(folder, exist_ok=True)
```

---

# TIME

## Core Functions
```python
import time

# Pause execution
time.sleep(5)              # Wait 5 seconds
time.sleep(0.5)            # Wait 500ms

# Measure time
start = time.time()
# ... code ...
end = time.time()
duration = end - start

# High precision timing
start = time.perf_counter()
# ... code ...
duration = time.perf_counter() - start
```

## Timing Patterns
```python
# Simple timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.2f}s")
        return result
    return wrapper

# Countdown
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("GO!")

# Wait with progress
def wait_with_progress(seconds):
    for i in range(seconds, 0, -1):
        print(f"Waiting: {i}s", end='\r')
        time.sleep(1)
    print("Done!     ")
```

---

# PATHLIB

## Modern Path Handling
```python
from pathlib import Path

# Current directory
Path.cwd()

# Home directory
Path.home()

# Create path objects
p = Path("folder/file.txt")
p = Path("automation") / "cleaned_data" / "file.csv"

# Create folders
p = Path("automation/cleaned_data")
p.mkdir(parents=True, exist_ok=True)

# Check existence
p.exists()
p.is_file()
p.is_dir()

# File operations
p.read_text()           # Read file
p.write_text("data")    # Write file
p.unlink()              # Delete file

# Path properties
p.parent                # Parent directory
p.name                  # Filename
p.stem                  # Filename without extension
p.suffix                # Extension
```

## Real Patterns
```python
# Find all CSV files
files = Path(".").glob("*.csv")
files = Path(".").rglob("**/*.csv")  # Recursive

# Process files
for csv in Path("data").glob("*.csv"):
    df = pd.read_csv(csv)
    # Process...
    output = Path("output") / csv.name
    df.to_csv(output)
```

---

# REQUESTS

## Core HTTP Operations
```python
import requests

# GET request
r = requests.get("https://api.example.com")

# POST request
r = requests.post("https://api.example.com", data={"key": "value"})
r = requests.post("https://api.example.com", json={"key": "value"})

# Response attributes
r.status_code       # 200, 404, 500, etc.
r.text              # Raw text
r.content           # Raw bytes
r.json()            # Parse JSON
r.headers           # Response headers
```

## Status Codes
| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Use data |
| 201 | Created | Success |
| 400 | Bad Request | Fix request |
| 401 | Unauthorized | Check auth |
| 404 | Not Found | Check URL |
| 429 | Rate Limit | Wait |
| 500 | Server Error | Retry later |

## Headers & Authentication
```python
# Custom headers (avoid blocking)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json"
}
r = requests.get(url, headers=headers)

# Sessions (persist cookies)
session = requests.Session()
session.post("https://site.com/login", data={"user": "x", "pass": "y"})
r = session.get("https://site.com/dashboard")

# Basic auth
from requests.auth import HTTPBasicAuth
r = requests.get(url, auth=HTTPBasicAuth("user", "pass"))
r = requests.get(url, auth=("user", "pass"))  # Shorthand
```

## File Operations
```python
# Download file
url = "https://example.com/file.csv"
r = requests.get(url)

with open("file.csv", "wb") as f:
    f.write(r.content)

# Download with progress
r = requests.get(url, stream=True)
with open("file.csv", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
```

## Error Handling
```python
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()  # Raises HTTPError for bad status
    data = r.json()
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

# SELENIUM

## Setup & Basic Control
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create driver
driver = webdriver.Chrome()

# Navigate
driver.get("https://www.google.com")
driver.back()
driver.forward()
driver.refresh()

# Window management
driver.maximize_window()
driver.set_window_size(1920, 1080)

# Close
driver.close()  # Current window
driver.quit()   # All windows + session
```

## Finding Elements (Locator Priority)
```python
# 1. ID (BEST - fastest & most reliable)
driver.find_element(By.ID, "username")

# 2. NAME (good for forms)
driver.find_element(By.NAME, "email")

# 3. CSS SELECTOR (flexible)
driver.find_element(By.CSS_SELECTOR, ".btn-primary")
driver.find_element(By.CSS_SELECTOR, "input[type='text']")
driver.find_element(By.CSS_SELECTOR, "div.container > p")

# 4. XPATH (powerful but slower)
driver.find_element(By.XPATH, "//button[@type='submit']")
driver.find_element(By.XPATH, "//button[text()='Login']")
driver.find_element(By.XPATH, "//input[contains(@id,'user')]")

# 5. Others (use sparingly)
driver.find_element(By.CLASS_NAME, "btn")
driver.find_element(By.TAG_NAME, "button")
driver.find_element(By.LINK_TEXT, "Click Here")
```

## Interacting with Elements
```python
# Click
element = driver.find_element(By.ID, "submit")
element.click()

# Type text
element = driver.find_element(By.ID, "username")
element.send_keys("myusername")
element.clear()  # Clear existing text

# Get information
element.text                    # Visible text
element.get_attribute("value")  # Attribute value
element.is_displayed()          # Visible?
element.is_enabled()            # Enabled?
element.is_selected()           # Selected? (checkbox/radio)
```

## Professional Waits (NOT time.sleep!)
```python
# Explicit wait (RECOMMENDED)
wait = WebDriverWait(driver, 10)

# Wait for element to exist
element = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Wait for element to be clickable (MOST USED)
element = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)

# Wait for text
wait.until(
    EC.text_to_be_present_in_element((By.ID, "status"), "Complete")
)
```

## Common XPath Patterns
```python
# Contains attribute
"//input[contains(@id,'user')]"
"//div[contains(@class,'container')]"

# Match text
"//button[text()='Login']"
"//button[contains(text(),'Submit')]"

# Combine conditions
"//input[contains(@id,'user') and @type='text']"

# Parent/child navigation
"//form//input[@type='text']"
"//label[text()='Email']/following-sibling::input"
```

## Real Login Pattern
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://example.com/login")
    
    # Wait & type username
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("myuser")
    
    # Type password
    password = driver.find_element(By.ID, "password")
    password.send_keys("mypass")
    
    # Click login
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    login_btn.click()
    
    # Wait for redirect
    wait.until(EC.url_contains("dashboard"))
    
finally:
    driver.quit()
```

## Handling Common Issues
```python
# Click blocked by overlay
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# JavaScript click (last resort)
driver.execute_script("arguments[0].click();", element)

# Handle alerts
alert = driver.switch_to.alert
alert.accept()  # Click OK
alert.dismiss()  # Click Cancel

# Switch to iframe
driver.switch_to.frame("iframe_name")
driver.switch_to.default_content()  # Back to main
```

---

# INTEGRATION PATTERNS

## Complete Automation Pipeline
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
from pathlib import Path
import time

# 1. Selenium login
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://example.com/login")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("user")
driver.find_element(By.ID, "password").send_keys("pass")
wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

# 2. Copy cookies to requests
session = requests.Session()
for cookie in driver.get_cookies():
    session.cookies.set(cookie["name"], cookie["value"])

# 3. Download via requests
r = session.get("https://example.com/export.csv")
Path("downloads").mkdir(exist_ok=True)
with open("downloads/data.csv", "wb") as f:
    f.write(r.content)

# 4. Clean with pandas
df = pd.read_csv("downloads/data.csv")
df = df.dropna()
df = df.drop_duplicates()
df["revenue"] = df["price"] * df["quantity"]

# 5. Save output
Path("outputs").mkdir(exist_ok=True)
df.to_excel("outputs/clean_report.xlsx", index=False)

driver.quit()
```

## Error Handling Template
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_automation():
    driver = None
    try:
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        
        # Automation logic here
        driver.get("https://example.com")
        # ...
        
    except TimeoutException:
        logger.error("Element not found in time")
    except Exception as e:
        logger.error(f"Automation failed: {e}")
    finally:
        if driver:
            driver.quit()
```

---

# GOLDEN RULES

## Pandas
- **One column** → Series, **List of columns** → DataFrame
- Always use `df.copy()` before destructive operations
- Filter: `df[condition]`, Select: `df[["col"]]`, Both: `df.loc[condition, ["col"]]`
- Use `aggfunc` not `add` in pivot_table
- `contains()` in boolean indexing requires column name

## OS/Pathlib
- **ALWAYS** use `os.path.join()` or `Path() / "file"` - never hardcode slashes
- Check existence before operations: `if Path("file").exists():`
- Use `exist_ok=True` to avoid crashes
- `mkdir()` for single folder, `makedirs()` for nested

## Time
- **Never** use `time.sleep()` blindly - use explicit waits in Selenium
- Use `time.perf_counter()` for accurate performance measurement
- `time.time()` for timestamps, `perf_counter()` for duration

## Requests
- **Always** set `timeout` to prevent hanging
- Use `Session()` for multiple requests to same site
- Check `r.status_code` before using response
- `r.content` for files, `r.json()` for APIs, `r.text` for HTML
- User-Agent header prevents blocking

## Selenium
- **Locator priority**: ID → Name → CSS → XPath
- **Always** use explicit waits (`WebDriverWait`), not `time.sleep()`
- **Always** use `try/finally` with `driver.quit()`
- Use `contains()` for dynamic IDs/classes
- `element_to_be_clickable` before clicking
- `By.XPATH` not `by.xpath` - capitalization matters

---

# QUICK DEBUGGING CHECKLIST

## Pandas Issues
- [ ] Check `df.dtypes` - wrong data type?
- [ ] Check `df.isna().sum()` - missing values?
- [ ] Use `df.head()` and `df.shape` to inspect
- [ ] Parentheses around each condition in filtering
- [ ] Use `&` for AND, `|` for OR (not `and`/`or`)

## Selenium Issues
- [ ] Element not found? → Check locator, use `wait`
- [ ] Click fails? → Check if clickable, scroll into view
- [ ] Stale element? → Re-find element after page change
- [ ] Random failures? → Add explicit waits
- [ ] Import `By` from selenium.webdriver.common.by
- [ ] Capitalization: `WebDriverWait`, `By.ID`, `contains()`

## Requests Issues  
- [ ] Check `r.status_code` - 200 = success
- [ ] Blocked? → Add `User-Agent` header
- [ ] Need login? → Use `Session()`
- [ ] Timeout? → Increase `timeout` parameter
- [ ] `.json()` not `.jason()` - method spelling
- [ ] POST not post in requests

## Common Syntax Errors
- [ ] `pd.concat()` not `df.concat()`
- [ ] `driver.find_element()` not `webdriver.find_element()`
- [ ] Method calls need `()` - `.click()` not `.click`
- [ ] String URLs need quotes: `"https://..."` not `https://...`
- [ ] XPath/CSS selectors need quotes

---

# PRODUCTION-LEVEL PATTERNS

## Data Pipeline Template
```python
import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPipeline:
    def __init__(self, input_path, output_path):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
    
    def extract(self):
        """Load data"""
        logger.info(f"Loading data from {self.input_path}")
        return pd.read_csv(self.input_path)
    
    def transform(self, df):
        """Clean and transform"""
        logger.info("Transforming data")
        # Remove missing
        df = df.dropna()
        # Remove duplicates
        df = df.drop_duplicates()
        # Clean text
        df["city"] = df["city"].str.strip().str.lower()
        # Create features
        df["revenue"] = df["price"] * df["quantity"]
        return df
    
    def load(self, df, filename):
        """Save output"""
        output_file = self.output_path / filename
        logger.info(f"Saving to {output_file}")
        df.to_excel(output_file, index=False)
    
    def run(self):
        """Execute pipeline"""
        try:
            df = self.extract()
            df = self.transform(df)
            self.load(df, "clean_data.xlsx")
            logger.info("Pipeline completed successfully")
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise

# Usage
pipeline = DataPipeline("raw_data.csv", "outputs")
pipeline.run()
```

## Retry Logic with Exponential Backoff
```python
import time
import requests
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    delay = base_delay * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed: {e}")
                    print(f"Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_with_backoff(max_retries=3, base_delay=1)
def fetch_data(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()
```

## Rate Limiter
```python
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current = time.time()
            # Remove old calls
            while self.calls and current - self.calls[0] > self.period:
                self.calls.popleft()
            
            # Check limit
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (current - self.calls[0])
                print(f"Rate limit reached. Waiting {sleep_time:.1f}s")
                time.sleep(sleep_time)
                self.calls.clear()
            
            self.calls.append(current)
            return func(*args, **kwargs)
        return wrapper

@RateLimiter(max_calls=10, period=60)  # 10 calls per minute
def api_call(endpoint):
    return requests.get(endpoint)
```

---

**END OF REVISION NOTES**

*These notes cover 95% of real-world automation scenarios*

**Master these patterns → Build professional automation systems** 🚀