````markdown
# 📘 Dictionaries in Python

## 🧱 Creating a Dictionary
```python
chai_types = {
    "Masala": "Spicy",
    "ginger": "Zesty",
    "Green": "Mild"
}
````

## 🔍 Accessing Elements

```python
print(chai_types["Masala"])        # Spicy
print(chai_types.get("Ginger"))    # None (case-sensitive)
print(chai_types.get("ginger"))    # Zesty
```

## ✏️ Updating Values

```python
chai_types["Green"] = "Fresh"
```

## 🔁 Looping Through Dictionary

```python
# Keys only
for chai in chai_types:
    print(chai)

# Keys and values
for chai in chai_types:
    print(chai, chai_types[chai])

# Using .items()
for key, value in chai_types.items():
    print(key, value)
```

## ✅ Check Key Existence

```python
if "Masala" in chai_types:
    print("I have masala chai")
```

## ➕ Adding New Key-Value Pair

```python
chai_types["Earl Grey"] = "Citrus"
```

## ➖ Removing Items

```python
chai_types.pop("ginger")         # Removes key 'ginger'
chai_types.popitem()             # Removes last inserted item
del chai_types["Green"]          # Deletes key 'Green'
```

## 📋 Copying Dictionary

```python
chai_types_copy = chai_types.copy()
```

---

## 🧭 Nested Dictionaries

```python
tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },
    "Tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}

# Access nested items
print(tea_shop["chai"])               # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])     # Zesty
```

---

## ⚙️ Dictionary Comprehension

```python
squared_num = {x: x**2 for x in range(6)}
print(squared_num)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 🧹 Clear Dictionary

```python
squared_num.clear()
```

---

## 🆕 Create Dictionary Using `fromkeys()`

```python
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
# Output: {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

new_dict = dict.fromkeys(keys, keys)
# Output:
# {
#   'Masala': ['Masala', 'Ginger', 'Lemon'],
#   'Ginger': ['Masala', 'Ginger', 'Lemon'],
#   'Lemon': ['Masala', 'Ginger', 'Lemon']
# }
```