Python Numbers: In-Depth Notes
1. Basic Numeric Types

Integers (int): Whole numbers, unlimited size in Python 3.

Example: x = 2, y = 3, z = 4
Operations: +, -, *, /, // (floor division), % (modulo), ** (exponentiation)
Example: x + y → 5, z ** 2 → 16, 2 ** 100 → 1267650600228229401496703205376


Floating-Point (float): Numbers with decimal points.

Example: result = 1/3.0 → 0.3333333333333333
Precision issues: 0.1 + 0.1 + 0.4 → 0.6000000000000001
Use decimal.Decimal for precise decimal arithmetic: Decimal('0.1') + Decimal('0.1') + Decimal('0.1') → 0.3


Complex Numbers: Numbers with real and imaginary parts.

Example: 2 + 1j, (2 + 1j) * 3 → (6+3j)



2. Numeric Operations

Arithmetic: +, -, *, /, //, %, **

Modulo: y % 2 → 1 (remainder of 3 ÷ 2)
Exponentiation: z ** 5 → 1024, 100 ** 2 → 10000


Comparison: <, >, <=, >=, ==, !=

Chained comparisons: x < y < z → True (2 < 3 < 4)
Logical combinations: x < y and y < z → True, 1 == 2 < 3 → False


Bitwise Operations (integers only):

Left shift: x << 2 → 4 (1 shifted left by 2 bits)
Bitwise OR: x | 2 → 3 (binary 1 | 10)



3. Number Base Representations

Octal: Prefix 0o, e.g., 0o20 → 16 (base 10)
Hexadecimal: Prefix 0x, e.g., 0xFF → 255
Binary: Prefix 0b, e.g., 0b1000 → 8
Conversions:
To string: oct(64) → '0o100', hex(64) → '0x40', bin(64) → '0b1000000'
From string: int('64', 8) → 52, int('64', 16) → 100



4. Math Module

Import: import math
Functions:
math.floor(x): Rounds down to nearest integer.
math.floor(3.5) → 3, math.floor(-3.5) → -4


math.trunc(x): Truncates to integer (removes decimal part).
math.trunc(2.8) → 2, math.trunc(-2.8) → -2





5. Random Numbers

Import: import random
Functions:
random.random(): Returns float between 0.0 and 1.0, e.g., 0.7867307242828568
random.randint(a, b): Returns random integer between a and b (inclusive), e.g., random.randint(1, 10) → 1 or 10
random.choice(sequence): Picks random element from sequence, e.g., random.choice(['lemon', 'masala', 'ginger', 'mint']) → 'ginger'
random.shuffle(sequence): Shuffles sequence in place, e.g., random.shuffle(l1) changes l1 order



6. Precise Arithmetic

Floating-Point Precision Issues:
Example: (0.1 + 0.1 + 0.1) - 0.3 → 5.551115123125783e-17


Solutions:
Use decimal.Decimal for precise decimal calculations.
Example: Decimal('0.1') + Decimal('0.1') + Decimal('0.1') → 0.3


Use fractions.Fraction for rational numbers.
Example: Fraction(2, 7) → Fraction(2, 7)





7. Sets and Numbers

Set Operations:
Intersection: setone & {1, 3} → {1, 3}
Union: setone | {1, 3, 7} → {1, 2, 3, 4, 7}
Difference: setone - {1, 2, 3, 4} → set()



8. Boolean and Number Interactions

Boolean as Numbers:
True == 1 → True, False == 0 → True
True + 4 → 5 (True treated as 1)
Note: Use == for comparison, not is with literals (True is 1 → False)



9. Type Checking

Use type() to check object type, e.g., type({}) → <class 'dict'>
Avoid errors: type() requires 1 or 3 arguments, e.g., type() raises TypeError

10. String Representations

repr(x): Returns string with quotes for strings, e.g., repr('chai') → "'chai'"
str(x): Returns string without quotes, e.g., str('chai') → 'chai'
print(x): Outputs string to console, e.g., print('chai') → chai

11. Common Pitfalls

Syntax Errors: Unclosed quotes or missing commas, e.g., repr('chai' → SyntaxError
Floating-Point Precision: Use Decimal or Fraction for critical calculations.
Boolean Comparisons: Avoid is with literals; use ==.

12. Best Practices

Use math module for advanced math operations.
Use decimal or fractions for precise calculations.
Leverage random for simulations and random selections.
Always validate input types to avoid TypeError or NameError.
