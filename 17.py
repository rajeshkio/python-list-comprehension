# Generate a list of all possible combinations of two lists.

list1 = [1, 2]
list2 = ['a', 'b']

combination_list = []
for i in list1:
    for j in list2:
        combination_list.append((i,j))
print(combination_list)

# Equivalent list comprehension

combination_list_comp = [(i,j) for i in list1 for j in list2]
print(combination_list_comp)