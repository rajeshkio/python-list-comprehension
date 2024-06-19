# Create a list of numbers divisible by both 2 and 3 up to 30.

divisible_by_two_three = []
for i in range(1,31):
    if i % 2 ==0 and i % 3 == 0:
        divisible_by_two_three.append(i)

print(divisible_by_two_three)

# Equivalent list comprehension

divisible_by_two_three_comp = [i for i in range(1,31) if i % 2 ==0 and i % 3 == 0]
print(divisible_by_two_three_comp)