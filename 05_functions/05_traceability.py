# your shop adds a 10% VAT on every order. You want this to be consistent and traceable. Task: Write add_vat(price, vat_rate)
# use this to compute final prices for 3 orders

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"original: {price}, Final with VAT: {final_amount}")