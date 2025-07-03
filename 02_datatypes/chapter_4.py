# boolean

is_boiling = True # true = 1
stir_count = 5
total_actions = stir_count + is_boiling #upcasting
print(f"Total actions:{total_actions}")

milk_present = 0
print(f"Is there milk? {bool(milk_present)}")

# logical operation (and, or, not)
# tea or coffee (any one can be true)
# tea and cookies (both should be true)

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")