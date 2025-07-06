# you run an online tea store. if the order amount is more than 300rs, delivery is free; otherwise, it costs 30rs.
#Task:
# input order_amount
# use ternary operator to decide delivery fee

order_amount = int(input("Enter Order Amount:"))
print(f"Order Amount: {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 30
print(delivery_fees)

# Age Verification System
# You’re building a system to verify user age for access.



# Tasks:

# Define a function verify_age that accepts a string input named age_str.
# Convert age_str to an integer using int().
verify_age = input("Enter age")
age = int(verify_age)
# Use a ternary operator to return:
print("Access Granted" if age >=18 else "Access Denied")
# "Access Granted" if age is 18 or older

# "Access Denied" otherwise