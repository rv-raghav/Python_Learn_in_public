# List -> [] mutable

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"maximum sugar level {max(sugar_levels)}")
print(f"minimum sugar level {min(sugar_levels)}")

#operator overloading

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(full_liquid_mix)

strong_brew = ['black tea','water'] * 3
print(strong_brew)

raw_spice_data = bytearray(b"CINNAMON") # bytearray is mutable ,what is bytearray? 
# bytearray is a mutable sequence of bytes, allowing for modification of its contents.
raw_spice_data[0] = 99  # Changing 'C' to 'c' (99 means 'c' in ASCII)
raw_spice_data[1] = 105  # Changing 'I' to 'i'
print(f"{raw_spice_data}")

# Shopping List
# You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

# Tasks:

# Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"
my_cart = ["apples", "bananas","milk"]
# Print the grocery list.
print(f"My grocery list: {my_cart}")
# Add "bread" to the end of the list.
my_cart.append("bread")
# Print the updated grocery list.
print(my_cart)
# Insert "ketchup" at the beginning of the list.
my_cart.insert(0,"ketchup")
# Print the updated grocery list.
print(my_cart)
# Remove "bananas" from the list.
my_cart.remove("bananas")
# Print the updated grocery list.
print(my_cart)
# Remove the last item from the list and store it in a variable named removed_item.
removed_item = my_cart.pop()
# Print the value of removed_item.
print(removed_item)
# Extend the grocery list by adding "rice" and "butter".
my_cart.extend("rice","butter")
# Print the updated grocery list.
print(my_cart)
# Sort the grocery list in alphabetical order.
my_cart.sort()
# Print the updated grocery list.
print(my_cart)
# Reverse the order of the grocery list.
my_cart.reverse()
# Print the updated grocery list.
print(my_cart)
# Concatenate the grocery list with another list containing "juice" and "jam".
another_list = ["juice","jam"]
concatenate = my_cart + another_list
# Print the resulting list.
print(concatenate)
# Duplicate the grocery list twice.
duplicated = concatenate *  2
# Print the resulting list.
print(duplicated)
# Define a string with the value "tomato cucumber spinach" and convert it into a list.
my_list = "tomato cucumber spinach"
new_list = bytearray(b"my_list")
# Print the converted list.
print(new_list)