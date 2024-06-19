# Create a list of tuples (x, y) where x is a number from 0 to 4 and y is the square of x.

tuple_list = []
for i in range(5):
    squared_numnber = i ** 2
    tuple_list.append((i, squared_numnber))
print(tuple_list)

# Equivalent list comprehension

tuple_list_comp = [ (num, num**2) for num in range(5)]
print(tuple_list_comp)