````markdown
# 📘 Tuples in Python

## 📦 What is a Tuple?

- A tuple is an **ordered**, **immutable** collection of elements.
- Defined using **parentheses `()`**.

---

## ✅ Creating a Tuple
```python
tea_types = ("Black", "Green", "Oolong")
````

## 🔍 Accessing Elements

```python
print(tea_types[0])     # Output: 'Black'
```

> ❗ **Note:** Using `()` like a function call (e.g., `tea_types(0)`) raises an error. Use square brackets `[]` to access elements.

---

## 🚫 Immutability

```python
tea_types[0] = "Lemon"   # ❌ Raises TypeError
```

> Tuples **cannot be changed** after creation — elements cannot be reassigned.

---

## 📏 Tuple Length

```python
len(tea_types)           # Output: 3
```

---

## ➕ Concatenating Tuples

```python
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)
# Output: ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
```

---

## ✅ Membership Test

```python
if "Green" in all_tea:
    print("I have green tea")
```

---

## 🔢 Count Occurrence

```python
more_tea.count("Herbal")   # Output: 1
```

---

## 📦 Tuple Unpacking

```python
(black, green, oolong) = tea_types

print(black)   # Output: 'Black'
print(green)   # Output: 'Green'
```

> ✅ Tuple unpacking allows assigning elements to individual variables.

---

## 🧾 Check Type

```python
type(tea_types)   # Output: <class 'tuple'>
```

---

## 🔐 Summary

| Operation        | Tuple                  |
| ---------------- | ---------------------- |
| Mutable?         | ❌ No                   |
| Indexed?         | ✅ Yes                  |
| Ordered?         | ✅ Yes                  |
| Duplicate items? | ✅ Yes                  |
| Methods          | `.count()`, `.index()` |
| Defined using    | `()`                   |

---

Use tuples when you want to:

* Ensure data integrity (no changes)
* Group related values (like coordinates, settings, etc.)

```
