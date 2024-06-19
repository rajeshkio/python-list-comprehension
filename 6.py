# Flatten a 2D list into a 1D list.

matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sublist in matrix:
    for item in sublist:
        flat_list.append(item)

print(flat_list)

# Equivalent list comprehension

flat_list_comp = [item for sublist in matrix for item in sublist ]
print(flat_list_comp)
