# Generate a list of Pythagorean triples (a, b, c) for a, b, c < 20.

triplets = []
for a in range(1, 21):
    for b in range(a, 21):
        for c in range(b, 21):
            if a**2 + b**2 == c**2:
                triplets.append((a,b,c))
print(triplets)

# Equivalent list comprehension

triplets_comp = [(a,b,c) for a in range(1,21) for b in range(a,21) for c in range(b,21) if a**2 + b**2 == c**2]
print(triplets_comp)