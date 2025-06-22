# 📝 Lists in Python

## ✅ Creating a List

```python
tea_varities = ["Black", "Green", "Oolong", "White"]
```

## 📤 Accessing Elements

```python
print(tea_varities)         # ['Black', 'Green', 'Oolong', 'White']
print(tea_varities[-1])     # White
print(tea_varities[1:3])    # ['Green', 'Oolong']
print(tea_varities[:2])     # ['Black', 'Green']
print(tea_varities[2:])     # ['Oolong', 'White']
print(tea_varities[3])      # White
```

## ✏️ Modifying Elements

```python
tea_varities[3] = "Herbal"
print(tea_varities)         # ['Black', 'Green', 'Oolong', 'Herbal']
```

## ✨ Slice Assignment

```python
tea_varities[1:2] = ['Lemon']  # Replace 'Green' with 'Lemon'
tea_varities[1:2] = ["test", "test"]  # Insert two elements
```

## 🔁 Looping Through a List

```python
for tea in tea_varities:
    print(tea)

# or with separator
for tea in tea_varities:
    print(tea, end="-")
```

## 🔍 Membership Test

```python
if "Oolong" in tea_varities:
    print("I have")

if "masala" in tea_varities:
    print("I have")
```

## ➕ Adding and ➖ Removing Items

```python
tea_varities.append("masala")     # Adds to end
tea_varities.pop()                # Removes last item
tea_varities.remove("Black")      # Removes first match
tea_varities.insert(1, "green")   # Inserts at index
```

## 🪞 Copying a List

```python
tea_varities_copy = tea_varities.copy()
```

Modifying `tea_varities_copy` doesn't affect `tea_varities`.

---

## 🧠 List Comprehension

```python
squared_nums = [x**2 for x in range(10)]
print(squared_nums)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```