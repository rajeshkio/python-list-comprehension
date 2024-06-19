# Filter out vowels from a string.

string = "hello world"

consonents = []
for char in string: 
    if char not in "aeiou" and char not in ' ':
        consonents.append(char)
print(consonents)

# Equivalent list comprehension

consonents_comp = [char for char in string if char not in "aeiou" and char not in ' ']
print(consonents_comp)