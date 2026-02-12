# 🤖 SELENIUM MASTER NOTES — COMPLETE GUIDE

**Author:** Prerak  
**Purpose:** Master Selenium for web automation and browser control  
**Version:** Complete Edition with Real-World Examples

---

## 📋 TABLE OF CONTENTS

1. [Introduction to Selenium](#introduction-to-selenium)
2. [Setup and Installation](#setup-and-installation)
3. [WebDriver Basics](#webdriver-basics)
4. [Finding Elements](#finding-elements)
5. [Interacting with Elements](#interacting-with-elements)
6. [Navigation and Windows](#navigation-and-windows)
7. [Waits and Synchronization](#waits-and-synchronization)
8. [Forms and User Input](#forms-and-user-input)
9. [Screenshots and Downloads](#screenshots-and-downloads)
10. [Advanced Techniques](#advanced-techniques)
11. [Real-World Applications](#real-world-applications)
12. [Best Practices](#best-practices)

---

# INTRODUCTION TO SELENIUM

## What is Selenium?

**Definition:**  
Selenium is a powerful tool for controlling web browsers through programs and automating browser tasks. It's the industry standard for browser automation.

**Mental Model:**  
> Selenium = Your program controlling a real browser like a human would

**Why Selenium Matters:**
- Automate repetitive web tasks
- Test web applications
- Scrape JavaScript-heavy websites
- Fill forms automatically
- Take screenshots
- Download files from websites
- Monitor website changes

---

## Selenium vs Other Tools

| Tool | Best For | JavaScript Support |
|------|----------|-------------------|
| **Selenium** | Full browser control, testing | ✅ Full |
| **Requests** | Simple HTTP requests | ❌ None |
| **Beautiful Soup** | Parsing static HTML | ❌ None |
| **Scrapy** | Large-scale scraping | ⚠️ Limited |
| **Playwright** | Modern alternative | ✅ Full |

**When to Use Selenium:**
- Website requires JavaScript
- Need to interact (click, type, scroll)
- Need to wait for dynamic content
- Simulating real user behavior
- Testing web applications

---

# SETUP AND INSTALLATION

## 1) Install Selenium

```bash
# Install Selenium
pip install selenium

# Verify installation
python -c "import selenium; print(selenium.__version__)"
```

---

## 2) Install WebDriver

### Option 1: WebDriver Manager (RECOMMENDED)

```bash
# Install webdriver-manager (easiest way)
pip install webdriver-manager
```

**Advantages:**
- Automatic driver download
- Always uses correct version
- Cross-platform
- No manual configuration

---

### Option 2: Manual Installation

**Chrome:**
1. Download ChromeDriver from https://chromedriver.chromium.org/
2. Match Chrome browser version
3. Add to system PATH

**Firefox:**
1. Download GeckoDriver from https://github.com/mozilla/geckodriver/releases
2. Add to system PATH

**Edge:**
1. Download EdgeDriver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

---

## 3) Basic Setup

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatic WebDriver setup (RECOMMENDED)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://www.google.com")

# Close browser
driver.quit()
```

---

## 4) Browser Options

### Chrome Options

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome options
chrome_options = Options()

# Headless mode (no GUI)
chrome_options.add_argument("--headless")

# Window size
chrome_options.add_argument("--window-size=1920,1080")

# Disable GPU (for headless)
chrome_options.add_argument("--disable-gpu")

# User agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# Disable notifications
chrome_options.add_argument("--disable-notifications")

# Incognito mode
chrome_options.add_argument("--incognito")

# Disable images (faster loading)
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Create driver with options
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
```

---

### Firefox Options

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = Options()

# Headless mode
firefox_options.add_argument("--headless")

# Create Firefox driver
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=firefox_options
)
```

---

# WEBDRIVER BASICS

## 1) Opening Websites

### Navigate to URL

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://www.python.org")

# Get current URL
current_url = driver.current_url
print(current_url)

# Get page title
title = driver.title
print(title)

# Get page source
page_source = driver.page_source
```

---

## 2) Browser Navigation

### Back, Forward, Refresh

```python
# Navigate to first page
driver.get("https://www.google.com")

# Go to another page
driver.get("https://www.python.org")

# Go back
driver.back()

# Go forward
driver.forward()

# Refresh page
driver.refresh()
```

---

## 3) Window Management

### Window Size and Position

```python
# Maximize window
driver.maximize_window()

# Set specific size
driver.set_window_size(1920, 1080)

# Get window size
size = driver.get_window_size()
print(f"Width: {size['width']}, Height: {size['height']}")

# Set window position
driver.set_window_position(0, 0)

# Fullscreen
driver.fullscreen_window()

# Minimize
driver.minimize_window()
```

---

## 4) Closing Browser

### Quit vs Close

```python
# Close current window/tab
driver.close()

# Close browser and end session
driver.quit()  # RECOMMENDED - Always use quit()
```

**Important:**  
Always use `driver.quit()` in a `finally` block to ensure cleanup:

```python
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    # Your automation code here
finally:
    driver.quit()  # Ensures browser closes even if error occurs
```

---

# FINDING ELEMENTS

## 1) Locator Strategies

### All Locator Types

| Strategy | Syntax | Example |
|----------|--------|---------|
| **ID** | `By.ID` | `driver.find_element(By.ID, "username")` |
| **NAME** | `By.NAME` | `driver.find_element(By.NAME, "email")` |
| **CLASS** | `By.CLASS_NAME` | `driver.find_element(By.CLASS_NAME, "btn-primary")` |
| **TAG** | `By.TAG_NAME` | `driver.find_element(By.TAG_NAME, "h1")` |
| **CSS** | `By.CSS_SELECTOR` | `driver.find_element(By.CSS_SELECTOR, "div.content > p")` |
| **XPATH** | `By.XPATH` | `driver.find_element(By.XPATH, "//button[@id='submit']")` |
| **LINK TEXT** | `By.LINK_TEXT` | `driver.find_element(By.LINK_TEXT, "Click Here")` |
| **PARTIAL LINK** | `By.PARTIAL_LINK_TEXT` | `driver.find_element(By.PARTIAL_LINK_TEXT, "Click")` |

---

## 2) Find Single Element

### Basic Finders

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Find by ID (fastest and most reliable)
element = driver.find_element(By.ID, "username")

# Find by name
element = driver.find_element(By.NAME, "email")

# Find by class name
element = driver.find_element(By.CLASS_NAME, "btn-primary")

# Find by tag name
element = driver.find_element(By.TAG_NAME, "h1")

# Find by link text (exact match)
element = driver.find_element(By.LINK_TEXT, "Sign Up")

# Find by partial link text
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
```

---

## 3) Find Multiple Elements

### Find All Matching Elements

```python
from selenium.webdriver.common.by import By

# Find all elements with class name
elements = driver.find_elements(By.CLASS_NAME, "product-card")
print(f"Found {len(elements)} products")

# Find all links
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate through elements
for link in links:
    print(link.text)
    print(link.get_attribute("href"))
```

---

## 4) CSS Selectors

### CSS Selector Examples

```python
from selenium.webdriver.common.by import By

# Element with ID
element = driver.find_element(By.CSS_SELECTOR, "#username")

# Element with class
element = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Tag with class
element = driver.find_element(By.CSS_SELECTOR, "button.submit-btn")

# Direct child
element = driver.find_element(By.CSS_SELECTOR, "div.content > p")

# Descendant
element = driver.find_element(By.CSS_SELECTOR, "div.content p")

# Attribute selector
element = driver.find_element(By.CSS_SELECTOR, "input[type='email']")

# Multiple classes
element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

# Nth child
element = driver.find_element(By.CSS_SELECTOR, "ul li:nth-child(3)")

# First/last child
first = driver.find_element(By.CSS_SELECTOR, "ul li:first-child")
last = driver.find_element(By.CSS_SELECTOR, "ul li:last-child")
```

---

## 5) XPath Selectors

### XPath Examples

```python
from selenium.webdriver.common.by import By

# Absolute path (not recommended)
element = driver.find_element(By.XPATH, "/html/body/div/form/input")

# Relative path (RECOMMENDED)
element = driver.find_element(By.XPATH, "//input[@id='username']")

# By attribute
element = driver.find_element(By.XPATH, "//button[@type='submit']")

# By text content
element = driver.find_element(By.XPATH, "//button[text()='Sign Up']")

# Contains text
element = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign')]")

# By class
element = driver.find_element(By.XPATH, "//div[@class='container']")

# Contains class
element = driver.find_element(By.XPATH, "//div[contains(@class, 'container')]")

# Multiple conditions (AND)
element = driver.find_element(By.XPATH, "//input[@type='text' and @name='email']")

# Multiple conditions (OR)
element = driver.find_element(By.XPATH, "//input[@type='text' or @type='email']")

# Parent element
element = driver.find_element(By.XPATH, "//input[@id='username']/parent::div")

# Following sibling
element = driver.find_element(By.XPATH, "//label[@for='username']/following-sibling::input")

# By index
element = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
```

---

## 6) Choosing the Right Locator

### Best Practices

**Priority Order (Best to Worst):**
1. **ID** - Fastest, most reliable
2. **NAME** - Good for forms
3. **CSS Selector** - Flexible and fast
4. **XPath** - Most powerful but slower

```python
# ✅ BEST - Use ID when available
element = driver.find_element(By.ID, "username")

# ✅ GOOD - Use name for form elements
element = driver.find_element(By.NAME, "email")

# ✅ GOOD - CSS selector for complex queries
element = driver.find_element(By.CSS_SELECTOR, "div.login-form input[type='email']")

# ⚠️ ACCEPTABLE - XPath for complex navigation
element = driver.find_element(By.XPATH, "//div[@class='form']//input[@type='email']")

# ❌ AVOID - Absolute XPath (breaks easily)
element = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[2]")
```

---

# INTERACTING WITH ELEMENTS

## 1) Clicking Elements

### Click Actions

```python
from selenium.webdriver.common.by import By

# Click button
button = driver.find_element(By.ID, "submit-btn")
button.click()

# Click link
link = driver.find_element(By.LINK_TEXT, "Sign Up")
link.click()

# Click checkbox
checkbox = driver.find_element(By.ID, "agree-terms")
checkbox.click()

# Click radio button
radio = driver.find_element(By.CSS_SELECTOR, "input[value='option1']")
radio.click()
```

---

## 2) Typing Text

### Send Keys

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Type text
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("prerak@email.com")

# Clear and type
password_field = driver.find_element(By.ID, "password")
password_field.clear()  # Clear existing text
password_field.send_keys("SecurePassword123")

# Type and press Enter
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Type multiple keys
element.send_keys(Keys.CONTROL, "a")  # Select all
element.send_keys(Keys.CONTROL, "c")  # Copy
```

---

## 3) Special Keys

### Keyboard Keys

```python
from selenium.webdriver.common.keys import Keys

# Common special keys
element.send_keys(Keys.ENTER)         # Enter
element.send_keys(Keys.RETURN)        # Return
element.send_keys(Keys.TAB)           # Tab
element.send_keys(Keys.ESCAPE)        # Escape
element.send_keys(Keys.BACKSPACE)     # Backspace
element.send_keys(Keys.DELETE)        # Delete
element.send_keys(Keys.SPACE)         # Space

# Arrow keys
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ARROW_UP)
element.send_keys(Keys.ARROW_LEFT)
element.send_keys(Keys.ARROW_RIGHT)

# Modifier keys
element.send_keys(Keys.CONTROL, "a")  # Ctrl+A
element.send_keys(Keys.SHIFT, "text") # Shift+text
element.send_keys(Keys.ALT, "f")      # Alt+F

# Function keys
element.send_keys(Keys.F1)
element.send_keys(Keys.F5)  # Refresh
```

---

## 4) Getting Element Information

### Element Properties

```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "username")

# Get text content
text = element.text
print(text)

# Get attribute value
value = element.get_attribute("value")
placeholder = element.get_attribute("placeholder")
href = element.get_attribute("href")

# Get CSS property
color = element.value_of_css_property("color")
font_size = element.value_of_css_property("font-size")

# Check if enabled
is_enabled = element.is_enabled()

# Check if displayed
is_displayed = element.is_displayed()

# Check if selected (checkbox/radio)
is_selected = element.is_selected()

# Get element tag name
tag = element.tag_name

# Get element size
size = element.size  # {'width': 200, 'height': 50}

# Get element location
location = element.location  # {'x': 100, 'y': 200}
```

---

## 5) Dropdowns and Select

### Working with Select Elements

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Find dropdown
dropdown = driver.find_element(By.ID, "country")
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("India")

# Select by value attribute
select.select_by_value("IN")

# Select by index (0-based)
select.select_by_index(2)

# Get selected option
selected_option = select.first_selected_option
print(selected_option.text)

# Get all options
all_options = select.options
for option in all_options:
    print(option.text)

# Deselect (for multi-select only)
select.deselect_by_visible_text("India")
select.deselect_all()
```

---

## 6) Checkboxes and Radio Buttons

### Check/Uncheck

```python
from selenium.webdriver.common.by import By

# Checkbox
checkbox = driver.find_element(By.ID, "agree-terms")

# Check if already selected
if not checkbox.is_selected():
    checkbox.click()  # Check it

# Uncheck
if checkbox.is_selected():
    checkbox.click()  # Uncheck it

# Radio button
radio = driver.find_element(By.CSS_SELECTOR, "input[value='male']")
radio.click()
```

---

# NAVIGATION AND WINDOWS

## 1) Tabs and Windows

### Multiple Windows

```python
from selenium.webdriver.common.by import By

# Get current window handle
main_window = driver.current_window_handle

# Open link in new tab (using JavaScript)
link = driver.find_element(By.LINK_TEXT, "Open in New Tab")
driver.execute_script("window.open(arguments[0], '_blank');", link.get_attribute("href"))

# Get all window handles
all_windows = driver.window_handles

# Switch to new window
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Do something in new window
print(driver.title)

# Close current window
driver.close()

# Switch back to main window
driver.switch_to.window(main_window)
```

---

### Open New Tab

```python
# Open new tab with JavaScript
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])

# Close tab and return to first
driver.close()
driver.switch_to.window(driver.window_handles[0])
```

---

## 2) Frames and iFrames

### Switch to Frame

```python
from selenium.webdriver.common.by import By

# Switch to frame by index
driver.switch_to.frame(0)

# Switch to frame by name or ID
driver.switch_to.frame("frame_name")

# Switch to frame by WebElement
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Switch back to main content
driver.switch_to.default_content()

# Switch to parent frame
driver.switch_to.parent_frame()
```

---

## 3) Alerts and Popups

### Handle JavaScript Alerts

```python
from selenium.webdriver.common.by import By

# Click button that triggers alert
button = driver.find_element(By.ID, "alert-btn")
button.click()

# Switch to alert
alert = driver.switch_to.alert

# Get alert text
alert_text = alert.text
print(alert_text)

# Accept alert (click OK)
alert.accept()

# Dismiss alert (click Cancel)
# alert.dismiss()

# Type in prompt alert
# alert.send_keys("Response text")
# alert.accept()
```

---

## 4) Scrolling

### Scroll Actions

```python
from selenium.webdriver.common.by import By

# Scroll to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll to top
driver.execute_script("window.scrollTo(0, 0);")

# Scroll by pixel amount
driver.execute_script("window.scrollBy(0, 500);")  # Scroll down 500px

# Scroll element into view
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Smooth scroll
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
```

---

# WAITS AND SYNCHRONIZATION

## 1) Implicit Wait

### Global Wait

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Set implicit wait (applies to all find_element calls)
driver.implicitly_wait(10)  # Wait up to 10 seconds

# Now all find operations wait up to 10 seconds
driver.get("https://www.example.com")
element = driver.find_element(By.ID, "username")  # Waits if not immediately found
```

**Note:**  
Implicit wait applies globally and affects all `find_element` calls.

---

## 2) Explicit Wait

### Wait for Specific Conditions

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Create wait object
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Wait for element to be present
element = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Wait for element to be clickable
button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit-btn"))
)
button.click()

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)

# Wait for text to be present
wait.until(
    EC.text_to_be_present_in_element((By.ID, "status"), "Complete")
)
```

---

## 3) Expected Conditions

### Common Wait Conditions

```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 10)

# Element exists in DOM
wait.until(EC.presence_of_element_located((By.ID, "element")))

# Element is visible
wait.until(EC.visibility_of_element_located((By.ID, "element")))

# Element is clickable
wait.until(EC.element_to_be_clickable((By.ID, "button")))

# Element is selected
wait.until(EC.element_to_be_selected((By.ID, "checkbox")))

# Text present in element
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))

# Title contains text
wait.until(EC.title_contains("Welcome"))

# Title is exactly
wait.until(EC.title_is("Home Page"))

# URL contains text
wait.until(EC.url_contains("dashboard"))

# Alert is present
wait.until(EC.alert_is_present())

# Element becomes invisible
wait.until(EC.invisibility_of_element_located((By.ID, "loading")))

# Element becomes stale (removed from DOM)
element = driver.find_element(By.ID, "dynamic")
wait.until(EC.staleness_of(element))

# Number of windows
wait.until(EC.number_of_windows_to_be(2))

# Frame to be available
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))
```

---

## 4) Custom Wait Conditions

### Create Custom Waits

```python
from selenium.webdriver.support.ui import WebDriverWait

def element_has_class(locator, class_name):
    """Wait for element to have specific class"""
    def _predicate(driver):
        element = driver.find_element(*locator)
        classes = element.get_attribute("class").split()
        return class_name in classes
    return _predicate

# Usage
wait = WebDriverWait(driver, 10)
wait.until(element_has_class((By.ID, "status"), "success"))
```

---

## 5) Sleep (Not Recommended)

### Fixed Delays

```python
import time

# Hard wait (NOT RECOMMENDED - use explicit waits instead)
time.sleep(5)  # Wait 5 seconds

# Only use when absolutely necessary
# Example: Waiting for animation to complete
```

**Note:**  
Prefer explicit waits over `time.sleep()` for better performance and reliability.

---

# FORMS AND USER INPUT

## 1) Filling Forms

### Complete Form Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.example.com/register")

# Text input
driver.find_element(By.ID, "first_name").send_keys("Prerak")
driver.find_element(By.ID, "last_name").send_keys("Patel")

# Email
driver.find_element(By.ID, "email").send_keys("prerak@example.com")

# Password
driver.find_element(By.ID, "password").send_keys("SecurePass123")

# Dropdown
country_select = Select(driver.find_element(By.ID, "country"))
country_select.select_by_visible_text("India")

# Radio button
driver.find_element(By.CSS_SELECTOR, "input[value='male']").click()

# Checkbox
driver.find_element(By.ID, "terms").click()

# Submit form
driver.find_element(By.ID, "submit-btn").click()
```

---

## 2) File Upload

### Upload Files

```python
from selenium.webdriver.common.by import By
import os

# Find file input
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

# Provide absolute path to file
file_path = os.path.abspath("document.pdf")
file_input.send_keys(file_path)

# Submit form
driver.find_element(By.ID, "upload-btn").click()
```

---

## 3) Form Validation

### Check Form Errors

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Submit form with invalid data
driver.find_element(By.ID, "email").send_keys("invalid-email")
driver.find_element(By.ID, "submit-btn").click()

# Wait for error message
wait = WebDriverWait(driver, 5)
error = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
)

print(f"Error: {error.text}")

# Check if field has error class
email_field = driver.find_element(By.ID, "email")
has_error = "error" in email_field.get_attribute("class")
```

---

# SCREENSHOTS AND DOWNLOADS

## 1) Taking Screenshots

### Screenshot Methods

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org")

# Full page screenshot
driver.save_screenshot("page.png")

# Alternative method
driver.get_screenshot_as_file("page.png")

# Get screenshot as PNG bytes
png_bytes = driver.get_screenshot_as_png()

# Get screenshot as base64
base64_screenshot = driver.get_screenshot_as_base64()
```

---

### Element Screenshot

```python
from selenium.webdriver.common.by import By

# Find element
element = driver.find_element(By.ID, "logo")

# Screenshot of specific element
element.screenshot("logo.png")

# As PNG bytes
png_bytes = element.screenshot_as_png

# As base64
base64_img = element.screenshot_as_base64
```

---

## 2) Downloading Files

### Configure Download Directory

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Set download directory
download_dir = os.path.abspath("downloads")

chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,  # Don't ask where to save
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)

# Click download link
driver.get("https://www.example.com/downloads")
driver.find_element(By.LINK_TEXT, "Download PDF").click()

# Wait for download to complete
import time
time.sleep(5)  # In production, use better wait logic

driver.quit()
```

---

### Wait for Download Completion

```python
import os
import time

def wait_for_download(directory, timeout=30):
    """Wait for downloads to complete"""
    seconds = 0
    
    while seconds < timeout:
        # Check if any .crdownload files (Chrome temp files)
        temp_files = [f for f in os.listdir(directory) if f.endswith('.crdownload')]
        
        if not temp_files:
            return True
        
        time.sleep(1)
        seconds += 1
    
    return False

# Usage
download_dir = "downloads"
driver.find_element(By.LINK_TEXT, "Download").click()

if wait_for_download(download_dir):
    print("Download complete!")
else:
    print("Download timeout!")
```

---

# ADVANCED TECHNIQUES

## 1) JavaScript Execution

### Execute JavaScript

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Execute simple JavaScript
driver.execute_script("alert('Hello from Selenium');")

# Get return value
title = driver.execute_script("return document.title;")
print(title)

# Pass arguments to JavaScript
element = driver.find_element(By.ID, "username")
driver.execute_script("arguments[0].style.border = '3px solid red';", element)

# Scroll using JavaScript
driver.execute_script("window.scrollTo(0, 500);")

# Click using JavaScript (when normal click doesn't work)
button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", button)

# Get element position
position = driver.execute_script(
    "return arguments[0].getBoundingClientRect();", 
    element
)
```

---

## 2) Action Chains

### Complex Mouse Actions

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Create ActionChains object
actions = ActionChains(driver)

# Hover over element
element = driver.find_element(By.ID, "menu")
actions.move_to_element(element).perform()

# Right click
actions.context_click(element).perform()

# Double click
actions.double_click(element).perform()

# Click and hold
actions.click_and_hold(element).perform()

# Release
actions.release().perform()

# Drag and drop
source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")
actions.drag_and_drop(source, target).perform()

# Chain multiple actions
actions.move_to_element(element).click().send_keys("text").perform()
```

---

## 3) Cookies

### Manage Cookies

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Get all cookies
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

# Get specific cookie
cookie = driver.get_cookie("session_id")
print(cookie)

# Add cookie
driver.add_cookie({
    "name": "user_id",
    "value": "12345",
    "domain": ".example.com"
})

# Delete cookie
driver.delete_cookie("user_id")

# Delete all cookies
driver.delete_all_cookies()
```

---

## 4) Headless Mode

### Run Without GUI

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

# Browser runs invisibly
driver.get("https://www.example.com")
print(driver.title)

driver.quit()
```

---

## 5) Proxy Configuration

### Use Proxy

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# HTTP proxy
chrome_options.add_argument('--proxy-server=http://proxy.example.com:8080')

# SOCKS proxy
chrome_options.add_argument('--proxy-server=socks5://proxy.example.com:1080')

driver = webdriver.Chrome(options=chrome_options)
```

---

## 6) User Agent

### Change User Agent

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Set custom user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)

# Verify user agent
ua = driver.execute_script("return navigator.userAgent;")
print(ua)
```

---

# REAL-WORLD APPLICATIONS

## Application 1: Login Automation

### Automated Login System

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAutomation:
    """Automate login to websites"""
    
    def __init__(self, headless=False):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self, url, username, password, 
              username_field_id, password_field_id, submit_button_id):
        """Perform login"""
        try:
            # Navigate to login page
            self.driver.get(url)
            
            # Wait for username field
            username_input = self.wait.until(
                EC.presence_of_element_located((By.ID, username_field_id))
            )
            
            # Enter credentials
            username_input.send_keys(username)
            
            password_input = self.driver.find_element(By.ID, password_field_id)
            password_input.send_keys(password)
            
            # Submit
            submit_button = self.driver.find_element(By.ID, submit_button_id)
            submit_button.click()
            
            # Wait for redirect
            self.wait.until(EC.url_changes(url))
            
            print("Login successful!")
            return True
            
        except Exception as e:
            print(f"Login failed: {e}")
            return False
    
    def is_logged_in(self, indicator_element_id):
        """Check if login was successful"""
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, indicator_element_id))
            )
            return True
        except:
            return False
    
    def close(self):
        """Close browser"""
        self.driver.quit()

# Usage
login_bot = LoginAutomation(headless=False)
success = login_bot.login(
    url="https://example.com/login",
    username="user@example.com",
    password="password123",
    username_field_id="email",
    password_field_id="password",
    submit_button_id="login-btn"
)

if success:
    print("Logged in successfully!")

# Keep browser open or do more actions
# login_bot.close()
```

---

## Application 2: Form Automation

### Bulk Form Submission

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FormAutomation:
    """Automate form filling"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def fill_registration_form(self, data):
        """Fill registration form with data"""
        try:
            # Navigate to form
            self.driver.get(data['url'])
            
            # Fill text fields
            for field_id, value in data['fields'].items():
                element = self.wait.until(
                    EC.presence_of_element_located((By.ID, field_id))
                )
                element.clear()
                element.send_keys(value)
                time.sleep(0.5)  # Human-like delay
            
            # Handle dropdowns
            if 'dropdowns' in data:
                for dropdown_id, value in data['dropdowns'].items():
                    dropdown = Select(self.driver.find_element(By.ID, dropdown_id))
                    dropdown.select_by_visible_text(value)
            
            # Handle checkboxes
            if 'checkboxes' in data:
                for checkbox_id in data['checkboxes']:
                    checkbox = self.driver.find_element(By.ID, checkbox_id)
                    if not checkbox.is_selected():
                        checkbox.click()
            
            # Submit
            submit_btn = self.driver.find_element(By.ID, data['submit_button'])
            submit_btn.click()
            
            # Wait for success message
            success = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            
            print(f"Form submitted: {success.text}")
            return True
            
        except Exception as e:
            print(f"Form submission failed: {e}")
            return False
    
    def close(self):
        self.driver.quit()

# Usage
form_bot = FormAutomation()

# Data for multiple form submissions
forms_data = [
    {
        'url': 'https://example.com/register',
        'fields': {
            'first_name': 'Prerak',
            'last_name': 'Patel',
            'email': 'prerak@example.com',
            'phone': '1234567890'
        },
        'dropdowns': {
            'country': 'India'
        },
        'checkboxes': ['terms', 'newsletter'],
        'submit_button': 'submit-btn'
    }
]

# Fill multiple forms
for form_data in forms_data:
    form_bot.fill_registration_form(form_data)
    time.sleep(2)

form_bot.close()
```

---

## Application 3: Web Scraper with JavaScript

### Dynamic Content Scraper

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class DynamicScraper:
    """Scrape JavaScript-heavy websites"""
    
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def scrape_infinite_scroll(self, url, item_selector, scroll_pause=2):
        """Scrape page with infinite scroll"""
        self.driver.get(url)
        
        items = []
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Get current items
            elements = self.driver.find_elements(By.CSS_SELECTOR, item_selector)
            
            for element in elements:
                item_data = {
                    'text': element.text,
                    'html': element.get_attribute('outerHTML')
                }
                if item_data not in items:
                    items.append(item_data)
            
            # Scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            
            # Check if reached bottom
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        return items
    
    def scrape_with_pagination(self, url, item_selector, next_button_selector):
        """Scrape paginated content"""
        self.driver.get(url)
        all_items = []
        page = 1
        
        while True:
            print(f"Scraping page {page}...")
            
            # Wait for items to load
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
            )
            
            # Get items on current page
            items = self.driver.find_elements(By.CSS_SELECTOR, item_selector)
            for item in items:
                all_items.append(item.text)
            
            # Try to find next button
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, next_button_selector)
                if not next_button.is_enabled():
                    break
                next_button.click()
                time.sleep(2)
                page += 1
            except:
                break
        
        return all_items
    
    def close(self):
        self.driver.quit()

# Usage
scraper = DynamicScraper(headless=True)

# Scrape infinite scroll page
# items = scraper.scrape_infinite_scroll(
#     url="https://example.com/products",
#     item_selector=".product-card"
# )

# Scrape paginated content
# items = scraper.scrape_with_pagination(
#     url="https://example.com/products",
#     item_selector=".product",
#     next_button_selector=".next-page"
# )

# print(f"Scraped {len(items)} items")
# scraper.close()
```

---

## Application 4: Screenshot Taker

### Automated Screenshot Tool

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os

class ScreenshotTool:
    """Take screenshots of websites"""
    
    def __init__(self, output_dir="screenshots"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=options)
        self.output_dir = output_dir
        
        os.makedirs(output_dir, exist_ok=True)
    
    def screenshot_url(self, url, filename=None):
        """Take screenshot of URL"""
        self.driver.get(url)
        
        # Wait for page to load
        self.driver.implicitly_wait(5)
        
        # Generate filename
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            domain = url.split("//")[1].split("/")[0]
            filename = f"{domain}_{timestamp}.png"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Take screenshot
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        
        return filepath
    
    def screenshot_element(self, url, selector, filename=None):
        """Take screenshot of specific element"""
        self.driver.get(url)
        
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"element_{timestamp}.png"
        
        filepath = os.path.join(self.output_dir, filename)
        element.screenshot(filepath)
        
        print(f"Element screenshot saved: {filepath}")
        return filepath
    
    def screenshot_multiple(self, urls):
        """Take screenshots of multiple URLs"""
        results = []
        
        for url in urls:
            try:
                filepath = self.screenshot_url(url)
                results.append({'url': url, 'file': filepath, 'success': True})
            except Exception as e:
                results.append({'url': url, 'error': str(e), 'success': False})
        
        return results
    
    def close(self):
        self.driver.quit()

# Usage
screenshot_tool = ScreenshotTool("screenshots")

# Single screenshot
# screenshot_tool.screenshot_url("https://www.python.org")

# Multiple screenshots
urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]
# results = screenshot_tool.screenshot_multiple(urls)

# for result in results:
#     if result['success']:
#         print(f"✓ {result['url']}: {result['file']}")
#     else:
#         print(f"✗ {result['url']}: {result['error']}")

# screenshot_tool.close()
```

---

## Application 5: Data Extraction Bot

### Extract Structured Data

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

class DataExtractor:
    """Extract structured data from websites"""
    
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def extract_table(self, url, table_selector):
        """Extract data from HTML table"""
        self.driver.get(url)
        
        # Wait for table
        table = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, table_selector))
        )
        
        # Extract headers
        headers = []
        header_cells = table.find_elements(By.TAG_NAME, "th")
        for cell in header_cells:
            headers.append(cell.text)
        
        # Extract rows
        rows_data = []
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        for row in rows[1:]:  # Skip header row
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            if row_data:
                rows_data.append(row_data)
        
        # Create DataFrame
        df = pd.DataFrame(rows_data, columns=headers)
        return df
    
    def extract_list_items(self, url, item_selector, fields):
        """Extract list of items with specific fields"""
        self.driver.get(url)
        
        # Wait for items
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
        )
        
        items = self.driver.find_elements(By.CSS_SELECTOR, item_selector)
        
        data = []
        for item in items:
            item_data = {}
            
            for field_name, field_selector in fields.items():
                try:
                    element = item.find_element(By.CSS_SELECTOR, field_selector)
                    item_data[field_name] = element.text
                except:
                    item_data[field_name] = None
            
            data.append(item_data)
        
        return pd.DataFrame(data)
    
    def save_to_csv(self, df, filename):
        """Save DataFrame to CSV"""
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    
    def close(self):
        self.driver.quit()

# Usage
extractor = DataExtractor(headless=True)

# Extract table
# df = extractor.extract_table(
#     url="https://example.com/data",
#     table_selector="table.data-table"
# )
# extractor.save_to_csv(df, "table_data.csv")

# Extract list items
# fields = {
#     'title': '.product-title',
#     'price': '.product-price',
#     'rating': '.product-rating'
# }
# df = extractor.extract_list_items(
#     url="https://example.com/products",
#     item_selector=".product-card",
#     fields=fields
# )
# extractor.save_to_csv(df, "products.csv")

# extractor.close()
```

---

# BEST PRACTICES

## 1) Always Use try-finally

```python
from selenium import webdriver

# ✅ GOOD - Ensures cleanup
driver = webdriver.Chrome()

try:
    driver.get("https://www.example.com")
    # Your automation code
finally:
    driver.quit()  # Always closes even if error occurs
```

---

## 2) Use Explicit Waits

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ❌ BAD - Hard coded sleep
import time
time.sleep(5)

# ✅ GOOD - Wait for specific condition
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.ID, "element"))
)
```

---

## 3) Prefer ID and Name Locators

```python
# ✅ BEST - ID (fastest and most reliable)
element = driver.find_element(By.ID, "username")

# ✅ GOOD - Name
element = driver.find_element(By.NAME, "email")

# ⚠️ ACCEPTABLE - CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "#username")

# ⚠️ USE SPARINGLY - XPath
element = driver.find_element(By.XPATH, "//input[@id='username']")

# ❌ AVOID - Absolute XPath
element = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[1]")
```

---

## 4) Handle Exceptions Properly

```python
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)

# ✅ GOOD - Specific exception handling
try:
    element = driver.find_element(By.ID, "username")
    element.send_keys("user")
except NoSuchElementException:
    print("Element not found")
except TimeoutException:
    print("Operation timed out")
except StaleElementReferenceException:
    print("Element is no longer in DOM")
    # Re-find element
    element = driver.find_element(By.ID, "username")
```

---

## 5) Use Page Object Model

```python
# ✅ GOOD - Page Object Pattern
class LoginPage:
    """Page Object for Login Page"""
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://example.com/login"
    
    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    submit_button = (By.ID, "submit")
    
    def load(self):
        self.driver.get(self.url)
    
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

# Usage
driver = webdriver.Chrome()
login_page = LoginPage(driver)
login_page.load()
login_page.login("user", "pass")
```

---

## 6) Be Respectful to Websites

```python
import time

# ✅ GOOD - Add delays between actions
driver.find_element(By.ID, "link1").click()
time.sleep(1)  # Human-like delay

driver.find_element(By.ID, "link2").click()
time.sleep(1)

# ✅ GOOD - Set user agent
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0...")

# ✅ GOOD - Respect robots.txt
# Check website's robots.txt before scraping
```

---

## 7) Use Headless for Production

```python
from selenium.webdriver.chrome.options import Options

# ✅ GOOD - Headless for servers/automation
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")  # For Linux servers

driver = webdriver.Chrome(options=options)
```

---

# QUICK REFERENCE CHEAT SHEET

## Essential Operations

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Navigate
driver.get("https://www.example.com")
driver.back()
driver.forward()
driver.refresh()

# Find elements
element = driver.find_element(By.ID, "id")
element = driver.find_element(By.NAME, "name")
element = driver.find_element(By.CLASS_NAME, "class")
element = driver.find_element(By.CSS_SELECTOR, "selector")
element = driver.find_element(By.XPATH, "//xpath")
elements = driver.find_elements(By.CLASS_NAME, "class")

# Interact
element.click()
element.send_keys("text")
element.send_keys(Keys.RETURN)
element.clear()

# Get info
text = element.text
value = element.get_attribute("value")
is_displayed = element.is_displayed()
is_enabled = element.is_enabled()
is_selected = element.is_selected()

# Dropdown
select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option")
select.select_by_value("value")
select.select_by_index(0)

# Wait
element = wait.until(EC.presence_of_element_located((By.ID, "id")))
element = wait.until(EC.element_to_be_clickable((By.ID, "button")))

# Windows/Tabs
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.default_content()

# Frames
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()

# Alerts
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()

# Screenshots
driver.save_screenshot("page.png")
element.screenshot("element.png")

# JavaScript
driver.execute_script("window.scrollTo(0, 500);")
result = driver.execute_script("return document.title;")

# Cleanup
driver.quit()
```

---

# WHAT YOU'VE MASTERED

After completing these notes, you can:

✅ Set up Selenium with automatic WebDriver management  
✅ Control browsers programmatically  
✅ Find elements using all locator strategies  
✅ Interact with forms, buttons, and inputs  
✅ Handle dropdowns, checkboxes, and radio buttons  
✅ Work with multiple windows and tabs  
✅ Manage frames and iframes  
✅ Handle alerts and popups  
✅ Implement proper waits and synchronization  
✅ Take screenshots and download files  
✅ Execute JavaScript in browser  
✅ Build complex automation workflows  
✅ Create production-ready web automation scripts  
✅ Scrape JavaScript-heavy websites  
✅ Automate login and form submission  

**You're ready to automate any web task!**

---

# PRACTICE EXERCISES

## Beginner Level

1. Open a website and take a screenshot
2. Fill a simple login form
3. Click through multiple pages and collect titles
4. Extract all links from a webpage
5. Download a file from a website

## Intermediate Level

1. Automate Google search and collect results
2. Fill multi-step forms with validation
3. Scrape product data from e-commerce site
4. Handle dynamic content loading
5. Create automated login bot

## Advanced Level

1. Build complete web scraper with pagination
2. Create form submission automation with error handling
3. Develop automated testing framework
4. Build monitoring system for website changes
5. Create data extraction pipeline with export to Excel

---

**End of Selenium Master Notes**

*Master browser automation, build powerful web bots!* 🤖