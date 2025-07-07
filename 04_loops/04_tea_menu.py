# The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This object can then be used directly in for loops or converted into other data structures like a list of tuples. 
# Key features and usage:
# Adds a counter to an iterable:
# enumerate() takes an iterable (like a list, tuple, string, etc.) and pairs each item with a corresponding index.
# Returns an enumerate object:
# This object is an iterator that yields tuples of (index, value) for each item in the iterable. 
# Simplifies index tracking in loops:
# Instead of manually managing an index variable in a for loop, enumerate() provides a cleaner and more efficient way to access both the item and its index.
# Customizable starting index:
# By default, enumerate() starts counting from 0, but you can specify a different starting index using the start parameter.
# Syntax:
# Python

# enumerate(iterable, start=0)
# Example:
# Python

# my_list = ['apple', 'banana', 'cherry']

# for index, value in enumerate(my_list):
#     print(f"Index: {index}, Value: {value}")

# # Example with custom start index
# for index, value in enumerate(my_list, start=1):
#     print(f"Item {index}: {value}")

# you're creating a tea menu board
# each item must be numbered
# task: use enumerate() to print menu items with number.

menu = ["green", "lemon", "spiced", "mint"]
# for m in menu:
#     print(f"menu items is {m}")

# using enumerate
for idx, item in enumerate(menu, start = 1): # idx is index basically a variable start = 1 for number
    print(f"{idx} : {item} chai")