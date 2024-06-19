# Create a list of the first letters of each word in a list.

words = ['apple', 'banana', 'cherry']

firstLetters = []
for word in words:
    firstLetters.append(word[0])

print(firstLetters)


# Equivalent list comprehension

firstLettersComp = [word[0] for word in words]
print(firstLettersComp)