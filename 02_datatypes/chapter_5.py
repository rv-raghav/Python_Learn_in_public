# real numbers
import sys
from fractions import Fraction
from decimal import Decimal
ideal_temp = 95.5
current_temp = 95.49

print(f"ideal temp {ideal_temp}")
print(f"current temp {current_temp}")
print(f"Differnce temp {ideal_temp - current_temp}")
print(sys.float_info)

# Write a Python program that performs the following operations and prints the results Addition, Subtraction, Multiplication, Division (float result), Floor Division (integer result), Modulus (remainder)

a = 10
b = 5
c = a + b
print(f"Addition {c}")

c = a - b
print(f"Subtraction {c}")

c = a * b
print(f"Multiplication {c}")

c = float(a / b)
print(f"Division(float) {c}")

c = a // b
print(f"Floor Division (integer) {c}")

c = a % b
print(f"Modulus {c}")

# Should You Go for a Walk?
# You’re deciding whether to go for a walk based on two real-life conditions:

# is_sunny = True

# have_umbrella = False

# Print the result of the following:

# Should you go for a walk if it’s sunny and you don’t need an umbrella?

# Should you go for a walk if it’s sunny or if you have an umbrella?

# Is it not sunny today?

# Do you not have an umbrella?

is_sunny = True
have_umbrella = False
print(f"{is_sunny and have_umbrella}")
print(f"{is_sunny or have_umbrella}")
print(f"{not is_sunny}")
print(f"{not have_umbrella}")