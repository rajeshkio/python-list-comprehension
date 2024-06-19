# Generate a list of squares from 1 to 10.
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)

# Converting to list Comprehension
squaresComp = [i**2 for i in range(1,11)]
print(squaresComp)
