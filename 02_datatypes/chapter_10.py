# dictionary
chai_order = dict(type="Masala chai", size = "large",sugar = 2)
print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(chai_recipe['base'])
print(chai_recipe)
del chai_recipe["liquid"]
print(chai_recipe)

chai_order = dict(type="Masala chai", size = "large",sugar = 2)
print(chai_order.keys())
print(chai_order.values())
print(chai_order.items())

last_item = chai_order.popitem()
print(last_item)

# Customer Profile Management
# You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.

# Tasks:

# Create a dictionary named customer with the following fields:

# "name": "John Doe"

# "age": 32

# "city": "New York"
customer = {"name": "John Doe", "age": 32, "city": "New York"}
# Print the dictionary.
print(customer)
# Add "email" and "phone" to the dictionary.
new_info = dict(customer, email ='john.doe@example.com', phone = 123-456-7890)
# Print the updated dictionary.
print(new_info)
# Print the customer’s "name" and "city" values.
print(customer['name'],customer['city'])
# Check whether the key "email" exists in the dictionary and print the result.
print(f"{'email' in new_info}")
# Delete the "age" field from the dictionary.
del new_info["age"]
# Print the updated dictionary.
print(new_info)

# Print all dictionary keys, values, and items.
print(new_info.keys)
print(new_info.values)
print(new_info.items)


# Remove and print the last inserted key-value pair.
new_info.popitem()
print(new_info)
# Use .get() to access the key "membership" (which doesn’t exist).
membership_status = new_info.get("college")
# Print the result.
print(membership_status)
# Update the dictionary with a new field "address" set to "221B Baker Street".
new_info.update({'address': "221B Baker  Street"})
# Print the final dictionary.
print(new_info)