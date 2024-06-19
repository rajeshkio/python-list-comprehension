# Filter a list of dictionaries by a specific key value.

people = [{'name': 'John', 'age': 28}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 28}]
filtered_people = []
for person in people:
    if person['age'] == 28:
        filtered_people.append(person)
print(filtered_people)

# Equivalent list comprehension

filtered_people_comp = [person for person in people if person['age'] == 28]
print(filtered_people_comp)