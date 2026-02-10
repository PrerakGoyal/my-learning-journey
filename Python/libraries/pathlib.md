# 🛣️ PATHLIB MASTER NOTES — COMPLETE GUIDE

**Author:** Prerak  
**Purpose:** Master Python's pathlib module for modern path operations and cross-platform file handling  
**Learning Approach:** Theory → Examples → Practice → Real-world Applications  
**Version:** Complete Edition with Real-World Examples

---

## 📋 TABLE OF CONTENTS

1. [Introduction to Pathlib](#introduction-to-pathlib)
2. [Creating Path Objects](#creating-path-objects)
3. [Path Properties and Attributes](#path-properties-and-attributes)
4. [Path Operations and Manipulation](#path-operations-and-manipulation)
5. [File and Directory Checks](#file-and-directory-checks)
6. [Working with Files](#working-with-files)
7. [Working with Directories](#working-with-directories)
8. [Globbing and Pattern Matching](#globbing-and-pattern-matching)
9. [Path Methods and Utilities](#path-methods-and-utilities)
10. [Cross-Platform Path Handling](#cross-platform-path-handling)
11. [Pathlib vs os.path](#pathlib-vs-ospath)
12. [Real-World Applications](#real-world-applications)
13. [Best Practices](#best-practices)

---

# INTRODUCTION TO PATHLIB

## What is Pathlib?

**Definition:**  
`pathlib` is a Python module that provides object-oriented path operations. It represents file system paths as objects instead of strings, making path operations cleaner, safer, and more intuitive.

**Mental Model:**  
> Pathlib = Modern, object-oriented approach to working with files and folders (replaces string-based os.path)

**Why Pathlib Matters:**
- ✅ Object-oriented (cleaner syntax)
- ✅ Cross-platform compatible (Windows, Mac, Linux)
- ✅ Type hints friendly
- ✅ Chainable methods
- ✅ Intuitive and readable
- ✅ Avoids string concatenation pitfalls
- ✅ Modern Python standard (3.4+)

### Pathlib vs os.path

| Aspect | os.path | pathlib |
|--------|---------|---------|
| Type | String operations | Object-oriented |
| Syntax | `os.path.join(a, b)` | `Path(a) / b` |
| Cross-platform | Can be error-prone | Automatic |
| Readability | Less readable | More readable |
| Modern | Older approach | Newer approach |

---

## Importing Pathlib

```python
# Most common import
from pathlib import Path

# Other classes available
from pathlib import Path, PurePath, PureWindowsPath, PurePosixPath
from pathlib import WindowsPath, PosixPath

# For advanced use
from pathlib import Path

# Check available classes
print(dir(Path))
```

---

# CREATING PATH OBJECTS

## 1) Creating Path Objects from Strings

```python
from pathlib import Path

# From string
file_path = Path("C:/Users/Lenovo/data.csv")
folder_path = Path("/home/user/documents")

# Current directory
current = Path(".")

# Home directory
home = Path.home()
print(home)  # /Users/username or C:\Users\username

# Current working directory
cwd = Path.cwd()
print(cwd)
```

### Output:
```
/Users/Lenovo
/Users/Lenovo/Learning
```

---

## 2) Creating Path Objects from Parts

```python
from pathlib import Path

# From separate parts
path1 = Path("C:", "Users", "Lenovo", "data.csv")

# From multiple arguments
path2 = Path("C:/Users") / "Lenovo" / "Learning"

# Building step by step
base = Path("C:/Users")
user = base / "Lenovo"
project = user / "Learning" / "Python"
```

### Output:
```
C:\Users\Lenovo\data.csv
C:\Users\Lenovo\Learning
C:\Users\Lenovo\Learning\Python
```

---

## 3) The `/` Operator (Path Joining)

**Important:**  
The `/` operator is the preferred way to join paths (much cleaner than string concatenation).

```python
from pathlib import Path

# Using /
path1 = Path("home") / "user" / "documents" / "file.txt"

# Equivalent but not recommended
path2 = Path("home/user/documents/file.txt")

# Mixing string and Path
path3 = Path("home") / "user" / "documents"
path4 = path3 / "file.txt"

print(path1)
print(path4)
```

### Output:
```
home/user/documents/file.txt
home/user/documents/file.txt
```

---

## 4) Absolute vs Relative Paths

```python
from pathlib import Path

# Relative path (relative to current directory)
relative = Path("data/file.csv")

# Absolute path (full path from root)
absolute = Path.cwd() / "data/file.csv"

# Resolve to absolute
resolved = relative.resolve()

print(f"Relative: {relative}")
print(f"Absolute: {absolute}")
print(f"Resolved: {resolved}")
```

---

# PATH PROPERTIES AND ATTRIBUTES

## 1) Extracting Path Components

```python
from pathlib import Path

path = Path("/home/user/documents/report.pdf")

# Parts of the path
print(path.parts)
# Output: ('/', 'home', 'user', 'documents', 'report.pdf')

# Drive letter (Windows)
print(path.drive)
# Output: '' (empty on Unix/Mac)

# Root
print(path.anchor)
# Output: '/'

# Parent directory
print(path.parent)
# Output: /home/user/documents

# File name (with extension)
print(path.name)
# Output: report.pdf

# File stem (name without extension)
print(path.stem)
# Output: report

# File extension/suffix
print(path.suffix)
# Output: .pdf

# All suffixes (for multi-part extensions)
print(path.suffixes)
# Output: ['.tar', '.gz'] for file.tar.gz
```

---

## 2) Parent Directories

```python
from pathlib import Path

path = Path("/home/user/documents/folder/file.txt")

# Direct parent
print(path.parent)
# Output: /home/user/documents/folder

# Multiple levels up
print(path.parent.parent)
# Output: /home/user/documents

print(path.parent.parent.parent)
# Output: /home/user

# All parents (iterate)
for parent in path.parents:
    print(parent)

# Output:
# /home/user/documents/folder
# /home/user/documents
# /home/user
# /home
# /
```

---

## 3) Path String Representation

```python
from pathlib import Path

path = Path("C:/Users/Lenovo/data.csv")

# As string
path_str = str(path)
print(path_str)
# Output: C:\Users\Lenovo\data.csv (Windows) or C:/Users/Lenovo/data.csv (Unix)

# Forward slashes (all platforms)
path_posix = path.as_posix()
print(path_posix)
# Output: C:/Users/Lenovo/data.csv

# URL representation
path_uri = path.as_uri()
print(path_uri)
# Output: file:///C:/Users/Lenovo/data.csv
```

---

# PATH OPERATIONS AND MANIPULATION

## 1) Joining Paths (The `/` Operator)

```python
from pathlib import Path

base = Path("C:/Users/Lenovo")
subfolder = "Learning/Python"
filename = "script.py"

# Chain operations
full_path = base / subfolder / filename
print(full_path)
# Output: C:\Users\Lenovo\Learning\Python\script.py

# With string
folder = Path("docs")
result = folder / "subdir" / "file.txt"
print(result)
```

---

## 2) Path Normalization

```python
from pathlib import Path

# Messy path
path = Path("./data/../scripts/./main.py")

# Resolve to absolute and clean
cleaned = path.resolve()
print(cleaned)
# Output: /absolute/path/to/scripts/main.py

# Relative to current directory
relative = Path(".") / "docs" / ".." / "data"
print(relative)
# Output: docs/../data

# Cleaned relative
print(relative.resolve())
# Output: /absolute/path/to/data
```

---

## 3) Replacing Path Components

```python
from pathlib import Path

path = Path("/home/user/documents/report.pdf")

# Replace filename
new_path = path.with_name("summary.pdf")
print(new_path)
# Output: /home/user/documents/summary.pdf

# Replace stem (name without extension)
new_path = path.with_stem("final_report")
print(new_path)
# Output: /home/user/documents/final_report.pdf

# Replace extension
new_path = path.with_suffix(".docx")
print(new_path)
# Output: /home/user/documents/report.docx

# Replace multiple
new_path = path.with_name("backup.json")
print(new_path)
# Output: /home/user/documents/backup.json
```

---

# FILE AND DIRECTORY CHECKS

## 1) Checking Path Type

```python
from pathlib import Path

path_file = Path("data.csv")
path_dir = Path("documents")
path_link = Path("shortcut")

# File check
if path_file.is_file():
    print("It's a file")

# Directory check
if path_dir.is_dir():
    print("It's a directory")

# Symbolic link check
if path_link.is_symlink():
    print("It's a symbolic link")

# Exists check
if path_file.exists():
    print("Path exists")

# Block device
if path.is_block_device():
    print("Block device")

# Character device
if path.is_char_device():
    print("Character device")

# Socket
if path.is_socket():
    print("Socket")

# FIFO (Named pipe)
if path.is_fifo():
    print("FIFO pipe")
```

---

## 2) Path Existence and Validation

```python
from pathlib import Path

file_path = Path("data.csv")

# Simple existence check
if file_path.exists():
    print("File or directory exists")
else:
    print("Path doesn't exist")

# Type-specific checks
if file_path.is_file():
    print("It's definitely a file")
elif file_path.is_dir():
    print("It's definitely a directory")
else:
    print("It's something else or doesn't exist")
```

---

## 3) File Properties

```python
from pathlib import Path
import os

path = Path("documents/report.pdf")

# File size in bytes
size = path.stat().st_size
print(f"Size: {size} bytes")

# Modification time
mtime = path.stat().st_mtime
print(f"Modified: {mtime}")

# Access time
atime = path.stat().st_atime
print(f"Accessed: {atime}")

# Creation time (Windows)
ctime = path.stat().st_ctime
print(f"Created: {ctime}")

# File permissions
mode = path.stat().st_mode
print(f"Permissions: {oct(mode)}")

# Is readable
if os.access(path, os.R_OK):
    print("Readable")

# Is writable
if os.access(path, os.W_OK):
    print("Writable")

# Is executable
if os.access(path, os.X_OK):
    print("Executable")
```

---

# WORKING WITH FILES

## 1) Reading Files

```python
from pathlib import Path

file_path = Path("data.txt")

# Read entire file as string
content = file_path.read_text()
print(content)

# Read with specific encoding
content = file_path.read_text(encoding='utf-8')

# Read as bytes
binary_content = file_path.read_bytes()
print(binary_content)

# Read line by line
lines = file_path.read_text().split('\n')
for line in lines:
    print(line)
```

---

## 2) Writing Files

```python
from pathlib import Path

file_path = Path("output.txt")

# Write text (overwrites if exists)
file_path.write_text("Hello, World!")

# Write with encoding
file_path.write_text("Hello 世界", encoding='utf-8')

# Append text (read → modify → write)
content = file_path.read_text()
file_path.write_text(content + "\nNew line")

# Write bytes
file_path.write_bytes(b"Binary data")
```

---

## 3) Creating and Deleting Files

```python
from pathlib import Path

file_path = Path("new_file.txt")

# Create an empty file
file_path.touch()

# Create file with specific modification time
from time import time
file_path.touch(exist_ok=True)

# Check if exists before creating
if not file_path.exists():
    file_path.write_text("")

# Delete a file
if file_path.exists():
    file_path.unlink()

# Delete with error handling
try:
    file_path.unlink()
except FileNotFoundError:
    print("File doesn't exist")
```

---

# WORKING WITH DIRECTORIES

## 1) Creating Directories

```python
from pathlib import Path

# Create single directory
dir_path = Path("new_folder")
dir_path.mkdir()

# Create parent directories too
nested = Path("a/b/c/d")
nested.mkdir(parents=True, exist_ok=True)

# Create with error handling
try:
    nested.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Directory already exists")
```

---

## 2) Listing Directory Contents

```python
from pathlib import Path

folder = Path("documents")

# List all items
for item in folder.iterdir():
    print(item)

# Convert to list
items = list(folder.iterdir())

# List only files
files = [f for f in folder.iterdir() if f.is_file()]

# List only directories
dirs = [d for d in folder.iterdir() if d.is_dir()]

# List with sorting
sorted_items = sorted(folder.iterdir())

# List with file size
for item in folder.iterdir():
    size = item.stat().st_size if item.is_file() else "DIR"
    print(f"{item.name}: {size}")
```

---

## 3) Deleting Directories

```python
from pathlib import Path
import shutil

dir_path = Path("empty_folder")

# Delete empty directory
dir_path.rmdir()

# Delete non-empty directory (all contents)
shutil.rmtree(dir_path)

# Safe deletion with error handling
if dir_path.exists():
    if dir_path.is_dir():
        shutil.rmtree(dir_path)
    else:
        dir_path.unlink()
```

---

# GLOBBING AND PATTERN MATCHING

## 1) Basic Globbing

```python
from pathlib import Path

folder = Path("documents")

# All Python files in folder
py_files = folder.glob("*.py")
for file in py_files:
    print(file)

# Get all matches as list
all_py = list(folder.glob("*.py"))

# Specific pattern
csv_files = list(folder.glob("*.csv"))

# Pattern matching
txt_files = list(folder.glob("*.txt"))

# Multiple types
all_data = list(folder.glob("*.*"))
```

---

## 2) Recursive Globbing

```python
from pathlib import Path

folder = Path("project")

# All Python files recursively
all_py = list(folder.glob("**/*.py"))

# All files recursively
all_files = list(folder.glob("**/*"))

# Only files (not directories)
only_files = [f for f in folder.glob("**/*") if f.is_file()]

# All CSV files at any depth
data_files = list(folder.glob("**/data/*.csv"))
```

---

## 3) Advanced Pattern Matching

```python
from pathlib import Path

folder = Path(".")

# Match files starting with test
test_files = list(folder.glob("test_*.py"))

# Match numbered files
num_files = list(folder.glob("file_[0-9]*.txt"))

# Match any character
any_char = list(folder.glob("?.txt"))

# Character ranges
files = list(folder.glob("[a-c]*.txt"))

# Multiple extensions
specific = list(folder.glob("*.{py,txt,csv}"))  # Note: requires rglob for recursion

# Better for complex patterns
import fnmatch
all_items = folder.iterdir()
matched = [x for x in all_items if fnmatch.fnmatch(x.name, "test_*.py")]
```

---

# PATH METHODS AND UTILITIES

## 1) Path Comparison

```python
from pathlib import Path

path1 = Path("documents/file.txt")
path2 = Path("documents/file.txt")
path3 = Path("file.txt")

# Equality
if path1 == path2:
    print("Same path")

# Resolve for comparison
resolved1 = path1.resolve()
resolved2 = path3.resolve()
if resolved1 == resolved2:
    print("Same absolute path")

# Check if path is relative to another
try:
    relative = path1.relative_to(Path("documents"))
    print(relative)  # Output: file.txt
except ValueError:
    print("Path is not relative")

# Check if path is inside another
if Path("documents/file.txt").relative_to(Path("documents")):
    print("File is inside documents folder")
```

---

## 2) Path Relativity

```python
from pathlib import Path

# Make path relative to another
path = Path("/home/user/documents/file.txt")
base = Path("/home/user")

relative = path.relative_to(base)
print(relative)
# Output: documents/file.txt

# Relative from current directory
cwd = Path.cwd()
relative = path.resolve().relative_to(cwd)
print(relative)
```

---

## 3) Finding Common Path

```python
from pathlib import Path

path1 = Path("/home/user/documents/file1.txt")
path2 = Path("/home/user/downloads/file2.txt")

# Common ancestor (manual)
for p1 in path1.parents:
    if p2.relative_to(p1) is not None:
        print(f"Common: {p1}")
        break

# Or simpler
anchor = path1.parents[-1]  # Root
while anchor != path1 and anchor != path2:
    try:
        path1.relative_to(anchor)
        path2.relative_to(anchor)
        break
    except ValueError:
        anchor = anchor.parent
```

---

# CROSS-PLATFORM PATH HANDLING

## 1) Automatic Platform Detection

```python
from pathlib import Path

# Path automatically uses correct separator
windows_path = Path("C:", "Users", "Lenovo", "file.txt")

unix_path = Path("/", "home", "user", "file.txt")

# Correct separator used automatically
print(windows_path)  # C:\Users\Lenovo\file.txt (on Windows)
print(unix_path)    # /home/user/file.txt (on Unix)

# The / operator works everywhere
universal = Path("home") / "user" / "files" / "data.csv"
```

---

## 2) Platform-Specific Paths

```python
from pathlib import Path, PureWindowsPath, PurePosixPath

# Windows format
win_path = PureWindowsPath("C:/Users/file.txt")
print(win_path)
# Output: C:\Users\file.txt

# POSIX (Unix/Mac) format
posix_path = PurePosixPath("/home/user/file.txt")
print(posix_path)
# Output: /home/user/file.txt

# Use conditional
import platform
if platform.system() == "Windows":
    data_path = Path("C:/Data")
else:
    data_path = Path("/home/user/data")
```

---

## 3) Cross-Platform Best Practices

```python
from pathlib import Path

# ✅ Good: Use / operator
config_file = Path.home() / ".config" / "myapp" / "config.json"

# ✅ Good: Use Path constructor
data_dir = Path("data") / "csv_files"

# ❌ Avoid: String concatenation
# bad_path = "data" + "/" + "file.csv"  # Platform-specific issues

# ❌ Avoid: os.path.join
import os
# bad_path = os.path.join("data", "file.csv")  # Old style

print(config_file)
print(data_dir)
```

---

# PATHLIB VS OS.PATH

## Feature Comparison

| Task | os.path | pathlib |
|------|---------|---------|
| Join paths | `os.path.join(a, b)` | `Path(a) / b` |
| Get filename | `os.path.basename(p)` | `Path(p).name` |
| Get directory | `os.path.dirname(p)` | `Path(p).parent` |
| Get extension | `os.path.splitext(p)[1]` | `Path(p).suffix` |
| Absolute path | `os.path.abspath(p)` | `Path(p).resolve()` |
| Check exists | `os.path.exists(p)` | `Path(p).exists()` |
| Check file | `os.path.isfile(p)` | `Path(p).is_file()` |
| Check dir | `os.path.isdir(p)` | `Path(p).is_dir()` |
| List files | `os.listdir(p)` | `Path(p).iterdir()` |
| Create dir | `os.makedirs(p)` | `Path(p).mkdir()` |
| Remove dir | `os.rmdir(p)` | `Path(p).rmdir()` |

---

## Code Comparison Examples

### Example 1: Reading Configuration File

**os.path approach:**
```python
import os

config_path = os.path.join(os.path.expanduser("~"), ".config", "app", "config.json")
if os.path.isfile(config_path):
    with open(config_path, 'r') as f:
        content = f.read()
```

**pathlib approach:**
```python
from pathlib import Path

config_path = Path.home() / ".config" / "app" / "config.json"
if config_path.is_file():
    content = config_path.read_text()
```

---

### Example 2: Processing Multiple Files

**os.path approach:**
```python
import os

for filename in os.listdir("data"):
    filepath = os.path.join("data", filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
```

**pathlib approach:**
```python
from pathlib import Path

for filepath in Path("data").iterdir():
    if filepath.is_file():
        lines = filepath.read_text().splitlines()
```

---

### Example 3: Finding All Python Files

**os.path approach:**
```python
import os

for root, dirs, files in os.walk("project"):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            print(filepath)
```

**pathlib approach:**
```python
from pathlib import Path

for filepath in Path("project").glob("**/*.py"):
    print(filepath)
```

---

# REAL-WORLD APPLICATIONS

## 1) Bulk File Processing

```python
from pathlib import Path
import shutil

# Copy all CSV files to backup folder
source = Path("data")
backup = Path("data_backup")
backup.mkdir(exist_ok=True)

for csv_file in source.glob("*.csv"):
    destination = backup / csv_file.name
    shutil.copy2(csv_file, destination)
    print(f"Copied {csv_file.name}")
```

---

## 2) Project Structure Generator

```python
from pathlib import Path

def create_project(project_name):
    project = Path(project_name)
    
    # Create directories
    directories = [
        project / "src",
        project / "tests",
        project / "docs",
        project / "data" / "raw",
        project / "data" / "processed",
    ]
    
    for dir_path in directories:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create files
    (project / "README.md").write_text("# " + project_name)
    (project / ".gitignore").write_text("__pycache__/\n*.pyc\n.DS_Store\n")
    (project / "src" / "__init__.py").touch()
    (project / "tests" / "__init__.py").touch()
    
    print(f"Project '{project_name}' created successfully!")

# Usage
create_project("my_app")
```

---

## 3) Log File Management

```python
from pathlib import Path
import datetime

def cleanup_old_logs(log_dir, days_old=7):
    import time
    
    log_path = Path(log_dir)
    cutoff_time = time.time() - (days_old * 24 * 60 * 60)
    
    for log_file in log_path.glob("*.log"):
        if log_file.stat().st_mtime < cutoff_time:
            log_file.unlink()
            print(f"Deleted {log_file.name}")

# Usage
cleanup_old_logs("logs", days_old=30)
```

---

## 4) Config File Finder

```python
from pathlib import Path

def find_config(filename="config.json"):
    """Search for config file up the directory tree"""
    
    current = Path.cwd()
    
    while True:
        config = current / filename
        if config.exists():
            return config
        
        # Move to parent
        parent = current.parent
        if parent == current:  # Reached root
            return None
        current = parent

# Usage
config_file = find_config()
if config_file:
    print(f"Found config at: {config_file}")
    config_data = config_file.read_text()
else:
    print("Config not found")
```

---

## 5) File Renaming with Pattern

```python
from pathlib import Path

def rename_files(folder, pattern_from, pattern_to):
    """Rename files matching a pattern"""
    
    folder_path = Path(folder)
    
    for file in folder_path.glob(pattern_from):
        new_name = file.name.replace(
            pattern_from.strip("*"),
            pattern_to.strip("*")
        )
        new_path = file.parent / new_name
        file.rename(new_path)
        print(f"{file.name} → {new_name}")

# Usage
rename_files("documents", "old_*.txt", "new_*.txt")
```

---

# BEST PRACTICES

## 1) Always Use Path Objects

```python
# ✅ Good
from pathlib import Path
file_path = Path("data") / "file.csv"

# ❌ Avoid
file_path = "data" + "/" + "file.csv"

# ❌ Avoid (harder to maintain)
file_path = "data/file.csv"
```

---

## 2) Use Context Managers for File Operations

```python
from pathlib import Path

# ✅ Good (automatically closes file)
path = Path("data.txt")
with path.open('r') as f:
    content = f.read()

# ✅ Also good (simpler for small files)
content = path.read_text()

# ❌ Avoid (manual file closing)
f = open(path)
content = f.read()
# forgot to close!
```

---

## 3) Check Existence Before Operations

```python
from pathlib import Path

file_path = Path("config.json")

# ✅ Good
if file_path.exists():
    config = file_path.read_text()

# ✅ Also good (with error handling)
try:
    config = file_path.read_text()
except FileNotFoundError:
    config = "{}"

# ❌ Avoid (crashes if file missing)
config = file_path.read_text()
```

---

## 4) Use Relative Paths for Portability

```python
from pathlib import Path

# ✅ Good (works on all machines)
data_dir = Path(__file__).parent / "data"
config = data_dir / "config.json"

# ✅ Good (relative to home)
cache = Path.home() / ".cache" / "myapp"

# ❌ Avoid (hardcoded absolute paths)
config = Path("C:/Users/Lenovo/Learning/data/config.json")

# ❌ Avoid (different on each machine)
config = Path("/home/user/project/data/config.json")
```

---

## 5) Type Hints with Path

```python
from pathlib import Path
from typing import Union

# ✅ Good type hints
def read_config(path: Path) -> str:
    return path.read_text()

def process_files(directory: Path) -> list[Path]:
    return list(directory.glob("*.txt"))

# ✅ Also good (accept Path or string)
def load_data(path: Union[Path, str]) -> dict:
    p = Path(path)
    return eval(p.read_text())

# Usage
config = read_config(Path("config.json"))
files = process_files(Path.cwd())
```

---

## 6) Handle Platform Differences Gracefully

```python
from pathlib import Path
import platform

# ✅ Good
if platform.system() == "Windows":
    data_path = Path("C:\\Data")
else:
    data_path = Path.home() / "data"

# ✅ Even better (use home directory)
app_data = Path.home() / ".myapp"

# ✅ Or use environment variables
import os
data_path = Path(os.getenv("DATA_HOME", Path.home() / "data"))
```

---

## 7) Efficient Globbing for Large Directories

```python
from pathlib import Path

folder = Path("large_directory")

# ❌ Slow (converts all to list first)
# all_files = list(folder.glob("**/*"))

# ✅ Fast (processes one at a time)
for file_path in folder.glob("**/*.csv"):
    process_file(file_path)

# ✅ Good (filter while globbing)
large_files = (
    f for f in folder.glob("**/*")
    if f.is_file() and f.stat().st_size > 1000000
)
for file in large_files:
    archive_file(file)
```

---

## Summary Table

| Task | Method | Example |
|------|--------|---------|
| Create path | Constructor | `Path("data/file.csv")` |
| Join paths | `/` operator | `Path("data") / "file.csv"` |
| Get parent | `.parent` | `path.parent` |
| Get filename | `.name` | `path.name` |
| Get extension | `.suffix` | `path.suffix` |
| Check exists | `.exists()` | `path.exists()` |
| Check file | `.is_file()` | `path.is_file()` |
| Check dir | `.is_dir()` | `path.is_dir()` |
| Read file | `.read_text()` | `path.read_text()` |
| Write file | `.write_text()` | `path.write_text("data")` |
| List files | `.iterdir()` | `path.iterdir()` |
| Find files | `.glob()` | `path.glob("*.txt")` |
| Create dir | `.mkdir()` | `path.mkdir()` |
| Delete file | `.unlink()` | `path.unlink()` |
| Delete dir | `.rmdir()` | `path.rmdir()` |

---

## Key Takeaways

1. **Use pathlib for all path operations** (replaces os.path)
2. **Use `/` operator** for joining paths (cleaner than string concatenation)
3. **Path objects are more intuitive** and chainable
4. **Automatically handles cross-platform** differences
5. **Use `.exists()` and type checks** before operations
6. **Use `.glob()` for pattern matching** instead of os.walk
7. **Read/write files directly** with `.read_text()` and `.write_text()`
8. **Type hint with `Path`** for better code clarity

---

