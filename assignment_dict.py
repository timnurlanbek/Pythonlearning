from subprocess import list2cmdline
from tkinter import N
from typing import Counter


dictionaries = {}
dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dictionaries [1] = 10
dictionaries [2] = 20
dictionaries [3] = 30
dictionaries [4] = 40
dictionaries [5] = 50
dictionaries [6] = 60
print("first method. Output is", dictionaries) # hard way

for dictionary in dic1,dic2,dic3:                # easy way
    dictionaries = dictionaries
print("Second method. Result is",dictionaries)

print()
print()


                                                              # Second problem
n = int(input("Enter a number: "))
d = dict()
for x in range (1,n+1):
    d[x] = x*x
print(d)

print()
print()


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict = Counter(d1) + Counter(d2)
print(dict)


print()
print()


list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_value = set( val for dic in list for val in dic.values())
print("Unique Values: ",unique_value)




