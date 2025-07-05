# tuples --> () they are immutable
masala_spices = ("caradamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices 

print(f"Main masala spices: {spice1}, {spice2},{spice3}")

ginger_ratio, cardamom_ratio = 2,1
print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}")
ginger_ratio,cardamom_ratio = cardamom_ratio,ginger_ratio
print(f"Ratio is G:{ginger_ratio} and C: {cardamom_ratio}")

# membership

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")

# Swapping Temperature
# You are building a temperature converter app. Sometimes, due to incorrect input order, the min_temp and max_temp values are swapped.

# Current values are

# min_temp = 40

# max_temp = 25

# Use Python tuples to swap them back to the correct order.

min_temp, max_temp = 40, 25
min_temp, max_temp = 25, 40
print(min_temp)
print(max_temp)