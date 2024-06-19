# Create a list of sums of corresponding elements from two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = []
print(list(zip(list1, list2)))
for x,y in zip(list1, list2):
    sum_list.append(x+y)
print(sum_list)

# Equivalent list comprehension

sum_list_comp = [x+y for x,y in zip(list1, list2)]
print(sum_list_comp)