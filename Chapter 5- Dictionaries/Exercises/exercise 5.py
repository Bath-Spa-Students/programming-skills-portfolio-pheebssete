# to make list later on
pets = []

# listing pets 
pet = {'animal type': 'Koi fish',
    'name': 'Lucky',
    'owner': 'Leo'}
pets.append(pet)

pet = {'animal type': 'Rottweiler',
    'name': 'Bruce',
    'owner': 'Aliyah',}
pets.append(pet)

pet = {'animal type': 'Ragdoll',
    'name': 'Sof',
    'owner': 'Alexene'}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")