# you want to simulate tea heating. it starts at 40 C and boils at 100 C. 
# Task : use a while loop - inc temp by 15 until it reaches or exceeds 100
# print each temp step

temperature = 40

while temperature < 100:
    print(f"Current temp {temperature}")
    # temperature = temperature + 15
    temperature += 15

print("tea is ready to boil")


# ✅ Use for loop when:
# You know in advance how many times you want to loop (typically over a sequence like list, string, or range).

# Examples:
# Loop over a list:

# python
# Copy
# Edit
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# Loop using a range (fixed number of times):

# python
# Copy
# Edit
# for i in range(5):
#     print(i)
# ✅ Use while loop when:
# You want to loop until a condition becomes false, but you don’t necessarily know how many times in advance.

# Examples:
# Loop until user types "exit":

# python
# Copy
# Edit
# user_input = ""
# while user_input != "exit":
#     user_input = input("Type something (or 'exit' to quit): ")
# Loop until a number becomes 0:

# python
# Copy
# Edit
# n = 5
# while n > 0:
#     print(n)
#     n -= 1
# 📌 Summary:
# Goal / Situation	Use for	Use while
# Iterating over a sequence (list, str)	✅ Yes	🚫 No (less ideal)
# Fixed number of repetitions	✅ Yes (range)	✅ Yes
# Looping until a condition is met	🚫 No	✅ Yes
# Infinite loop with condition to break	🚫 No	✅ Yes (while True)