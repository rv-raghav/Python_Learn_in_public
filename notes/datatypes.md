Python Object Types / Data Types
A comprehensive guide to Python's built-in and advanced data types, including examples and key characteristics.

Numeric Types
Numeric types represent numbers in various forms, including integers, floating-point numbers, and complex numbers.

Integer: Whole numbers without a decimal point.1234, -56, 0b111  # Decimal, negative, binary


Float: Numbers with decimal points or in scientific notation.3.1415, 1.2e-10  # Regular float, scientific notation


Complex: Numbers with real and imaginary parts.3+4j, complex(2, -3)  # Complex number


Decimal: Fixed-precision decimal numbers for precise arithmetic.from decimal import Decimal
Decimal('0.1') + Decimal('0.2')  # Precise: 0.3


Fraction: Rational numbers as numerator/denominator pairs.from fractions import Fraction
Fraction(1, 3)  # Represents 1/3




Sequence Types
Sequences are ordered collections of items, supporting indexing and slicing.

String: Immutable sequence of characters, enclosed in single, double, or triple quotes.'spam', "Bob's", '''multiline''', b'a\x01c'  # Unicode, raw bytes


List: Mutable, ordered collection of items, enclosed in square brackets.[1, [2, 'three'], 4.5], list(range(10))  # Nested, range conversion


Tuple: Immutable, ordered collection of items, enclosed in parentheses.(1, 'spam', 4, 'U'), tuple('spam'), namedtuple('Point', ['x', 'y'])(10, 20)




Mapping Types
Mappings store key-value pairs, allowing efficient lookup by key.

Dictionary: Mutable collection of key-value pairs, enclosed in curly braces.{'food': 'spam', 'taste': 'yum'}, dict(hours=10)




Set Types
Sets are unordered collections of unique, immutable objects.

Set: Mutable collection of unique items.set('abc'), {'a', 'b', 'c'}


Frozenset: Immutable version of a set.frozenset('abc')




File Types
File objects represent open files for reading or writing data.

File: Interface for file operations, created using open().open('eggs.txt', 'r'), open(r'C:\ham.bin', 'wb')  # Text read, binary write




Boolean and None Types
Special types for logical values and absence of value.

Boolean: Represents truth values.True, False


None: Represents the absence of a value or null.None




Callable Types
Objects that can be invoked, such as functions and classes.

Function: Reusable block of code defined with def or lambda.def add(x, y): return x + y
lambda x: x * 2


Module: File containing Python code, imported using import.import math
math.sqrt(16)  # 4.0


Class: Blueprint for creating objects, defined with class.class Person:
    def __init__(self, name):
        self.name = name




Advanced Types and Concepts
Specialized constructs for advanced programming patterns.

Decorators: Functions that modify the behavior of other functions or methods.def my_decorator(func):
    def wrapper(): print("Decorated!"); func()
    return wrapper
@my_decorator
def say_hello(): print("Hello!")


Generators: Functions that yield values one at a time, defined with yield.def my_gen(): yield 1; yield 2; yield 3


Iterators: Objects with __next__ and __iter__ methods for iteration.iter([1, 2, 3])  # Returns iterator


Metaprogramming: Code that manipulates code, e.g., using type or metaclasses.MyClass = type('MyClass', (), {'x': 1})




Key Characteristics



Type
Mutable
Ordered
Example Usage



Integer
No
N/A
Arithmetic operations


String
No
Yes
Text processing


List
Yes
Yes
Dynamic collections


Dictionary
Yes
No
Key-value storage


Set
Yes
No
Unique item collection


File
N/A
N/A
File I/O


Boolean
No
N/A
Logical operations


Function
N/A
N/A
Reusable code blocks