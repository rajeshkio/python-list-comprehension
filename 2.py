# Create a list of even numbers from 0 to 20.

even = []
for i in range(1,21):
    if i %2 == 0:
        even.append(i)
print(even)

# Equivalent list comprehension

evenComp = [i for i in range(1,21) if i % 2 ==0 ]
print(evenComp)