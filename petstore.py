pet_supplies = []
pet_supplies.append("food")
pet_supplies.append("treats")
pet_supplies.insert(0,"toys")
pet_supplies.append("collars")
pet_supplies[1] = "pet tags"
pet_supplies.append("cages")
pet_supplies.append("aquariums")
pet_supplies.insert(2,"leashes")

print(pet_supplies,"\n")
print()
print()
del pet_supplies[3]
print("products=", pet_supplies,"\n")

print(pet_supplies.pop(), "item was popped out")
print(pet_supplies,"\n")

print(pet_supplies.pop(2), "item was popped out")
print(pet_supplies,"\n")

pet_supplies.remove("pet tags")
print(pet_supplies,"\n")

pet_supplies.sort()

for supply in pet_supplies:
    print(supply)
print()

pet_supplies.reverse()

for supply in pet_supplies:
    print(supply)
print()

for supply in pet_supplies[:2]:
    print(supply)