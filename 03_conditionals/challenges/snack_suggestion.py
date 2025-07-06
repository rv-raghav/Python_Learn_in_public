# A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order. Otherwise, it says it's not available.
# Task:
# - Take snack input
# - if its cookies or samosa, cnfm the order
# - else show unavailability

snack = input("Enter your preferred snack:").lower()
# print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve ypu {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")

# Restaurant Billing System
# You’re designing a billing system for a restaurant. Depending on the total bill amount entered by the customer, they might get a free dessert.



# Tasks:

# Ask the user to enter their total bill amount. Store it in a variable named bill_amount.

# If the bill amount is greater than 500, return the string "You get a free dessert!"

# Otherwise, return the string: "No free dessert this time."

bill_amount = input("Enter your bill amount")
if bill_amount > 500:
    print('You get a free dessert!')
else:
    print("No free dessert this time.")