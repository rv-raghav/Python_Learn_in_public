
# Working with Python in Shell (Windows, Linux, macOS)

---

## 🔰 Detecting the Right Python Command

| OS        | Common Python Commands |
|-----------|------------------------|
| Windows   | `python`               |
| Linux     | `python3`              |
| macOS     | `python3`              |

> ✅ Use `python3` to avoid version conflicts, especially on Unix-based systems.

---

## ✅ Checking Python Installation

```bash
python --version     # On Windows
python3 --version    # On Linux/macOS
```

### 🛠 If command not found:

- On **Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install python3
  ```

- On **macOS**:
  ```bash
  brew install python
  ```

---

## 🚀 Running Python in Interactive Mode (REPL)

```bash
python       # Windows
python3      # Linux/macOS
```

Use `Ctrl+D` (Linux/macOS) or `Ctrl+Z` then `Enter` (Windows) to exit.

---

## 📂 Current Working Directory

```python
import os
os.getcwd()
```

To change directory:

```python
os.chdir('/path/to/dir')
```

---

## 🔁 Example Loop in Shell

```python
for c in "chai":
    print(c)
```

> ⚠️ Must **indent** after `for`, `if`, `def`, etc.

---

## 📦 Importing Your Own Modules

### 1. Your file: `hello_python.py`

```python
print("chai aur python")
chai_one = "lemon tea"

def chai(name):
    print(name)
```

### 2. Import in REPL or script:

```python
import hello_python
hello_python.chai("mint tea")
print(hello_python.chai_one)
```

### 3. Reload after editing:

```python
from importlib import reload
reload(hello_python)
```

> 🧠 Python only loads a module once per session unless reloaded.

---

## 🐍 Common Errors

- `ModuleNotFoundError`: File not in same directory or not found in `sys.path`.
- `AttributeError`: Function or variable doesn’t exist in the module.
- `IndentationError`: Forgetting indentation after `for`, `if`, `def`, etc.

---

## 🧭 Fixing Module Path Issues

Check:

```python
import sys
print(sys.path)
```

If needed:

```python
sys.path.append('/path/to/your/module')
```

---

## 🔄 Exit Python Shell

- Linux/macOS: `Ctrl + D`
- Windows: `Ctrl + Z` then `Enter`