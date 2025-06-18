Python String Indexing and Slicing

Basic Indexing
Strings in Python are sequences of characters, and each character has an index. Indexing starts at 0 for the first character, and negative indices count from the end, with -1 being the last character.

Accessing a single character:
username = "raghavverma"
username[0]   # 'r' (first character)
username[-1]  # 'a' (last character)
username[-2]  # 'm' (second-to-last character)


Length of a string:Use len() to get the total number of characters.
len(username)  # 11




Slicing
Slicing extracts a substring using the syntax string[start:stop:step], where:

start: Index where the slice begins (inclusive).

stop: Index where the slice ends (exclusive).

step: Interval between characters (optional, defaults to 1).

Basic slicing:
username[1:3]    # 'ag' (characters from index 1 to 2)
username[2:6]    # 'ghav' (characters from index 2 to 5)
username[:5]     # 'ragha' (from start to index 4)
username[6:]     # 'verma' (from index 6 to end)


Using step:
username[::2]    # 'rgaem' (every second character)
username[::-1]   # 'amrevvahgar' (reverse the string)
username[1:8:2]  # 'ahv' (from index 1 to 7, every second character)




Advanced Indexing and Slicing
Advanced techniques leverage Python's flexible indexing for more complex operations.

Negative index slicing:Use negative indices to slice from the end.
username[-5:]    # 'verma' (last 5 characters)
username[-6:-1]  # 'vverm' (from sixth-to-last to second-to-last)


Combining positive and negative indices:
username[1:-1]   # 'aghavverm' (from index 1 to second-to-last)


Step with negative indices:
username[-1:-8:-2]  # 'amrv' (from last to eighth-to-last, every second character)


Empty slices:If the slice is invalid, an empty string is returned.
username[10:5]   # '' (empty, as start > stop with default step)
username[5:5]    # '' (empty, as start equals stop)




Practical Examples
Here are practical applications of indexing and slicing using the string "raghavverma".

Extract first name (assuming up to first 6 characters):
username[:6]  # 'ragha'


Extract last name (assuming last 5 characters):
username[-5:]  # 'verma'


Check for substring:
'verma' in username[6:]  # True


Create initials:
username[0] + username[6]  # 'rv' (first letter of first and last name)


Reverse substring:
username[1:6][::-1]  # 'ahgav' (reverse of 'ragha')




Error Handling
Indexing and slicing can raise errors if indices are out of bounds:

IndexError: Accessing an index beyond the string's length.username[20]  # IndexError: string index out of range


Slicing is safe: Out-of-bounds slices return empty strings or partial results.username[8:20]  # 'rma' (stops at end of string)




Tips and Best Practices

Use negative indices for quick access to the end of a string.
Leverage step for patterns like reversing or skipping characters.
Validate indices when writing robust code to avoid IndexError.
Combine slicing with string methods for powerful text manipulation:username[6:].upper()  # 'VERMA' (convert last name to uppercase)