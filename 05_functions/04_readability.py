# you sell different chai sizes.
# instead of writing formulas everywhere, create a function.
# task: write calculate_bill(cups, price_per_cup)
# return total bill
# use this function for multiple orders

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3,15)
print(my_bill)

print("order for table 2:", calculate_bill(2, 50))