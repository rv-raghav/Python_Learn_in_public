# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of base tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving {milk_per_serving}")

total_tea_bags  = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"White tea bags per pot:{bags_per_pot}")

total_cardomom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardomom_pods % pods_per_cup
print(f"Left over pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"scaled flavour strength {powerful_flavour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000 # = 1000000000(readability (_))
print(f"tea leaves: {total_tea_leaves_harvested}")