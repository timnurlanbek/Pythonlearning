pet_supplies = {}

# dictionary = {key   :    value}
# products   = {product:   quantity}

pet_supplies["food"    ] = 40
pet_supplies["treats"  ] = 20
pet_supplies["toys"    ] = 30
pet_supplies["collars" ] = 12
pet_supplies["pet tags"] = 15
pet_supplies["cages"   ] = 20
pet_supplies["aquariums"]= 50
print(pet_supplies)

pet_supplies["cages"] += 10
pet_supplies["food" ] -= 4
print("Food:", pet_supplies.get("food"))





for supply, quantity in pet_supplies.items():
    print("Quantity:", quantity, ", Products:", supply)
print()

for supply in pet_supplies.keys():
    print("Quantity:", pet_supplies[supply],", Product", supply)
print()




for quantity in pet_supplies.values():
    print("Quantity:", quantity)
print()

for quantity in set(pet_supplies.values()):
    print("Quantity:", quantity)