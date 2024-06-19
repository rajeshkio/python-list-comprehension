# Generate a list of reversed words from a list.

words = ['hello', 'world', 'python']
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(reversed_words)


# Equivalent list comprehension

reversed_words_comp = [word[::-1] for word in words]
print(reversed_words_comp)

