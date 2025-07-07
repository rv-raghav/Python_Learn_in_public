# The zip() function in Python is a built-in function that takes one or more iterables (like lists, tuples, or strings) as input and returns an iterator of tuples. Each tuple contains elements from the input iterables, paired together based on their corresponding positions. 
# Key characteristics of zip():
# Aggregates elements:
# It combines elements from multiple iterables into a single, new iterable. 
# Returns a zip object:
# The output of zip() is a zip object, which is an iterator. This means it generates tuples on demand, making it memory-efficient, especially for large datasets. 
# Pairs elements positionally:
# The first element of each input iterable is paired together, then the second elements, and so on. 
# Shortest iterable determines length:
# If the input iterables have different lengths, zip() stops when the shortest iterable is exhausted. Excess elements from longer iterables are ignored.
# Common uses of zip():
# Parallel iteration: Iterating over multiple lists or sequences simultaneously in a for loop.
# Combining lists into a dictionary: Pairing elements from two lists to form key-value pairs for a dictionary.
# "Unzipping" data: Using the * operator with zip() to separate elements back into individual iterables.
# Example:
# Python

# names = ["Alice", "Bob", "Charlie"]
# ages = [30, 25, 35]

# # Combine names and ages using zip()
# combined_data = list(zip(names, ages))
# print(combined_data)
# # Output: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# # Iterate in parallel
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# you're preparing an order summary with customer names and their total bills.
# task : 
# - use two lists : one for names and one for bills.
# - print "[Name] paid rs[amount]"

names =  ["raghav","archit","aryan"]
bills = [50, 70, 100]

for name,amount in zip(names,bills):
    print(f"name is {name} and bill is {amount}")