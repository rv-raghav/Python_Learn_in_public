#walrus operator :=

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"not divisible, remainder is {remainder}")

value = 13
if remainder := value % 5:
    print(f'not divisible, remainder is {remainder}')

available_sizes = ["small","medium","large"]

if (requested_sizes := input("enter your chai cup size: ")) in available_sizes:
    print(f"serving {requested_sizes} chai")
else:
    print(f"size is unavailable - {requested_sizes}")


flavours = ["masala", "ginger", "lemon", "mint"]
print("available flavours: ", flavours)

while (flavor := input("choose your flavour: ")) not in flavours:
    print(f"sorry {flavor} is not available")
print(f"you choose {flavor} chai")