# Transpose a matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for item in matrix:
        transposed_row.append(item[i])  
    transposed.append(transposed_row)
print(transposed)

# Equivalent list comprehension

transposed_comp = [ [item[i] for item in matrix] for i in range(len(matrix[0]))]
print(transposed_comp)