# ⏰ TIME LIBRARY MASTER NOTES — COMPLETE GUIDE

**Author:** Prerak  
**Purpose:** Master Python's time module for time-based operations and automation  
**Version:** Complete Edition with Real-World Examples

---

## 📋 TABLE OF CONTENTS

1. [Introduction to Time Module](#introduction-to-time-module)
2. [Getting Current Time](#getting-current-time)
3. [Sleeping and Delays](#sleeping-and-delays)
4. [Time Measurement and Benchmarking](#time-measurement-and-benchmarking)
5. [Working with Timestamps](#working-with-timestamps)
6. [Time Formatting and Parsing](#time-formatting-and-parsing)
7. [Time Zones](#time-zones)
8. [Time Arithmetic](#time-arithmetic)
9. [Performance Monitoring](#performance-monitoring)
10. [Real-World Applications](#real-world-applications)
11. [Common Patterns](#common-patterns)
12. [Best Practices](#best-practices)

---

# INTRODUCTION TO TIME MODULE

## What is the Time Module?

**Definition:**  
The `time` module provides time-related functions for Python. It handles time measurement, delays, time formatting, and system time operations.

**Mental Model:**  
> Time module = Your program's stopwatch, alarm clock, and calendar

**Why Time Module Matters:**
- Add delays in automation scripts
- Measure code performance
- Schedule tasks
- Create timestamps for logging
- Build rate limiting
- Timeout mechanisms

---

## Importing the Time Module

```python
import time

# Check available functions
print(dir(time))

# Get help
help(time.sleep)
```

---

## Time Concepts to Understand

### 1) Unix Timestamp (Epoch Time)

**Definition:**  
Seconds since January 1, 1970, 00:00:00 UTC (the "epoch")

```python
import time

# Get current timestamp
timestamp = time.time()
print(timestamp)

# Output: 1706745600.123456
```

**Why This Matters:**
- Universal time representation
- Easy to calculate time differences
- Database-friendly format
- No timezone confusion

---

### 2) Struct Time

**Definition:**  
A tuple-like object containing time components (year, month, day, etc.)

```python
# Get current time as struct
current = time.localtime()
print(current)

# Output:
# time.struct_time(tm_year=2024, tm_mon=2, tm_mday=1, 
#                  tm_hour=14, tm_min=30, tm_sec=45, 
#                  tm_wday=3, tm_yday=32, tm_isdst=0)
```

**Components:**
- `tm_year` → Year (e.g., 2024)
- `tm_mon` → Month (1-12)
- `tm_mday` → Day of month (1-31)
- `tm_hour` → Hour (0-23)
- `tm_min` → Minute (0-59)
- `tm_sec` → Second (0-61)
- `tm_wday` → Day of week (0=Monday, 6=Sunday)
- `tm_yday` → Day of year (1-366)
- `tm_isdst` → Daylight saving time flag

---

### 3) Time vs DateTime vs Calendar

| Module | Best For |
|--------|----------|
| **time** | Basic delays, timestamps, simple timing |
| **datetime** | Date arithmetic, complex time operations |
| **calendar** | Calendar-related operations |

**Quick Rule:**
- Use `time` for: delays, performance measurement, timestamps
- Use `datetime` for: date manipulation, scheduling
- Use `calendar` for: calendar display, date validation

---

# GETTING CURRENT TIME

## 1) Current Timestamp

### Get Unix Timestamp

```python
import time

# Current time as timestamp (float)
timestamp = time.time()
print(timestamp)

# Output: 1706745678.901234

# Store for later comparison
start_time = time.time()
```

**Use Cases:**
- Measure elapsed time
- Create unique identifiers
- Database timestamps
- Cache expiration

---

## 2) Current Local Time

### Get Local Time as Struct

```python
# Get current local time
local_time = time.localtime()
print(local_time)

# Access components
print(f"Year: {local_time.tm_year}")
print(f"Month: {local_time.tm_mon}")
print(f"Day: {local_time.tm_mday}")
print(f"Hour: {local_time.tm_hour}")
print(f"Minute: {local_time.tm_min}")
print(f"Second: {local_time.tm_sec}")

# Output:
# Year: 2024
# Month: 2
# Day: 1
# Hour: 14
# Minute: 30
# Second: 45
```

---

## 3) Current UTC Time

### Get UTC Time

```python
# Get current UTC time
utc_time = time.gmtime()
print(utc_time)

# Compare local vs UTC
local = time.localtime()
utc = time.gmtime()

print(f"Local hour: {local.tm_hour}")
print(f"UTC hour: {utc.tm_hour}")
print(f"Difference: {local.tm_hour - utc.tm_hour} hours")
```

**When to Use UTC:**
- Server applications
- International applications
- Logging systems
- Database storage

---

## 4) Formatted Current Time

### Get Readable Time String

```python
# Current time as readable string
current = time.ctime()
print(current)

# Output: Thu Feb  1 14:30:45 2024

# Custom formatted time
formatted = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Output: 2024-02-01 14:30:45
```

---

# SLEEPING AND DELAYS

## 1) Basic Sleep

### Simple Delay

```python
import time

print("Starting...")
time.sleep(2)  # Sleep for 2 seconds
print("2 seconds later!")

# Output:
# Starting...
# (2 second pause)
# 2 seconds later!
```

**Use Cases:**
- Wait for web pages to load
- Rate limiting API calls
- Creating pauses in automation
- Polling intervals

---

## 2) Fractional Seconds

### Sleep with Decimals

```python
# Sleep for half a second
time.sleep(0.5)

# Sleep for 100 milliseconds
time.sleep(0.1)

# Sleep for 1.5 seconds
time.sleep(1.5)

# Very short sleep (10ms)
time.sleep(0.01)
```

---

## 3) Dynamic Sleep

### Calculate Sleep Duration

```python
import time

# Sleep until specific time of day
target_hour = 9
target_minute = 0

while True:
    current = time.localtime()
    
    if current.tm_hour == target_hour and current.tm_min == target_minute:
        print("Time to start!")
        break
    else:
        time.sleep(60)  # Check every minute
```

---

## 4) Sleep with Progress

### Visual Sleep Indicator

```python
import time

def sleep_with_progress(seconds):
    """Sleep with countdown"""
    for i in range(seconds, 0, -1):
        print(f"Waiting: {i} seconds...", end='\r')
        time.sleep(1)
    print("Done!                    ")

# Usage
sleep_with_progress(5)
```

---

## 5) Interruptible Sleep

### Sleep with Keyboard Interrupt

```python
import time

def safe_sleep(seconds):
    """Sleep that can be interrupted with Ctrl+C"""
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        print("\nSleep interrupted!")

# Usage
print("Sleeping for 10 seconds (Ctrl+C to interrupt)")
safe_sleep(10)
```

---

## 6) Rate Limiting

### Delay Between Operations

```python
import time

def process_items(items, delay=1):
    """Process items with delay between each"""
    for i, item in enumerate(items, 1):
        print(f"Processing {i}/{len(items)}: {item}")
        # Do work here
        
        # Don't delay after last item
        if i < len(items):
            time.sleep(delay)

# Usage
urls = ["url1.com", "url2.com", "url3.com"]
process_items(urls, delay=2)  # 2 second delay between requests
```

---

# TIME MEASUREMENT AND BENCHMARKING

## 1) Simple Timing

### Measure Execution Time

```python
import time

# Start timer
start = time.time()

# Code to measure
total = 0
for i in range(1000000):
    total += i

# End timer
end = time.time()

# Calculate duration
duration = end - start
print(f"Execution time: {duration:.4f} seconds")

# Output: Execution time: 0.0523 seconds
```

---

## 2) Function Timer Decorator

### Automatic Function Timing

```python
import time
from functools import wraps

def timer(func):
    """Decorator to time function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        duration = end - start
        print(f"{func.__name__} took {duration:.4f} seconds")
        return result
    
    return wrapper

# Usage
@timer
def slow_function():
    time.sleep(2)
    return "Done"

@timer
def calculate_sum(n):
    return sum(range(n))

# Test
slow_function()
calculate_sum(1000000)

# Output:
# slow_function took 2.0012 seconds
# calculate_sum took 0.0234 seconds
```

---

## 3) High-Resolution Timing

### Precise Performance Measurement

```python
import time

# perf_counter() - most precise for performance measurement
start = time.perf_counter()

# Code to benchmark
result = sum(range(1000000))

end = time.perf_counter()

duration = end - start
print(f"Duration: {duration:.6f} seconds")

# Output: Duration: 0.023456 seconds
```

**Time Functions for Measurement:**

| Function | Purpose | Resolution |
|----------|---------|------------|
| `time.time()` | Wall clock time | ~1 microsecond |
| `time.perf_counter()` | Performance counter | High precision |
| `time.process_time()` | CPU time only | High precision |
| `time.monotonic()` | Never goes backward | High precision |

### When to Use Each:

```python
import time

# Use time() for general purposes
start = time.time()
time.sleep(1)
print(f"Wall time: {time.time() - start:.4f}s")

# Use perf_counter() for benchmarks
start = time.perf_counter()
result = sum(range(1000000))
print(f"Performance: {time.perf_counter() - start:.6f}s")

# Use process_time() for CPU time only (excludes sleep)
start = time.process_time()
time.sleep(1)
result = sum(range(1000))
print(f"CPU time: {time.process_time() - start:.6f}s")

# Use monotonic() when you need guaranteed forward progress
start = time.monotonic()
time.sleep(1)
print(f"Monotonic: {time.monotonic() - start:.4f}s")
```

---

## 4) Compare Algorithm Performance

### Benchmark Multiple Approaches

```python
import time

def benchmark(func, *args, iterations=1000):
    """Run function multiple times and get average time"""
    start = time.perf_counter()
    
    for _ in range(iterations):
        func(*args)
    
    end = time.perf_counter()
    avg_time = (end - start) / iterations
    
    return avg_time

# Test different approaches
def approach1(n):
    return [i**2 for i in range(n)]

def approach2(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# Benchmark
n = 1000
time1 = benchmark(approach1, n, iterations=1000)
time2 = benchmark(approach2, n, iterations=1000)

print(f"List comprehension: {time1*1000:.3f} ms")
print(f"Loop with append: {time2*1000:.3f} ms")
print(f"Speedup: {time2/time1:.2f}x")
```

---

## 5) Timeout Implementation

### Execute with Time Limit

```python
import time

def run_with_timeout(func, timeout, *args, **kwargs):
    """Run function with timeout (simple version)"""
    start = time.time()
    
    while True:
        if time.time() - start > timeout:
            raise TimeoutError(f"Function exceeded {timeout} seconds")
        
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            raise e

# Better approach using threading
import threading

def timeout_wrapper(timeout):
    """Decorator for function timeout"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [None]
            exception = [None]
            
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e
            
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(timeout)
            
            if thread.is_alive():
                raise TimeoutError(f"Function exceeded {timeout} seconds")
            
            if exception[0]:
                raise exception[0]
            
            return result[0]
        
        return wrapper
    return decorator

# Usage
@timeout_wrapper(timeout=2)
def slow_operation():
    time.sleep(5)  # This will timeout
    return "Done"

try:
    slow_operation()
except TimeoutError as e:
    print(f"Timeout: {e}")
```

---

# WORKING WITH TIMESTAMPS

## 1) Convert Timestamp to Readable Time

### Timestamp → Struct Time

```python
import time

# Get timestamp
timestamp = time.time()
print(f"Timestamp: {timestamp}")

# Convert to local time
local = time.localtime(timestamp)
print(f"Local: {local}")

# Convert to UTC
utc = time.gmtime(timestamp)
print(f"UTC: {utc}")

# Convert specific timestamp
old_timestamp = 1609459200  # Jan 1, 2021
old_time = time.localtime(old_timestamp)
print(f"Year: {old_time.tm_year}, Month: {old_time.tm_mon}")
```

---

## 2) Convert Struct Time to Timestamp

### Struct Time → Timestamp

```python
import time

# Create a struct time
struct_time = time.struct_time((
    2024,  # tm_year
    2,     # tm_mon
    1,     # tm_mday
    12,    # tm_hour
    0,     # tm_min
    0,     # tm_sec
    3,     # tm_wday (0=Monday)
    32,    # tm_yday
    0      # tm_isdst
))

# Convert to timestamp
timestamp = time.mktime(struct_time)
print(f"Timestamp: {timestamp}")

# Or use current time
current = time.localtime()
current_timestamp = time.mktime(current)
print(f"Current timestamp: {current_timestamp}")
```

---

## 3) Calculate Time Differences

### Compare Timestamps

```python
import time

# Create two timestamps
start = time.time()
time.sleep(2.5)
end = time.time()

# Calculate difference
difference = end - start
print(f"Elapsed: {difference:.2f} seconds")

# Days between two dates
timestamp1 = 1704067200  # Jan 1, 2024
timestamp2 = 1735689600  # Jan 1, 2025

difference_seconds = timestamp2 - timestamp1
difference_days = difference_seconds / (24 * 60 * 60)

print(f"Days difference: {difference_days:.0f} days")
```

---

## 4) Age Calculation

### Calculate Age from Timestamp

```python
import time

def calculate_age(birth_timestamp):
    """Calculate age in years"""
    current = time.time()
    age_seconds = current - birth_timestamp
    age_years = age_seconds / (365.25 * 24 * 60 * 60)
    return age_years

# Birth date: Jan 1, 2000
birth = time.mktime(time.strptime("2000-01-01", "%Y-%m-%d"))
age = calculate_age(birth)
print(f"Age: {age:.1f} years")
```

---

# TIME FORMATTING AND PARSING

## 1) Format Time to String

### Using strftime()

```python
import time

# Get current time
now = time.localtime()

# Various formats
print(time.strftime("%Y-%m-%d", now))           # 2024-02-01
print(time.strftime("%H:%M:%S", now))           # 14:30:45
print(time.strftime("%Y-%m-%d %H:%M:%S", now))  # 2024-02-01 14:30:45
print(time.strftime("%B %d, %Y", now))          # February 01, 2024
print(time.strftime("%A, %B %d", now))          # Thursday, February 01
print(time.strftime("%I:%M %p", now))           # 02:30 PM
```

---

## 2) Format Codes Reference

### Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2024 |
| `%y` | 2-digit year | 24 |
| `%m` | Month (01-12) | 02 |
| `%d` | Day (01-31) | 01 |
| `%H` | Hour 24h (00-23) | 14 |
| `%I` | Hour 12h (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | PM |
| `%A` | Full weekday | Thursday |
| `%a` | Short weekday | Thu |
| `%B` | Full month | February |
| `%b` | Short month | Feb |
| `%j` | Day of year | 032 |
| `%U` | Week number | 05 |
| `%w` | Weekday (0-6) | 4 |
| `%Z` | Timezone | UTC |

---

## 3) Common Format Patterns

### Ready-to-Use Formats

```python
import time

now = time.localtime()

# Date formats
print(time.strftime("%Y-%m-%d", now))        # 2024-02-01 (ISO)
print(time.strftime("%m/%d/%Y", now))        # 02/01/2024 (US)
print(time.strftime("%d/%m/%Y", now))        # 01/02/2024 (EU)
print(time.strftime("%d-%b-%Y", now))        # 01-Feb-2024

# Time formats
print(time.strftime("%H:%M:%S", now))        # 14:30:45 (24h)
print(time.strftime("%I:%M:%S %p", now))     # 02:30:45 PM (12h)
print(time.strftime("%H:%M", now))           # 14:30

# Combined formats
print(time.strftime("%Y-%m-%d %H:%M:%S", now))              # 2024-02-01 14:30:45
print(time.strftime("%A, %B %d, %Y at %I:%M %p", now))     # Thursday, February 01, 2024 at 02:30 PM
print(time.strftime("%c", now))                             # Thu Feb  1 14:30:45 2024

# Filename-safe timestamp
print(time.strftime("%Y%m%d_%H%M%S", now))   # 20240201_143045
```

---

## 4) Parse String to Time

### Using strptime()

```python
import time

# Parse date string
date_string = "2024-02-01"
parsed = time.strptime(date_string, "%Y-%m-%d")
print(parsed)

# Parse datetime string
datetime_string = "2024-02-01 14:30:45"
parsed = time.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
print(f"Year: {parsed.tm_year}")
print(f"Month: {parsed.tm_mon}")
print(f"Day: {parsed.tm_mday}")

# Convert to timestamp
timestamp = time.mktime(parsed)
print(f"Timestamp: {timestamp}")
```

---

## 5) Common Parsing Patterns

### Parse Various Formats

```python
import time

# Different date formats
formats = [
    ("2024-02-01", "%Y-%m-%d"),
    ("02/01/2024", "%m/%d/%Y"),
    ("01-Feb-2024", "%d-%b-%Y"),
    ("February 1, 2024", "%B %d, %Y"),
    ("Thu, 01 Feb 2024", "%a, %d %b %Y"),
]

for date_str, format_str in formats:
    parsed = time.strptime(date_str, format_str)
    print(f"{date_str} → {parsed.tm_year}-{parsed.tm_mon:02d}-{parsed.tm_mday:02d}")
```

---

# TIME ZONES

## 1) Timezone Awareness

### Understanding Timezones

```python
import time

# Get timezone info
print(f"Timezone: {time.tzname}")
print(f"UTC offset: {time.timezone / 3600} hours")
print(f"Daylight saving: {time.daylight}")

# Output (example):
# Timezone: ('EST', 'EDT')
# UTC offset: 5.0 hours
# Daylight saving: 1
```

---

## 2) Convert Between Timezones

### Local ↔ UTC

```python
import time

# Current local time
local = time.localtime()
print(f"Local: {time.strftime('%Y-%m-%d %H:%M:%S', local)}")

# Same time in UTC
utc = time.gmtime()
print(f"UTC: {time.strftime('%Y-%m-%d %H:%M:%S', utc)}")

# Convert timestamp to both
timestamp = time.time()
local_from_ts = time.localtime(timestamp)
utc_from_ts = time.gmtime(timestamp)

print(f"Local: {time.strftime('%H:%M:%S', local_from_ts)}")
print(f"UTC: {time.strftime('%H:%M:%S', utc_from_ts)}")
```

---

## 3) Timezone-Safe Operations

### Best Practices

```python
import time

def get_utc_timestamp():
    """Always store times in UTC"""
    return time.time()

def format_local_time(timestamp):
    """Display in user's local time"""
    local = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", local)

def format_utc_time(timestamp):
    """Display in UTC"""
    utc = time.gmtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S UTC", utc)

# Usage
ts = get_utc_timestamp()
print(f"Stored: {ts}")
print(f"Display (local): {format_local_time(ts)}")
print(f"Display (UTC): {format_utc_time(ts)}")
```

---

# TIME ARITHMETIC

## 1) Add/Subtract Time

### Calculate Future/Past Times

```python
import time

# Current time
current = time.time()

# Add time
one_hour_later = current + (60 * 60)           # +1 hour
one_day_later = current + (24 * 60 * 60)       # +1 day
one_week_later = current + (7 * 24 * 60 * 60)  # +1 week

# Subtract time
one_hour_ago = current - (60 * 60)
one_day_ago = current - (24 * 60 * 60)

# Display
print(f"Now: {time.ctime(current)}")
print(f"1 hour later: {time.ctime(one_hour_later)}")
print(f"1 day later: {time.ctime(one_day_later)}")
print(f"1 hour ago: {time.ctime(one_hour_ago)}")
```

---

## 2) Time Constants

### Useful Constants

```python
# Define constants for clarity
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY

# Usage
import time

current = time.time()

# Much more readable
tomorrow = current + DAY
next_week = current + WEEK
three_hours_later = current + (3 * HOUR)

print(f"Tomorrow: {time.ctime(tomorrow)}")
print(f"Next week: {time.ctime(next_week)}")
```

---

## 3) Calculate Duration

### Human-Readable Duration

```python
import time

def format_duration(seconds):
    """Convert seconds to human-readable format"""
    days = int(seconds // (24 * 60 * 60))
    seconds %= (24 * 60 * 60)
    
    hours = int(seconds // (60 * 60))
    seconds %= (60 * 60)
    
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0 or not parts:
        parts.append(f"{seconds}s")
    
    return " ".join(parts)

# Usage
duration = 90125  # seconds
print(format_duration(duration))  # 1d 1h 2m 5s

# Measure elapsed time
start = time.time()
time.sleep(3.5)
elapsed = time.time() - start
print(f"Elapsed: {format_duration(elapsed)}")  # 3s
```

---

# PERFORMANCE MONITORING

## 1) Function Profiling

### Detailed Performance Analysis

```python
import time

class Timer:
    """Context manager for timing code blocks"""
    
    def __init__(self, name="Operation"):
        self.name = name
        self.start = None
        self.end = None
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.end = time.perf_counter()
        duration = self.end - self.start
        print(f"{self.name} took {duration:.4f} seconds")

# Usage
with Timer("Data processing"):
    # Simulate work
    result = sum(range(1000000))

with Timer("File writing"):
    time.sleep(0.5)

# Output:
# Data processing took 0.0234 seconds
# File writing took 0.5012 seconds
```

---

## 2) Multi-Step Profiling

### Track Multiple Operations

```python
import time

class StepTimer:
    """Track time for multiple steps"""
    
    def __init__(self):
        self.steps = []
        self.start_time = time.perf_counter()
        self.last_step = self.start_time
    
    def step(self, name):
        """Record a step"""
        current = time.perf_counter()
        duration = current - self.last_step
        total = current - self.start_time
        
        self.steps.append({
            'name': name,
            'duration': duration,
            'total': total
        })
        
        self.last_step = current
        print(f"{name}: {duration:.4f}s (total: {total:.4f}s)")
    
    def summary(self):
        """Print summary"""
        print("\n=== Summary ===")
        for step in self.steps:
            percent = (step['duration'] / step['total']) * 100
            print(f"{step['name']}: {step['duration']:.4f}s ({percent:.1f}%)")

# Usage
timer = StepTimer()

time.sleep(0.5)
timer.step("Load data")

time.sleep(0.3)
timer.step("Process data")

time.sleep(0.2)
timer.step("Save results")

timer.summary()
```

---

## 3) Performance Comparison

### Compare Multiple Implementations

```python
import time

def compare_performance(functions, *args, iterations=1000):
    """Compare execution time of multiple functions"""
    results = []
    
    for func in functions:
        start = time.perf_counter()
        
        for _ in range(iterations):
            func(*args)
        
        end = time.perf_counter()
        avg_time = (end - start) / iterations
        
        results.append({
            'name': func.__name__,
            'time': avg_time
        })
    
    # Sort by time
    results.sort(key=lambda x: x['time'])
    
    # Display results
    print(f"\nPerformance comparison ({iterations} iterations):")
    print("-" * 50)
    
    fastest = results[0]['time']
    
    for i, result in enumerate(results, 1):
        slowdown = result['time'] / fastest
        print(f"{i}. {result['name']:<20} {result['time']*1000:.3f}ms  ({slowdown:.2f}x)")

# Example functions
def approach_a(n):
    return [i*i for i in range(n)]

def approach_b(n):
    result = []
    for i in range(n):
        result.append(i*i)
    return result

def approach_c(n):
    return list(map(lambda x: x*x, range(n)))

# Compare
compare_performance([approach_a, approach_b, approach_c], 100)
```

---

# REAL-WORLD APPLICATIONS

## Application 1: Rate Limiter

### API Rate Limiting

```python
import time

class RateLimiter:
    """Limit number of operations per time period"""
    
    def __init__(self, max_calls, period):
        """
        max_calls: Maximum number of calls
        period: Time period in seconds
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = []
    
    def __call__(self, func):
        """Decorator for rate limiting"""
        def wrapper(*args, **kwargs):
            current = time.time()
            
            # Remove old calls
            self.calls = [c for c in self.calls if current - c < self.period]
            
            # Check limit
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (current - self.calls[0])
                print(f"Rate limit reached. Sleeping for {sleep_time:.2f}s")
                time.sleep(sleep_time)
                self.calls = []
            
            # Record this call
            self.calls.append(current)
            
            return func(*args, **kwargs)
        
        return wrapper

# Usage
@RateLimiter(max_calls=5, period=10)  # 5 calls per 10 seconds
def api_call(url):
    print(f"Calling {url} at {time.strftime('%H:%M:%S')}")
    return "Response"

# Test - will rate limit after 5 calls
for i in range(8):
    api_call(f"https://api.example.com/endpoint{i}")
```

---

## Application 2: Retry with Backoff

### Exponential Backoff Retry

```python
import time

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60):
    """Decorator for retry with exponential backoff"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    
                    # Calculate delay (exponential backoff)
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    
                    print(f"Attempt {attempt + 1} failed: {e}")
                    print(f"Retrying in {delay}s...")
                    time.sleep(delay)
        
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=4, base_delay=1, max_delay=30)
def unstable_api_call():
    """Simulates an API that sometimes fails"""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("API temporarily unavailable")
    return "Success!"

# Test
try:
    result = unstable_api_call()
    print(f"Result: {result}")
except Exception as e:
    print(f"All retries failed: {e}")
```

---

## Application 3: Timeout Decorator

### Function Timeout Handler

```python
import time
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds):
    """Decorator to timeout function execution (Unix only)"""
    
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError(f"Function exceeded {seconds} seconds")
        
        def wrapper(*args, **kwargs):
            # Set alarm
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                # Disable alarm
                signal.alarm(0)
            
            return result
        
        return wrapper
    return decorator

# Cross-platform alternative using threading
import threading

def timeout_threading(seconds):
    """Cross-platform timeout decorator"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [None]
            exception = [None]
            
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e
            
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            
            if thread.is_alive():
                raise TimeoutError(f"Function exceeded {seconds} seconds")
            
            if exception[0]:
                raise exception[0]
            
            return result[0]
        
        return wrapper
    return decorator

# Usage
@timeout_threading(3)
def long_running_task():
    print("Starting task...")
    time.sleep(5)  # Will timeout
    return "Completed"

try:
    long_running_task()
except TimeoutError as e:
    print(f"Task timed out: {e}")
```

---

## Application 4: Scheduling Tasks

### Simple Task Scheduler

```python
import time
from datetime import datetime

class Scheduler:
    """Simple task scheduler"""
    
    def __init__(self):
        self.tasks = []
    
    def daily(self, hour, minute, task):
        """Schedule daily task"""
        self.tasks.append({
            'type': 'daily',
            'hour': hour,
            'minute': minute,
            'task': task,
            'last_run': None
        })
    
    def interval(self, seconds, task):
        """Schedule interval task"""
        self.tasks.append({
            'type': 'interval',
            'seconds': seconds,
            'task': task,
            'last_run': None
        })
    
    def run(self):
        """Run scheduler (blocking)"""
        print("Scheduler started. Press Ctrl+C to stop.")
        
        try:
            while True:
                current = time.time()
                current_local = time.localtime(current)
                
                for task_info in self.tasks:
                    should_run = False
                    
                    if task_info['type'] == 'daily':
                        # Check if time matches
                        if (current_local.tm_hour == task_info['hour'] and
                            current_local.tm_min == task_info['minute']):
                            
                            # Check if already run today
                            if task_info['last_run'] is None:
                                should_run = True
                            else:
                                last_run_local = time.localtime(task_info['last_run'])
                                if last_run_local.tm_yday != current_local.tm_yday:
                                    should_run = True
                    
                    elif task_info['type'] == 'interval':
                        # Check if enough time passed
                        if task_info['last_run'] is None:
                            should_run = True
                        elif current - task_info['last_run'] >= task_info['seconds']:
                            should_run = True
                    
                    if should_run:
                        print(f"Running task: {task_info['task'].__name__}")
                        task_info['task']()
                        task_info['last_run'] = current
                
                time.sleep(1)  # Check every second
        
        except KeyboardInterrupt:
            print("\nScheduler stopped.")

# Usage
scheduler = Scheduler()

def morning_task():
    print("Good morning! Running daily backup...")

def check_email():
    print("Checking email...")

# Schedule tasks
scheduler.daily(9, 0, morning_task)           # Every day at 9:00 AM
scheduler.interval(300, check_email)           # Every 5 minutes

# Run (uncomment to test)
# scheduler.run()
```

---

## Application 5: Performance Monitor

### Real-Time Performance Tracker

```python
import time
import threading

class PerformanceMonitor:
    """Monitor performance metrics in real-time"""
    
    def __init__(self, interval=1.0):
        self.interval = interval
        self.operations = []
        self.running = False
        self.thread = None
    
    def record_operation(self, duration):
        """Record an operation duration"""
        self.operations.append({
            'timestamp': time.time(),
            'duration': duration
        })
    
    def get_stats(self, window=60):
        """Get statistics for last N seconds"""
        current = time.time()
        cutoff = current - window
        
        recent = [op for op in self.operations if op['timestamp'] >= cutoff]
        
        if not recent:
            return {
                'count': 0,
                'avg_duration': 0,
                'min_duration': 0,
                'max_duration': 0,
                'ops_per_second': 0
            }
        
        durations = [op['duration'] for op in recent]
        
        return {
            'count': len(recent),
            'avg_duration': sum(durations) / len(durations),
            'min_duration': min(durations),
            'max_duration': max(durations),
            'ops_per_second': len(recent) / window
        }
    
    def start_monitoring(self):
        """Start real-time monitoring"""
        self.running = True
        self.thread = threading.Thread(target=self._monitor)
        self.thread.daemon = True
        self.thread.start()
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.running = False
        if self.thread:
            self.thread.join()
    
    def _monitor(self):
        """Monitor loop"""
        while self.running:
            stats = self.get_stats(window=60)
            
            print(f"\n=== Performance Stats (last 60s) ===")
            print(f"Operations: {stats['count']}")
            print(f"Avg duration: {stats['avg_duration']*1000:.2f}ms")
            print(f"Min/Max: {stats['min_duration']*1000:.2f}ms / {stats['max_duration']*1000:.2f}ms")
            print(f"Ops/sec: {stats['ops_per_second']:.2f}")
            
            time.sleep(self.interval)

# Usage
monitor = PerformanceMonitor(interval=5)
monitor.start_monitoring()

# Simulate operations
import random
for i in range(100):
    start = time.time()
    time.sleep(random.uniform(0.01, 0.1))  # Simulate work
    duration = time.time() - start
    monitor.record_operation(duration)
    time.sleep(0.1)

monitor.stop_monitoring()
```

---

# COMMON PATTERNS

## Pattern 1: Polling Loop

### Wait for Condition

```python
import time

def wait_for_condition(check_func, timeout=30, interval=1):
    """Wait for condition to be true"""
    start = time.time()
    
    while time.time() - start < timeout:
        if check_func():
            return True
        time.sleep(interval)
    
    return False

# Usage
def is_file_ready():
    import os
    return os.path.exists("data.txt")

# Wait for file to appear
if wait_for_condition(is_file_ready, timeout=60):
    print("File is ready!")
else:
    print("Timeout waiting for file")
```

---

## Pattern 2: Progress Indicator

### Show Progress with Timing

```python
import time

def process_with_progress(items):
    """Process items with progress and timing"""
    total = len(items)
    start = time.time()
    
    for i, item in enumerate(items, 1):
        # Process item
        time.sleep(0.1)  # Simulate work
        
        # Calculate progress
        elapsed = time.time() - start
        avg_time = elapsed / i
        remaining = (total - i) * avg_time
        
        # Display progress
        percent = (i / total) * 100
        print(f"Progress: {i}/{total} ({percent:.1f}%) - "
              f"Elapsed: {elapsed:.1f}s - "
              f"Remaining: {remaining:.1f}s", end='\r')
    
    print()  # New line at end

# Usage
items = range(50)
process_with_progress(items)
```

---

## Pattern 3: Debounce

### Prevent Rapid Repeated Calls

```python
import time

class Debounce:
    """Debounce function calls"""
    
    def __init__(self, wait):
        self.wait = wait
        self.last_call = 0
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current = time.time()
            
            if current - self.last_call >= self.wait:
                self.last_call = current
                return func(*args, **kwargs)
            else:
                print(f"Debounced (wait {self.wait}s)")
        
        return wrapper

# Usage
@Debounce(wait=2)
def save_data():
    print(f"Saving data at {time.strftime('%H:%M:%S')}")

# Test - only first and last will execute
for i in range(5):
    save_data()
    time.sleep(0.5)
```

---

## Pattern 4: Cache with TTL

### Time-Based Cache

```python
import time

class TTLCache:
    """Cache with time-to-live"""
    
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.cache = {}
    
    def get(self, key):
        """Get cached value if not expired"""
        if key in self.cache:
            value, timestamp = self.cache[key]
            
            if time.time() - timestamp < self.ttl:
                return value
            else:
                # Expired
                del self.cache[key]
        
        return None
    
    def set(self, key, value):
        """Set cache value with timestamp"""
        self.cache[key] = (value, time.time())
    
    def clear_expired(self):
        """Clear all expired entries"""
        current = time.time()
        expired = [
            key for key, (value, timestamp) in self.cache.items()
            if current - timestamp >= self.ttl
        ]
        
        for key in expired:
            del self.cache[key]

# Usage
cache = TTLCache(ttl=5)  # 5 second TTL

cache.set("user:123", {"name": "Alice"})
print(cache.get("user:123"))  # Returns data

time.sleep(6)
print(cache.get("user:123"))  # Returns None (expired)
```

---

# BEST PRACTICES

## 1) Use Appropriate Timer

### Choose the Right Function

```python
import time

# ✅ For delays and general timing
time.sleep(1)
timestamp = time.time()

# ✅ For performance benchmarks (most precise)
start = time.perf_counter()
# ... code ...
duration = time.perf_counter() - start

# ✅ For CPU time only
start = time.process_time()
# ... code ...
cpu_time = time.process_time() - start

# ✅ For monotonic time (never goes backward)
start = time.monotonic()
# ... code ...
elapsed = time.monotonic() - start
```

---

## 2) Store in UTC

### Timezone Best Practice

```python
import time

# ❌ BAD - Store local time
bad_timestamp = time.mktime(time.localtime())

# ✅ GOOD - Store UTC timestamp
good_timestamp = time.time()

# ✅ GOOD - Convert to local for display only
def display_time(timestamp):
    local = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", local)
```

---

## 3) Handle Sleep Interruptions

### Robust Sleep

```python
import time

def interruptible_sleep(seconds):
    """Sleep that can be interrupted"""
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        print("\nInterrupted!")
        raise

# Or with timeout check
def sleep_until(target_time):
    """Sleep until specific timestamp"""
    while True:
        now = time.time()
        if now >= target_time:
            break
        
        remaining = target_time - now
        try:
            time.sleep(min(remaining, 1))  # Sleep max 1s at a time
        except KeyboardInterrupt:
            print("\nInterrupted!")
            break
```

---

## 4) Use Context Managers for Timing

### Clean Timing Code

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name="Operation"):
    """Context manager for timing"""
    start = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - start
        print(f"{name} took {duration:.4f}s")

# ✅ GOOD - Clean and readable
with timer("Data processing"):
    # Your code here
    time.sleep(0.5)

with timer("File operations"):
    # More code
    time.sleep(0.3)
```

---

## 5) Avoid Busy Waiting

### Efficient Waiting

```python
import time

# ❌ BAD - Busy waiting (wastes CPU)
def bad_wait_for_file():
    import os
    while not os.path.exists("file.txt"):
        pass  # CPU at 100%!

# ✅ GOOD - Sleep between checks
def good_wait_for_file():
    import os
    while not os.path.exists("file.txt"):
        time.sleep(0.1)  # CPU usage minimal
```

---

## 6) Precise Timing for Short Operations

### Measure Quick Code

```python
import time

# ❌ BAD - time.time() not precise enough
start = time.time()
x = sum(range(1000))
duration = time.time() - start  # Might be 0.0

# ✅ GOOD - perf_counter() for precision
start = time.perf_counter()
x = sum(range(1000))
duration = time.perf_counter() - start  # Accurate
```

---

# QUICK REFERENCE CHEAT SHEET

## Essential Time Operations

```python
import time

# Get current time
timestamp = time.time()                    # Unix timestamp
local = time.localtime()                   # Local time struct
utc = time.gmtime()                        # UTC time struct
readable = time.ctime()                    # Human-readable

# Sleep/Delays
time.sleep(1)                              # Sleep 1 second
time.sleep(0.1)                            # Sleep 100ms

# Format time
formatted = time.strftime("%Y-%m-%d %H:%M:%S")

# Parse time
parsed = time.strptime("2024-02-01", "%Y-%m-%d")

# Measure performance
start = time.perf_counter()
# ... code ...
duration = time.perf_counter() - start

# Time calculations
one_day_later = timestamp + (24 * 60 * 60)
one_hour_ago = timestamp - (60 * 60)

# Convert formats
timestamp = time.mktime(local)             # struct → timestamp
local = time.localtime(timestamp)          # timestamp → struct
```

---

# WHAT YOU'VE MASTERED

After completing these notes, you can:

✅ Measure code execution time accurately  
✅ Add delays and pauses in automation  
✅ Work with timestamps and time formats  
✅ Parse and format dates and times  
✅ Handle timezones correctly  
✅ Implement rate limiting  
✅ Create retry mechanisms with backoff  
✅ Build timeout functionality  
✅ Schedule tasks  
✅ Monitor performance  
✅ Create time-based caches  
✅ Build robust time-aware applications  

**You're ready to build production-grade time-aware automation!**

---

# PRACTICE EXERCISES

## Beginner Level

1. Create a countdown timer that displays remaining time
2. Calculate your age in days from birthdate
3. Format current time in different formats
4. Build a simple stopwatch
5. Create a pomodoro timer (25min work, 5min break)

## Intermediate Level

1. Build a rate limiter for API calls
2. Create a retry mechanism with exponential backoff
3. Implement a caching system with TTL
4. Build a task scheduler for daily tasks
5. Create a performance monitoring tool

## Advanced Level

1. Develop a multi-timezone meeting scheduler
2. Build a distributed rate limiter
3. Create a time-series data collector
4. Implement adaptive retry with jitter
5. Build a real-time performance dashboard

---

**End of Time Library Master Notes**

*Master time operations, build reliable automation!* ⏰