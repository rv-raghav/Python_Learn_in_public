#some chai flavors are put of stock. You want to skip those and stop entirely if someone requests a restricted flavor. 
# Task: Skip if flavour is "out of stock"
# - break if flavor is "discontinued"

flavours = ['ginger', 'Out of stock','lemon', "discontinued","tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print(f"out of loop")
