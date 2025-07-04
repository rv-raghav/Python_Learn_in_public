# Strings --> immutable sequences of characters
# core slicing indexing

chai_type = "Ginger Tea"
customer_name = "John Doe"

print(f"Order for {customer_name}: {chai_type} please.")

chai_description = "Aromatic and Bold"
print(f"first Word: {chai_description[0:8]}") # slicing from start to index 8
print(f"first Word: {chai_description[:8]}") # slicing from start to index 8
print(f"first Word: {chai_description[0:8:2]}") # slicing with step
print(f"last Word: {chai_description[12:]}") # slicing from index 12 to the end
print(f"last Word: {chai_description[::-1]}") # reverse the string

lable_text = "Chai SpÉcial"
ecodel_label = lable_text.encode('utf-8')
print(f"Original label: {lable_text}")
print(f"Encoded label: {ecodel_label}")
decoded_label = ecodel_label.decode('utf-8')

