# convert two lists into a dictionary

from ctypes.wintypes import WORD


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

# hr = {"name   

# extract keys "name" and " salary"

# filter={}

# for key, value in hr.items():
#     if key == "name" or key == "salary":
#         filter[key]=value
# print(filter)

# print("\n", hr)
# # delete a list of keys from a dictionary
# remove_keys =["name", "salary"]

# for key in remove_keys:
#     del hr[key]

# print("\n",key)

# print()
# rename a key of a dictionary
# rename a key "dicty to location"

# hr["location"] = hr.pop("city")

# print(hr)

# for i in range(len(key)):



# lrn_dict = {}
# lrn_dict["Name"]= "Temirbek"
# lrn_dict["Age"]=20
# lrn_dict["height"]=6,1
# print(lrn_dict)


# info_friend = {
#     "Name":"Avazbek",
#     "last_name":"Kandyboev",
#     "age":20,
#     "city":"Moskva"}
# print(info_friend) 

glossary = {
    "sorted()":"sorts all key or values in dict",
    "items()":"this is referred both key and values",
    "set":"chooes unique values or keys",
    }

glossary["pop"]="this deletes values"

print(glossary)


poll_takers = {
    "ryyan":"python",
    "jamila":"c++",
    "kerven":"",
    "daniiar":"",
    "Nuri":"",
}
for ke,val in poll_takers.items():
    if val=="":
        print("Please take our poll first "+ke)
    else:
        print("Thank you for responding "+ke)
