# Generate a list of prime numbers up to 50.

prime_numbers = []
for num in range(2,51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)

# Equivalent list comprehension

prime_numbers_comp = [num for num in range(2,51) if all(num % i != 0 for i in range(2,num)) ]
print(prime_numbers_comp)