# Filter out negative numbers from a list.

numbers = [5, -2, 9, -8, 4]

positiveNumbers = []
for num in numbers:
    if num >= 0:
        positiveNumbers.append(num)
print(positiveNumbers)


# Equivalent list comprehension

positiveNumbersComp = [num for num in numbers if num >= 0]
print(positiveNumbersComp)