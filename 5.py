# Create a list of tuples (number, square) for numbers from 1 to 5.

tupleList = []
for i in range(1,6):
    tupleList.append((i, i**2))
print(tupleList)

# Equivalent list comprehension

tupleListComp = [ (i, i**2) for i in range(1,6)]
print(tupleListComp)