# 🗂️ OS LIBRARY MASTER NOTES — COMPLETE GUIDE

**Author:** Prerak  
**Purpose:** Master Python's OS module for file system operations and automation  
**Version:** Complete Edition with Real-World Examples

---

## 📋 TABLE OF CONTENTS

1. [Introduction to OS Module](#introduction-to-os-module)
2. [Working with Directories](#working-with-directories)
3. [Working with Files](#working-with-files)
4. [Path Operations](#path-operations)
5. [File and Directory Information](#file-and-directory-information)
6. [Environment Variables](#environment-variables)
7. [Process Management](#process-management)
8. [Advanced Operations](#advanced-operations)
9. [OS.Path Module](#ospath-module)
10. [Pathlib Alternative](#pathlib-alternative)
11. [Real-World Projects](#real-world-projects)
12. [Best Practices](#best-practices)

---

# INTRODUCTION TO OS MODULE

## What is the OS Module?

**Definition:**  
The `os` module provides a way to interact with the operating system. It allows Python to perform operating system-dependent operations like reading/writing files, navigating directories, and executing system commands.

**Mental Model:**  
> OS module = Your Python program's bridge to your computer's file system

**Why OS Module Matters:**
- Automate file organization
- Create project structures automatically
- Process files in bulk
- Build cross-platform applications
- Manage system resources

---

## Importing the OS Module

```python
import os

# Check what's available
print(dir(os))

# Get help on specific function
help(os.getcwd)
```

---

## Platform Detection

```python
# Check operating system
print(os.name)

# Output:
# 'posix'   → Linux/Mac
# 'nt'      → Windows
# 'java'    → Jython

# Detailed platform info
import platform
print(platform.system())    # 'Windows', 'Linux', 'Darwin' (Mac)
print(platform.release())   # Version
print(platform.machine())   # Architecture
```

---

# WORKING WITH DIRECTORIES

## 1) Getting Current Directory

### Get Current Working Directory

```python
# Get current directory
current_dir = os.getcwd()
print(current_dir)

# Output (example):
# Windows: C:\Users\Prerak\Projects
# Linux:   /home/prerak/projects
# Mac:     /Users/prerak/projects
```

**Use Cases:**
- Find where your script is running
- Build relative paths
- Save outputs in current location

---

## 2) Changing Directory

### Change Working Directory

```python
# Change to a different directory
os.chdir("/path/to/directory")

# Verify the change
print(os.getcwd())

# Change to parent directory
os.chdir("..")

# Change to home directory (Windows)
os.chdir(os.path.expanduser("~"))
```

### Safe Directory Change

```python
# Save current directory before changing
original_dir = os.getcwd()

try:
    os.chdir("/new/directory")
    # Do work here
    print("Working in:", os.getcwd())
finally:
    # Always return to original directory
    os.chdir(original_dir)
```

---

## 3) Creating Directories

### Create Single Directory

```python
# Create a new directory
os.mkdir("new_folder")

# Create with error handling
try:
    os.mkdir("project_folder")
    print("Directory created successfully")
except FileExistsError:
    print("Directory already exists")
except PermissionError:
    print("Permission denied")
```

### Create Nested Directories

```python
# Create nested directories (all at once)
os.makedirs("parent/child/grandchild")

# Create only if doesn't exist (safe)
os.makedirs("my_project/data/raw", exist_ok=True)
```

**Important Difference:**

| Function | Creates Parent Dirs? | Error if Exists? |
|----------|---------------------|------------------|
| `mkdir()` | ❌ No | ✅ Yes |
| `makedirs()` | ✅ Yes | ✅ Yes (unless exist_ok=True) |

### Real-World Example

```python
# Create project structure
project_name = "automation_project"

folders = [
    f"{project_name}/data/raw",
    f"{project_name}/data/processed",
    f"{project_name}/scripts",
    f"{project_name}/output",
    f"{project_name}/logs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")
```

---

## 4) Listing Directory Contents

### List All Items

```python
# List everything in current directory
items = os.listdir()
print(items)

# List specific directory
items = os.listdir("/path/to/directory")
print(items)

# Output (example):
# ['file1.txt', 'file2.py', 'folder1', 'folder2']
```

### Filter by File Type

```python
# List only Python files
py_files = [f for f in os.listdir() if f.endswith('.py')]
print(py_files)

# List only directories
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)

# List only files (not directories)
files = [f for f in os.listdir() if os.path.isfile(f)]
print(files)
```

### Advanced Listing with Details

```python
# Get full paths
full_paths = [os.path.join(os.getcwd(), item) for item in os.listdir()]

# List with sizes
for item in os.listdir():
    if os.path.isfile(item):
        size = os.path.getsize(item)
        print(f"{item}: {size} bytes")
```

---

## 5) Removing Directories

### Remove Empty Directory

```python
# Remove empty directory only
os.rmdir("empty_folder")

# With error handling
try:
    os.rmdir("folder_name")
    print("Directory removed")
except OSError as e:
    print(f"Error: {e}")
```

### Remove Directory Tree

```python
import shutil

# Remove directory and all contents (DANGEROUS!)
shutil.rmtree("folder_with_contents")

# Safe removal with confirmation
folder = "old_project"
confirm = input(f"Delete {folder} and all contents? (yes/no): ")
if confirm.lower() == "yes":
    shutil.rmtree(folder)
    print("Deleted successfully")
```

**⚠️ Warning:**  
`shutil.rmtree()` permanently deletes everything! Use with caution.

---

## 6) Walking Directory Tree

### Walk Through All Subdirectories

```python
# Walk through directory tree
for root, dirs, files in os.walk("/path/to/directory"):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 50)
```

**Understanding os.walk():**
- `root` = current directory path
- `dirs` = list of subdirectories in root
- `files` = list of files in root

### Real-World Example: Find All Python Files

```python
# Find all .py files in project
python_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            full_path = os.path.join(root, file)
            python_files.append(full_path)

print(f"Found {len(python_files)} Python files:")
for file in python_files:
    print(file)
```

### Count Files by Extension

```python
from collections import Counter

extensions = []

for root, dirs, files in os.walk("."):
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext:  # Has extension
            extensions.append(ext)

# Count occurrences
ext_count = Counter(extensions)
print(ext_count)

# Output:
# Counter({'.py': 15, '.txt': 8, '.json': 3, '.md': 2})
```

---

# WORKING WITH FILES

## 1) Creating Files

### Create Empty File

```python
# Method 1: Using open()
with open("new_file.txt", "w") as f:
    pass  # Empty file

# Method 2: Using os
import os
os.mknod("new_file.txt")  # Linux/Mac only

# Cross-platform method
open("new_file.txt", "a").close()
```

### Create File with Content

```python
# Create and write
with open("config.txt", "w") as f:
    f.write("Setting1=Value1\n")
    f.write("Setting2=Value2\n")
```

---

## 2) Renaming Files

### Basic Rename

```python
# Rename file
os.rename("old_name.txt", "new_name.txt")

# Rename with error handling
try:
    os.rename("report.txt", "final_report.txt")
    print("File renamed successfully")
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permission denied")
```

### Bulk Rename Files

```python
# Rename all .txt files to .md
for filename in os.listdir():
    if filename.endswith(".txt"):
        new_name = filename.replace(".txt", ".md")
        os.rename(filename, new_name)
        print(f"Renamed: {filename} → {new_name}")
```

### Add Prefix/Suffix to Files

```python
# Add date prefix to all files
from datetime import datetime

date_prefix = datetime.now().strftime("%Y%m%d_")

for filename in os.listdir("."):
    if os.path.isfile(filename):
        new_name = date_prefix + filename
        os.rename(filename, new_name)
```

---

## 3) Removing Files

### Delete Single File

```python
# Remove file
os.remove("file_to_delete.txt")

# Safe removal
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("File deleted")
else:
    print("File doesn't exist")
```

### Delete Multiple Files

```python
# Delete all .log files
for filename in os.listdir():
    if filename.endswith(".log"):
        os.remove(filename)
        print(f"Deleted: {filename}")
```

### Delete Old Files

```python
import time

# Delete files older than 30 days
current_time = time.time()
days_threshold = 30
seconds_threshold = days_threshold * 24 * 60 * 60

for filename in os.listdir():
    if os.path.isfile(filename):
        file_age = current_time - os.path.getmtime(filename)
        if file_age > seconds_threshold:
            os.remove(filename)
            print(f"Deleted old file: {filename}")
```

---

## 4) Copying and Moving Files

### Copy Files (using shutil)

```python
import shutil

# Copy file
shutil.copy("source.txt", "destination.txt")

# Copy file with metadata (permissions, timestamps)
shutil.copy2("source.txt", "backup.txt")

# Copy to different directory
shutil.copy("file.txt", "/path/to/destination/")

# Copy entire directory tree
shutil.copytree("source_folder", "destination_folder")
```

### Move Files

```python
# Move file
shutil.move("file.txt", "/new/location/file.txt")

# Move and rename
shutil.move("old.txt", "/new/location/new.txt")

# Move directory
shutil.move("folder", "/new/location/")
```

### Organize Files by Extension

```python
import shutil

# Create folders and move files by type
extensions = {
    "images": [".jpg", ".png", ".gif", ".jpeg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".avi", ".mkv"],
    "music": [".mp3", ".wav", ".flac"]
}

# Create folders
for folder in extensions.keys():
    os.makedirs(folder, exist_ok=True)

# Move files
for filename in os.listdir():
    if os.path.isfile(filename):
        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder, exts in extensions.items():
            if file_ext in exts:
                shutil.move(filename, os.path.join(folder, filename))
                print(f"Moved {filename} to {folder}")
                break
```

---

# PATH OPERATIONS

## 1) Building Paths Safely

### Join Paths (Cross-Platform)

```python
# Join path components
path = os.path.join("folder", "subfolder", "file.txt")
print(path)

# Windows: folder\subfolder\file.txt
# Linux:   folder/subfolder/file.txt

# Multiple levels
project_path = os.path.join("projects", "automation", "data", "raw", "file.csv")
```

**Why os.path.join() is Important:**
- Automatically uses correct separator (\ or /)
- Works on all operating systems
- Prevents path errors

### Build Path from Current Directory

```python
# Path relative to current directory
current_dir = os.getcwd()
data_path = os.path.join(current_dir, "data", "processed")
print(data_path)

# Create the path
os.makedirs(data_path, exist_ok=True)
```

---

## 2) Path Components

### Split Path into Parts

```python
path = "/home/user/projects/automation/script.py"

# Get directory name
directory = os.path.dirname(path)
print(directory)  # /home/user/projects/automation

# Get file name
filename = os.path.basename(path)
print(filename)  # script.py

# Split into directory and filename
dir_name, file_name = os.path.split(path)
print(dir_name)   # /home/user/projects/automation
print(file_name)  # script.py
```

### Split File Name and Extension

```python
filename = "report_2024.pdf"

# Split name and extension
name, ext = os.path.splitext(filename)
print(name)  # report_2024
print(ext)   # .pdf

# Full path example
path = "/documents/annual_report.xlsx"
dir_path, filename = os.path.split(path)
name, ext = os.path.splitext(filename)

print(f"Directory: {dir_path}")
print(f"Filename: {name}")
print(f"Extension: {ext}")
```

---

## 3) Absolute vs Relative Paths

### Get Absolute Path

```python
# Convert relative to absolute path
relative_path = "data/file.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

# Get absolute path of current file
script_path = os.path.abspath(__file__)
print(script_path)
```

### Expand User Home Directory

```python
# Expand ~ to home directory
home_path = os.path.expanduser("~")
print(home_path)

# Build path in user's home
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
print(downloads)
```

### Normalize Path

```python
# Normalize path (remove redundant separators and up-level references)
messy_path = "folder//subfolder/./file.txt"
clean_path = os.path.normpath(messy_path)
print(clean_path)  # folder/subfolder/file.txt
```

---

# FILE AND DIRECTORY INFORMATION

## 1) Checking Existence

### Check if Path Exists

```python
# Check if path exists (file or directory)
if os.path.exists("file.txt"):
    print("Path exists")
else:
    print("Path doesn't exist")

# Check before operations
if not os.path.exists("output"):
    os.makedirs("output")
```

### Check File vs Directory

```python
path = "my_folder"

# Is it a file?
if os.path.isfile(path):
    print("It's a file")

# Is it a directory?
if os.path.isdir(path):
    print("It's a directory")

# Is it a symbolic link?
if os.path.islink(path):
    print("It's a symbolic link")
```

### Safe File Operations

```python
# Safe file reading
filename = "data.txt"

if os.path.exists(filename) and os.path.isfile(filename):
    with open(filename, "r") as f:
        content = f.read()
        print(content)
else:
    print(f"{filename} doesn't exist or is not a file")
```

---

## 2) File Size and Statistics

### Get File Size

```python
# Get size in bytes
size = os.path.getsize("file.txt")
print(f"Size: {size} bytes")

# Convert to human-readable format
def human_readable_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

size = os.path.getsize("large_file.zip")
print(human_readable_size(size))
```

### Get Detailed File Statistics

```python
# Get full stats
stats = os.stat("file.txt")

print(f"Size: {stats.st_size} bytes")
print(f"Created: {stats.st_ctime}")
print(f"Modified: {stats.st_mtime}")
print(f"Accessed: {stats.st_atime}")
print(f"Mode: {stats.st_mode}")
print(f"User ID: {stats.st_uid}")
print(f"Group ID: {stats.st_gid}")
```

### Get Modification Time

```python
import time
from datetime import datetime

# Get modification timestamp
mtime = os.path.getmtime("file.txt")

# Convert to readable format
mod_time = datetime.fromtimestamp(mtime)
print(f"Last modified: {mod_time}")

# Days since modification
current_time = time.time()
days_old = (current_time - mtime) / (24 * 60 * 60)
print(f"File is {days_old:.1f} days old")
```

---

## 3) Directory Size

### Calculate Directory Size

```python
def get_directory_size(path):
    """Calculate total size of directory and all contents"""
    total_size = 0
    
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    
    return total_size

# Usage
folder = "my_project"
size = get_directory_size(folder)
print(f"Total size: {human_readable_size(size)}")
```

---

## 4) File Permissions

### Check Permissions

```python
# Check if readable
if os.access("file.txt", os.R_OK):
    print("File is readable")

# Check if writable
if os.access("file.txt", os.W_OK):
    print("File is writable")

# Check if executable
if os.access("script.py", os.X_OK):
    print("File is executable")

# Check all permissions
filename = "file.txt"
permissions = []
if os.access(filename, os.R_OK):
    permissions.append("read")
if os.access(filename, os.W_OK):
    permissions.append("write")
if os.access(filename, os.X_OK):
    permissions.append("execute")

print(f"Permissions: {', '.join(permissions)}")
```

### Change Permissions (Linux/Mac)

```python
import stat

# Make file executable
os.chmod("script.sh", os.stat("script.sh").st_mode | stat.S_IEXEC)

# Set specific permissions (rwxr-xr-x)
os.chmod("file.txt", 0o755)

# Make read-only
os.chmod("config.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
```

---

# ENVIRONMENT VARIABLES

## 1) Reading Environment Variables

### Get Environment Variable

```python
# Get environment variable
home = os.environ.get("HOME")  # Linux/Mac
user = os.environ.get("USERNAME")  # Windows

print(f"Home: {home}")
print(f"User: {user}")

# With default value
api_key = os.environ.get("API_KEY", "default_key")

# Get all environment variables
all_env = os.environ
for key, value in all_env.items():
    print(f"{key}: {value}")
```

### Common Environment Variables

```python
# Operating system specific
if os.name == "nt":  # Windows
    user = os.environ.get("USERNAME")
    home = os.environ.get("USERPROFILE")
else:  # Linux/Mac
    user = os.environ.get("USER")
    home = os.environ.get("HOME")

print(f"User: {user}")
print(f"Home: {home}")
```

---

## 2) Setting Environment Variables

### Set for Current Process

```python
# Set environment variable
os.environ["API_KEY"] = "your_secret_key"
os.environ["DEBUG_MODE"] = "True"

# Access it
print(os.environ.get("API_KEY"))

# Remove environment variable
if "API_KEY" in os.environ:
    del os.environ["API_KEY"]
```

### Using .env Files (Best Practice)

```python
# Create .env file
with open(".env", "w") as f:
    f.write("DATABASE_URL=postgresql://localhost:5432/mydb\n")
    f.write("API_KEY=secret_key_here\n")
    f.write("DEBUG=True\n")

# Load .env file (using python-dotenv package)
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

# Now access variables
db_url = os.environ.get("DATABASE_URL")
api_key = os.environ.get("API_KEY")
```

---

# PROCESS MANAGEMENT

## 1) Running System Commands

### Execute Simple Command

```python
# Run system command
os.system("dir")  # Windows
os.system("ls")   # Linux/Mac

# Run and get return code
return_code = os.system("python script.py")
print(f"Return code: {return_code}")
```

### Better Way: Using subprocess

```python
import subprocess

# Run command and capture output
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

# Run with error handling
try:
    result = subprocess.run(
        ["python", "script.py"],
        check=True,
        capture_output=True,
        text=True
    )
    print("Success:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e.stderr)
```

---

## 2) Process Information

### Get Process ID

```python
# Get current process ID
pid = os.getpid()
print(f"Process ID: {pid}")

# Get parent process ID
ppid = os.getppid()
print(f"Parent Process ID: {ppid}")
```

---

# ADVANCED OPERATIONS

## 1) Temporary Files and Directories

### Create Temporary Directory

```python
import tempfile

# Create temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory: {temp_dir}")
    
    # Use temp directory
    temp_file = os.path.join(temp_dir, "temp_data.txt")
    with open(temp_file, "w") as f:
        f.write("Temporary data")
    
    # Files automatically deleted when leaving context
```

### Create Temporary File

```python
import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    temp_file.write("Temporary content")
    temp_path = temp_file.name
    print(f"Temporary file: {temp_path}")

# File still exists after context
# Manually delete when done
os.remove(temp_path)
```

---

## 2) Symbolic Links (Linux/Mac)

### Create Symbolic Link

```python
# Create symlink
source = "/path/to/original/file.txt"
link = "/path/to/link.txt"

os.symlink(source, link)

# Check if it's a symlink
if os.path.islink(link):
    print("It's a symbolic link")
    
# Read symlink target
target = os.readlink(link)
print(f"Points to: {target}")
```

---

## 3) File Locking

### Simple File Lock

```python
import fcntl  # Linux/Mac only

# Lock file for exclusive access
with open("file.txt", "w") as f:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    # Write to file (locked)
    f.write("Protected content")
    # Automatically unlocked when closed
```

---

# OS.PATH MODULE

## Complete os.path Reference

### Path Manipulation

| Function | Purpose | Example |
|----------|---------|---------|
| `os.path.join()` | Join path components | `os.path.join("a", "b", "c")` |
| `os.path.split()` | Split into dir and file | `os.path.split("/a/b/c.txt")` |
| `os.path.dirname()` | Get directory part | `os.path.dirname("/a/b/c.txt")` |
| `os.path.basename()` | Get filename part | `os.path.basename("/a/b/c.txt")` |
| `os.path.splitext()` | Split name and extension | `os.path.splitext("file.txt")` |

### Path Information

| Function | Purpose | Returns |
|----------|---------|---------|
| `os.path.exists()` | Check if path exists | Boolean |
| `os.path.isfile()` | Check if it's a file | Boolean |
| `os.path.isdir()` | Check if it's a directory | Boolean |
| `os.path.islink()` | Check if it's a symlink | Boolean |
| `os.path.isabs()` | Check if absolute path | Boolean |

### Path Transformations

| Function | Purpose | Example |
|----------|---------|---------|
| `os.path.abspath()` | Get absolute path | `os.path.abspath("file.txt")` |
| `os.path.normpath()` | Normalize path | `os.path.normpath("a//b/./c")` |
| `os.path.expanduser()` | Expand ~ to home | `os.path.expanduser("~/docs")` |
| `os.path.realpath()` | Resolve symlinks | `os.path.realpath("link")` |

### File Information

| Function | Purpose | Returns |
|----------|---------|---------|
| `os.path.getsize()` | Get file size | Bytes (int) |
| `os.path.getmtime()` | Get modification time | Timestamp (float) |
| `os.path.getctime()` | Get creation time | Timestamp (float) |
| `os.path.getatime()` | Get access time | Timestamp (float) |

---

# PATHLIB ALTERNATIVE

## Modern Approach (Python 3.4+)

### Why Pathlib?

**Advantages:**
- Object-oriented approach
- More readable
- Cross-platform by default
- Built-in methods for common operations

### Basic Pathlib Usage

```python
from pathlib import Path

# Create path object
path = Path("folder/subfolder/file.txt")

# Check existence
if path.exists():
    print("Path exists")

# Check if file or directory
if path.is_file():
    print("It's a file")

if path.is_dir():
    print("It's a directory")

# Get parent directory
parent = path.parent
print(parent)

# Get filename
filename = path.name
print(filename)

# Get extension
extension = path.suffix
print(extension)

# Get filename without extension
stem = path.stem
print(stem)
```

### Pathlib vs OS Comparison

```python
from pathlib import Path
import os

# OS way
os_path = os.path.join("folder", "file.txt")
os_exists = os.path.exists(os_path)
os_dir = os.path.dirname(os_path)

# Pathlib way (cleaner)
p = Path("folder") / "file.txt"
p_exists = p.exists()
p_dir = p.parent
```

### Common Pathlib Operations

```python
from pathlib import Path

# Current directory
cwd = Path.cwd()
print(cwd)

# Home directory
home = Path.home()
print(home)

# Create directory
Path("new_folder").mkdir(exist_ok=True)

# Create nested directories
Path("parent/child/grandchild").mkdir(parents=True, exist_ok=True)

# List directory
for item in Path(".").iterdir():
    print(item)

# Find files by pattern
py_files = list(Path(".").glob("*.py"))
print(py_files)

# Recursive search
all_py = list(Path(".").rglob("*.py"))
print(all_py)

# Read file
content = Path("file.txt").read_text()

# Write file
Path("output.txt").write_text("Hello, World!")

# Get file size
size = Path("file.txt").stat().st_size
```

---

# REAL-WORLD PROJECTS

## Project 1: File Organizer

### Organize Downloads Folder

```python
import os
import shutil
from pathlib import Path

def organize_downloads():
    """Organize files in Downloads folder by type"""
    
    downloads = Path.home() / "Downloads"
    
    # File type categories
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"]
    }
    
    # Create category folders
    for category in categories.keys():
        category_path = downloads / category
        category_path.mkdir(exist_ok=True)
    
    # Organize files
    for item in downloads.iterdir():
        if item.is_file():
            file_ext = item.suffix.lower()
            
            # Find matching category
            for category, extensions in categories.items():
                if file_ext in extensions:
                    destination = downloads / category / item.name
                    
                    # Handle duplicates
                    counter = 1
                    while destination.exists():
                        name = item.stem + f"_{counter}" + item.suffix
                        destination = downloads / category / name
                        counter += 1
                    
                    shutil.move(str(item), str(destination))
                    print(f"Moved: {item.name} → {category}")
                    break

# Run organizer
organize_downloads()
```

---

## Project 2: Duplicate File Finder

### Find and Remove Duplicate Files

```python
import os
import hashlib
from pathlib import Path

def get_file_hash(filepath):
    """Calculate MD5 hash of file"""
    hasher = hashlib.md5()
    
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in directory"""
    
    hash_dict = {}
    duplicates = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            try:
                file_hash = get_file_hash(filepath)
                
                if file_hash in hash_dict:
                    duplicates.append({
                        'original': hash_dict[file_hash],
                        'duplicate': filepath,
                        'size': os.path.getsize(filepath)
                    })
                else:
                    hash_dict[file_hash] = filepath
            
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
    
    return duplicates

# Find duplicates
folder = "path/to/folder"
dupes = find_duplicates(folder)

# Report
total_wasted_space = sum(d['size'] for d in dupes)
print(f"Found {len(dupes)} duplicate files")
print(f"Wasted space: {total_wasted_space / (1024*1024):.2f} MB")

# Remove duplicates (optional)
for dupe in dupes:
    print(f"Duplicate: {dupe['duplicate']}")
    # os.remove(dupe['duplicate'])  # Uncomment to delete
```

---

## Project 3: Backup Script

### Automated Backup System

```python
import os
import shutil
from datetime import datetime
from pathlib import Path

def create_backup(source_dir, backup_dir):
    """Create timestamped backup of directory"""
    
    # Create backup directory
    backup_root = Path(backup_dir)
    backup_root.mkdir(exist_ok=True)
    
    # Create timestamped folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_root / f"backup_{timestamp}"
    
    try:
        # Copy entire directory tree
        shutil.copytree(source_dir, backup_path)
        print(f"Backup created: {backup_path}")
        
        # Get backup size
        size = sum(
            f.stat().st_size 
            for f in backup_path.rglob('*') 
            if f.is_file()
        )
        print(f"Backup size: {size / (1024*1024):.2f} MB")
        
        return backup_path
    
    except Exception as e:
        print(f"Backup failed: {e}")
        return None

def cleanup_old_backups(backup_dir, keep_count=5):
    """Keep only recent N backups"""
    
    backup_root = Path(backup_dir)
    backups = sorted(backup_root.glob("backup_*"))
    
    # Remove old backups
    if len(backups) > keep_count:
        for old_backup in backups[:-keep_count]:
            shutil.rmtree(old_backup)
            print(f"Removed old backup: {old_backup.name}")

# Usage
source = "path/to/important/data"
backup_location = "path/to/backups"

create_backup(source, backup_location)
cleanup_old_backups(backup_location, keep_count=5)
```

---

## Project 4: Batch File Renamer

### Rename Multiple Files at Once

```python
import os
import re
from pathlib import Path

def batch_rename(directory, pattern, replacement):
    """Rename files matching pattern"""
    
    renamed_count = 0
    
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Apply pattern matching
            new_name = re.sub(pattern, replacement, filename)
            
            if new_name != filename:
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_name}")
                renamed_count += 1
    
    print(f"\nTotal files renamed: {renamed_count}")

def add_numbering(directory, prefix="file"):
    """Add sequential numbering to files"""
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for index, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{index:03d}{ext}"
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Example usage
folder = "path/to/folder"

# Remove spaces and replace with underscores
batch_rename(folder, r"\s+", "_")

# Add sequential numbering
# add_numbering(folder, prefix="image")
```

---

## Project 5: Log File Cleaner

### Automatic Log File Management

```python
import os
import time
from pathlib import Path

def clean_old_logs(log_directory, days_to_keep=7):
    """Delete log files older than specified days"""
    
    log_dir = Path(log_directory)
    current_time = time.time()
    cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)
    
    deleted_count = 0
    deleted_size = 0
    
    for log_file in log_dir.glob("*.log"):
        if log_file.is_file():
            file_time = log_file.stat().st_mtime
            
            if file_time < cutoff_time:
                file_size = log_file.stat().st_size
                log_file.unlink()
                
                deleted_count += 1
                deleted_size += file_size
                
                print(f"Deleted: {log_file.name}")
    
    print(f"\nDeleted {deleted_count} files")
    print(f"Freed {deleted_size / (1024*1024):.2f} MB")

def archive_old_logs(log_directory, days_to_archive=30):
    """Archive old log files to zip"""
    
    import zipfile
    from datetime import datetime
    
    log_dir = Path(log_directory)
    archive_dir = log_dir / "archives"
    archive_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d")
    archive_name = archive_dir / f"logs_{timestamp}.zip"
    
    current_time = time.time()
    cutoff_time = current_time - (days_to_archive * 24 * 60 * 60)
    
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for log_file in log_dir.glob("*.log"):
            if log_file.stat().st_mtime < cutoff_time:
                zipf.write(log_file, log_file.name)
                log_file.unlink()
                print(f"Archived and deleted: {log_file.name}")
    
    print(f"Archive created: {archive_name}")

# Usage
log_folder = "path/to/logs"
clean_old_logs(log_folder, days_to_keep=7)
# archive_old_logs(log_folder, days_to_archive=30)
```

---

# BEST PRACTICES

## 1) Error Handling

### Always Handle Exceptions

```python
# BAD - No error handling
os.remove("file.txt")

# GOOD - With error handling
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 2) Path Safety

### Use os.path.join() or Pathlib

```python
# BAD - Hardcoded separators (breaks on different OS)
path = "folder" + "/" + "file.txt"

# GOOD - Cross-platform
path = os.path.join("folder", "file.txt")

# BETTER - Modern approach
from pathlib import Path
path = Path("folder") / "file.txt"
```

---

## 3) Check Before Operating

### Verify Existence

```python
# Always check before operations
filename = "important.txt"

# Before deleting
if os.path.exists(filename):
    os.remove(filename)

# Before reading
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        content = f.read()
```

---

## 4) Use Context Managers

### Automatic Resource Cleanup

```python
# GOOD - File automatically closed
with open("file.txt", "w") as f:
    f.write("Content")

# GOOD - Temporary directory auto-cleaned
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    # Use temp_dir
    pass
# Automatically deleted here
```

---

## 5) Backup Before Destructive Operations

### Safety First

```python
import shutil

def safe_delete(filepath):
    """Delete file with backup"""
    if os.path.exists(filepath):
        # Create backup
        backup = filepath + ".backup"
        shutil.copy2(filepath, backup)
        
        try:
            os.remove(filepath)
            print(f"Deleted: {filepath}")
            # Remove backup if successful
            os.remove(backup)
        except Exception as e:
            print(f"Error: {e}")
            print("Backup preserved")
```

---

## 6) Use Appropriate Tools

### Choose the Right Tool

```python
# For simple operations - use os
os.rename("old.txt", "new.txt")

# For complex operations - use shutil
import shutil
shutil.copytree("source_folder", "dest_folder")

# For modern code - use pathlib
from pathlib import Path
Path("folder/file.txt").write_text("content")
```

---

## Common Pitfalls to Avoid

### ❌ Don't Do This:

```python
# 1. Hardcoded paths
path = "C:\\Users\\Prerak\\file.txt"  # Won't work on other systems

# 2. String concatenation for paths
path = "folder" + "/" + "file.txt"  # Wrong separator on Windows

# 3. Not handling errors
os.remove("file.txt")  # Crashes if file doesn't exist

# 4. Forgetting to close files
f = open("file.txt")
content = f.read()
# File never closed!

# 5. Deleting without checking
shutil.rmtree("folder")  # Dangerous!
```

### ✅ Do This Instead:

```python
# 1. Use expanduser or Path.home()
path = os.path.join(os.path.expanduser("~"), "file.txt")

# 2. Use os.path.join() or pathlib
path = os.path.join("folder", "file.txt")

# 3. Always handle errors
try:
    os.remove("file.txt")
except FileNotFoundError:
    pass

# 4. Use context managers
with open("file.txt") as f:
    content = f.read()

# 5. Check and confirm
if os.path.exists("folder"):
    confirm = input("Delete folder? (yes/no): ")
    if confirm == "yes":
        shutil.rmtree("folder")
```

---

# QUICK REFERENCE CHEAT SHEET

## Most Used Operations

```python
import os
from pathlib import Path

# Current directory
os.getcwd()

# Change directory
os.chdir("path")

# List files
os.listdir()
os.listdir("path")

# Create directory
os.makedirs("path/to/folder", exist_ok=True)

# Remove directory
os.rmdir("empty_folder")

# Remove file
os.remove("file.txt")

# Rename/Move
os.rename("old.txt", "new.txt")

# Check existence
os.path.exists("path")
os.path.isfile("file.txt")
os.path.isdir("folder")

# Join paths
os.path.join("folder", "file.txt")

# Get file info
os.path.getsize("file.txt")
os.path.getmtime("file.txt")

# Walk directory tree
for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))
```

---

# WHAT YOU'VE MASTERED

After completing these notes, you can:

✅ Navigate file systems programmatically  
✅ Create, rename, and delete files and directories  
✅ Build cross-platform file paths  
✅ Get file and directory information  
✅ Handle environment variables  
✅ Execute system commands  
✅ Organize files automatically  
✅ Build file management automation  
✅ Create backup systems  
✅ Use both os and pathlib effectively  
✅ Handle errors safely  
✅ Build production-ready file utilities  

**You're ready to automate file operations and build real-world tools!**

---

# PRACTICE EXERCISES

## Beginner Level

1. List all files in your Downloads folder
2. Create a project folder structure
3. Count files by extension
4. Rename all files in a folder with a prefix
5. Find the largest file in a directory

## Intermediate Level

1. Organize downloads by file type
2. Find duplicate files
3. Delete files older than 30 days
4. Create automated backup script
5. Build file search tool by content

## Advanced Level

1. Monitor directory for changes
2. Synchronize two folders
3. Build file encryption tool
4. Create file versioning system
5. Develop log rotation system

---

**End of OS Library Master Notes**

*Master file operations, automate your workflow!* 🚀