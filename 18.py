# Create a list of unique characters in a string.

string = "hello world"
unique_char =[]
for char in string:
    if char not in unique_char and char != ' ':
        unique_char.append(char)

print(unique_char)

# Equivalent list comprehension

unique_char_comp = []
[unique_char_comp.append(char)  for char in string if char not in unique_char_comp and char != ' ']
print(unique_char_comp)