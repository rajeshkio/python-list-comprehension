# Create a list of lengths of each word in a list.

words = ['hello', 'world', 'python']

word_length_list = []
for word in words:
    word_length_list.append(len(word))
print(word_length_list)

# Equivalent list comprehension

word_length_list_comp = [len(word) for word in words]
print(word_length_list_comp)