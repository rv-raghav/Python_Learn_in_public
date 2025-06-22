# Python Strings - Complete Guide

## 1. String Creation and Basic Operations

### Creating Strings
```python
# Single quotes
chai = 'Lemon Chai'

# Double quotes
chai = "Masala chai"

# Both are equivalent - use consistently in your code
```

### String Indexing
```python
chai = "Masala chai"

# Positive indexing (0-based)
first_char = chai[0]      # 'M'
second_char = chai[1]     # 'a'

# Negative indexing (from end)
last_char = chai[-1]      # 'i'
second_last = chai[-2]    # 'a'
```

## 2. String Slicing

### Basic Slicing Syntax: `string[start:end:step]`
```python
chai = "Masala chai"
num_list = "0123456789"

# Basic slicing
slice_chai = chai[0:6]    # 'Masala'
middle = chai[2:8]        # 'sala c'

# Omitting start/end
num_list[3:]              # '3456789' (from index 3 to end)
num_list[:7]              # '0123456' (from start to index 6)
num_list[:]               # '0123456789' (entire string)

# Step parameter
num_list[0:7:2]           # '0246' (every 2nd character)
num_list[0:7:3]           # '036' (every 3rd character)
num_list[::2]             # '02468' (every 2nd char in entire string)
num_list[::-1]            # '9876543210' (reverse string)
```

## 3. String Methods

### Case Manipulation
```python
chai = "Masala chai"

chai.lower()              # 'masala chai'
chai.upper()              # 'MASALA CHAI'
chai.capitalize()         # 'Masala chai'
chai.title()              # 'Masala Chai'
chai.swapcase()           # 'mASALA CHAI'
```

### Whitespace Handling
```python
chai = "   Masala chai  "

chai.strip()              # 'Masala chai' (removes leading/trailing whitespace)
chai.lstrip()             # 'Masala chai  ' (removes leading whitespace)
chai.rstrip()             # '   Masala chai' (removes trailing whitespace)
chai.strip('a ')          # 'Masala chai' (removes specific characters)
```

### String Replacement
```python
chai = "Lemon Chai"

chai.replace("Lemon", "Ginger")     # 'Ginger Chai'
chai.replace("a", "A")              # 'LemonChAi'
chai.replace("a", "A", 1)           # 'LemonChAi' (replace only first occurrence)

# Original string remains unchanged
print(chai)                         # 'Lemon Chai'
```

### String Splitting and Joining
```python
chai = "Lemon, Ginger, Masala, Mint"

# Splitting
chai.split()                        # ['Lemon,', 'Ginger,', 'Masala,', 'Mint'] (splits on whitespace)
chai.split(", ")                    # ['Lemon', 'Ginger', 'Masala', 'Mint'] (splits on specific delimiter)
chai.split(",")                     # ['Lemon', ' Ginger', ' Masala', ' Mint']

# Joining
chai_variety = ["Lemon", "Masala", "Ginger"]
"".join(chai_variety)               # 'LemonMasalaGinger'
" ".join(chai_variety)              # 'Lemon Masala Ginger'
"-".join(chai_variety)              # 'Lemon-Masala-Ginger'
", ".join(chai_variety)             # 'Lemon, Masala, Ginger'
```

### String Searching
```python
chai = "Masala Chai"

# Finding substrings
chai.find("Chai")                   # 7 (returns index of first occurrence)
chai.find("chai")                   # -1 (case-sensitive, not found)
chair.find("Tea")                   # -1 (not found)

# Advanced finding
chai.rfind("a")                     # 9 (rightmost occurrence of 'a')
chai.index("Chai")                  # 7 (like find, but raises exception if not found)

# Counting occurrences
chai = "Masala Chai Chai Chai"
chai.count("Chai")                  # 3
chai.count("a")                     # 4
```

### String Checking Methods
```python
chai = "Masala Chai"

# Content checks
chai.isalpha()                      # False (contains space)
chai.isdigit()                      # False
chai.isalnum()                      # False (contains space)
chai.isspace()                      # False

"123".isdigit()                     # True
"abc".isalpha()                     # True
"abc123".isalnum()                  # True

# Case checks
"MASALA".isupper()                  # True
"masala".islower()                  # True
"Masala".istitle()                  # True

# Start/End checks
chai.startswith("Masala")           # True
chai.startswith("masala")           # False (case-sensitive)
chai.endswith("Chai")               # True
chai.endswith("chai")               # False
```

## 4. String Formatting

### Old-style Formatting (%)
```python
name = "Masala"
quantity = 2

"I ordered %d cups of %s chai" % (quantity, name)
# 'I ordered 2 cups of Masala chai'
```

### str.format() Method
```python
chai_type = "Masala"
quantity = 2

# Positional arguments
order = 'I ordered {} cups of {} chai'
order.format(quantity, chai_type)   # 'I ordered 2 cups of Masala chai'

# Named arguments
order = 'I ordered {qty} cups of {type} chai'
order.format(qty=quantity, type=chai_type)

# Index-based
order = 'I ordered {0} cups of {1} chai'
order.format(quantity, chai_type)
```

### f-strings (Python 3.6+) - Recommended
```python
chai_type = "Masala"
quantity = 2
price = 3.50

f"I ordered {quantity} cups of {chai_type} chai"
# 'I ordered 2 cups of Masala chai'

f"Total cost: ${quantity * price:.2f}"
# 'Total cost: $7.00'

# Expressions inside f-strings
f"Chai type in uppercase: {chai_type.upper()}"
# 'Chai type in uppercase: MASALA'
```

## 5. String Length and Iteration

### Getting String Length
```python
chai = "Masala Chai"
len(chai)                           # 11 (includes space)
```

### Iterating Through Strings
```python
chai = "Masala Chai"

# Character by character
for letter in chai:
    print(letter)
# M
# a
# s
# a
# l
# a
#  
# C
# h
# a
# i

# With index
for i, letter in enumerate(chai):
    print(f"{i}: {letter}")
# 0: M
# 1: a
# 2: s
# ...
```

## 6. Escape Characters and Raw Strings

### Common Escape Characters
```python
# Newline
chai = "Masala\nChai"
print(chai)
# Masala
# Chai

# Tab
chai = "Masala\tChai"              # 'Masala    Chai'

# Quotes inside strings
chai = "He said, \"Masala chai is awesome\""
chai = 'He said, "Masala chai is awesome"'

# Backslash
path = "c:\\user\\pwd"             # 'c:\user\pwd' when printed
```

### Raw Strings
```python
# Raw strings treat backslashes literally
chai = r"Masala\nchai"             # 'Masala\\nchai'
print(chai)                        # Masala\nchai (no newline)

path = r"c:\user\pwd"              # Useful for file paths
regex = r"\d+\.\d+"                # Useful for regex patterns
```

## 7. String Membership and Comparison

### Membership Testing
```python
chai = "Masala Chai"

"Masala" in chai                   # True
"masala" in chai                   # False (case-sensitive)
"Tea" in chai                      # False
"Masala " in chai                  # True (exact match including space)

"Masala" not in chai               # False
```

### String Comparison
```python
chai1 = "Masala"
chai2 = "masala"
chai3 = "Masala"

chai1 == chai2                     # False (case-sensitive)
chai1 == chai3                     # True
chai1 != chai2                     # True

# Lexicographic comparison
"apple" < "banana"                 # True
"Apple" < "apple"                  # True (uppercase comes first in ASCII)
```

## 8. String Immutability

```python
chai = "Masala Chai"

# Strings are immutable - you cannot change them in place
# chai[0] = 'm'                    # This would raise TypeError

# Instead, create new strings
new_chai = 'm' + chai[1:]          # 'masala Chai'
new_chai = chai.replace('M', 'm')  # 'masala Chai'
```

## 9. Advanced String Operations

### String Alignment and Padding
```python
chai = "Masala"

chai.center(20)                    # '       Masala       '
chai.ljust(20)                     # 'Masala              '
chai.rjust(20)                     # '              Masala'
chai.zfill(10)                     # '0000Masala' (useful for numbers)
```

### String Encoding and Decoding
```python
chai = "Masala Chai"

# Encoding to bytes
chai_bytes = chai.encode('utf-8')   # b'Masala Chai'
chai_bytes = chai.encode('ascii')   # b'Masala Chai'

# Decoding from bytes
original = chai_bytes.decode('utf-8')  # 'Masala Chai'
```

## 10. Common String Patterns and Tips

### Converting Between Types
```python
# String to number
num_str = "123"
num = int(num_str)                 # 123
float_num = float("123.45")        # 123.45

# Number to string
str(123)                           # '123'
str(123.45)                        # '123.45'

# Boolean to string
str(True)                          # 'True'
```

### String Validation
```python
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

def is_phone_number(phone):
    return phone.replace("-", "").replace(" ", "").isdigit()
```

### Performance Tips
```python
# Use join() for multiple concatenations instead of += in loops
words = ["Masala", "Ginger", "Lemon", "Mint"]

# Inefficient
result = ""
for word in words:
    result += word + " "

# Efficient
result = " ".join(words)

# Use f-strings for formatting (Python 3.6+)
name = "Masala"
quantity = 2
message = f"I want {quantity} cups of {name} chai"  # Fastest and most readable
```

## Key Takeaways

1. **Strings are immutable** - operations return new strings
2. **Indexing starts at 0** - negative indices count from the end
3. **Slicing syntax**: `string[start:end:step]`
4. **Case matters** - most string operations are case-sensitive
5. **Use f-strings** for modern, readable string formatting
6. **Raw strings** (r"") are useful for paths and regex patterns
7. **join() is efficient** for combining multiple strings
8. **String methods don't modify** the original string - they return new ones

Remember to always check the Python documentation for the complete list of string methods and their parameters!