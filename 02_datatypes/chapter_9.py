# sets {}

essential_spices = {"cardamom","ginger", "cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices #union
print(all_spices)

common_spices = essential_spices & optional_spices # intersection
print(common_spices)

only_in_essential = essential_spices - optional_spices
print(only_in_essential)

print(f"is 'cloves in essential spices' {'cloves' in optional_spices}")

# Managing Store Inventory
# You’re managing product categories for a retail store. Your task is to identify:

# Which products are available in which branches

# What products are common

# What products are missing in each branch

# And which products should not be altered using frozenset

# Tasks:

# Create a set branch_a_products with the items: "bread", "milk", "butter", "jam"
branch_a_products = {"bread", "milk", "butter", "jam"}
# Create another set branch_b_products with the items: "bread", "cheese", "butter", "ketchup"
branch_b_products ={"bread", "cheese", "butter", "ketchup"}
# Print both sets.
print(branch_a_products)
print(branch_b_products)
# Find and print the union of both branches’ products.
both_branches = branch_a_products | branch_b_products
print(both_branches)
# Find and print the intersection of both branches’ products.
both_branches = branch_a_products & branch_b_products
print(both_branches)
# Find and print the products that are in branch_a_products but not in branch_b_products.
both_branches_common = branch_a_products - branch_b_products
print(both_branches_common)
# Check whether "ketchup" is available in branch_a_products and print the result.
print(f"{'ketchup' in branch_a_products}")
# Define a frozenset called essential_items with values: "milk", "bread", "ketchup".
essential_items = frozenset({"milk", "bread", "ketchup"})
# Print the frozenset.
print(essential_items)