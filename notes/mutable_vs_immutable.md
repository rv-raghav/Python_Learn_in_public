
# 🧠 Mutable vs Immutable in Python

---

## 🔑 Definitions

- **Immutable objects**: Cannot be changed after creation.
  - Examples: `int`, `float`, `str`, `tuple`, `bool`

- **Mutable objects**: Can be changed after creation.
  - Examples: `list`, `dict`, `set`, `bytearray`

---

## 🧪 Example with Immutable Type (`int`)

```python
>>> x = 10       # x points to int object 10
>>> y = x        # y points to the same object 10
>>> x
10
>>> y
10

>>> x = 15       # x now points to a new int object 15
>>> y
10              # y still points to the original 10
>>> x
15
```

### 🔍 Inner Working

- `int` is **immutable**, so changing `x` to 15 creates a **new object**.
- `y` remains pointing to the old object (10).

#### Memory Diagram:

```
Before:            After:

x ─▶ 10            x ─▶ 15
     ▲                 ▲
     │                 │
y ───┘             y ───┘
```

---

## 🧪 Example with Mutable Type (`list`)

```python
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
```

### 🔍 Inner Working

- Both `a` and `b` point to the **same list object**.
- Modifying `a` also affects `b`.

#### Memory Diagram:

```
a ──┬──▶ [1, 2, 3, 4]
    │
b ──┘
```

---

## 🛠 Best Practices

- Use **immutable** types when you need **data safety**.
- Use **mutable** types when you need to **modify shared data**.
- Use `copy()` or `deepcopy()` to avoid unwanted mutations when dealing with mutables.

```python
import copy
safe_copy = copy.deepcopy(original)
```

---

## 🧪 Check Object Identity

```python
>>> x = 10
>>> y = x
>>> x is y
True

>>> x = 15
>>> x is y
False
```

- `is` checks if two variables point to the **same object** in memory.

---