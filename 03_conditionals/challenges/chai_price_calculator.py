# A tea stall offers different prices for different cup sizes.Wap that calculates the price based on size.
# Task:
# input: "small","medium","large"
# small -> rs10, medium -> rs15, large -> rs20
# if invalid: show "unknown cup size"

cup = input("choose your cup size").lower()
if cup == "small":
    print("price is 10 rupees")
elif cup == "medium":
    print("price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("unknown cup size")

# Delivery Charge Calculator
# You’re building a delivery system for an e-commerce platform. Depending on the distance of the customer’s address, different delivery charges apply.

# Tasks:

# Take input from the user for delivery distance in Kilometers and store it in a variable named distance.

# If the distance is 2 km or less, return the string: "Delivery charge: 0"

# If the distance is greater than 2 km but not more than 5 km, return the string: "Delivery charge: 30"

# If the distance is greater than 5 km but not more than 10 km, return the string: "Delivery charge: 50"

# If the distance is more than 10 km, return the string: "Delivery not available for your location."

distance = input("enter distance")
if distance <= 2:
    print('Delivery charge: 0')
elif distance > 2 and distance <= 5:
    print("Delivery charge: 30")
elif distance > 5 and distance <= 10:
    print("Delivery charge: 50")
else:
    print("Delivery not available for your location.")