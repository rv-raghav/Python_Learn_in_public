# Object & Mutability 
# Everything in python is an object
# object -> unique id, unique type, value
# mutable -> that is changeable 
# immutable -> that is not changeable
# to find if an object is immutable or mutable always use id and not value
sugar_amount = 2
print(f"Initial sugar; {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar; {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# now in this example sugar_amount -> the reference changes 

# >>> x = 10       # x points to int object 10
# >>> y = x        # y points to the same object 10
# >>> x
# 10
# >>> y
# 10
# >>> x = 15       # x now points to a new int object 15
# >>> y
# 10              # y still points to the original 10

#### Memory Diagram:

# Before:            After:

#x ─▶ 10            x ─▶ 15
#     ▲                 ▲
#     │                 │
#y ───┘             y ───┘

## 🧪 Example with Mutable Type (`list`)

# ```python
# >>> a = [1, 2, 3]
# >>> b = a
# >>> a.append(4)
# >>> a
# [1, 2, 3, 4]
# >>> b
# [1, 2, 3, 4]
# ```

### 🔍 Inner Working

# - Both `a` and `b` point to the **same list object**.
# - Modifying `a` also affects `b`.

#### Memory Diagram:

# a ──┬──▶ [1, 2, 3, 4]
#     │
# b ──┘