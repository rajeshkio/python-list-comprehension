# Create a list of dictionaries with keys 'number' and 'square' with range from 1,6
squares= []
for i in range(1,6):
    squares.append({'number':i, 'square': i**2})
print(squares)

# Equivalent list comprehension

squares_comp = [{'number':i, 'square': i**2} for i in range(1,6) ]
print(squares_comp)