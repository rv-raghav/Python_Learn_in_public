# you're building a ticket info system for a railwap app. Based on seat type, show its features.
# Task:
# input : sleeper ac general luxury
# match using match-case
# unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditoned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")

# Food Menu Selector
# You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.

# Tasks:

# Define a function get_item_price that takes a string input item.

# Use match-case to return the following based on the item name:

# "pizza" → "Price: 30 bucks"

# "burger" → "Price: 15 bucks"

# "pasta" → "Price: 20 bucks"

# "salad" → "Price: 10 bucks"

# Any other item → "Item not available"

# Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).

get_item_price = input("enter item u want to eat").lower()

match get_item_price:
    case 'pizza':
        print("Price: 30 bucks")
    case 'burger':
        print("Price: 15 bucks")
    case 'pasta':
        print("Price: 20 bucks")
    case 'salad':
        print("Price: 10 bucks")
    case _:
        print("Item not available")
