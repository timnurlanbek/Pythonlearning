# convert two lists into a dictionary

key = ["Ten", "Twenty", "Thirty","Forty"]
values = [10,20,30,40]


# if len(key) > len(values):
#     print("Ther are more values")
# else:
#     dict1 = {}
#     for i in range(len(key)):
#         dict1[key[i]] = values[i]
    
#     print(dict1)


# merge two dict into one

# dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}
# print(dict2)

# for key, value in dict1.items():
#     if key not in dict2:
#         dict2[key]=value
# print(dict2)


# for i in range(len(key)):
#     print(key)

hr = {"name": "Kelly",
     "age" : 25,
     "salary": 8000,
     "city": "New York"}

# extract keys "name" and " salary"

filter={}

for key, value in hr.items():
    if key == "name" or key == "salary":
        filter[key]=value
print(filter)

print("\n", hr)
# delete a list of keys from a dictionary
remove_keys =["name", "salary"]

for key in remove_keys:
    del hr[key]

print("\n",key)

print()
# rename a key of a dictionary
# rename a key "dicty to location"

hr["location"] = hr.pop("city")

print(hr)