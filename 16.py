# Flatten a list of lists of varying lengths.
nested_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]

flat_list = []
for list in nested_list:
    for item in list:
        flat_list.append(item)
print(flat_list)

# Equivalent list comprehension

flat_list_comp = [item for list in nested_list for item in list]
print(flat_list_comp)