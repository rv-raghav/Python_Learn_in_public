order_size = input("Enter order size: ")
extra_shot_input = input("Do you need an extra shot? (yes/no): ")

# Normalize input to lowercase and check
extra_shot = extra_shot_input.lower() == "yes"

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"  # Added space before 'coffee'

print("Order:", coffee)
