from calendar import week
from hashlib import new


cow = "MASHa 234"
print(cow.center(64) + cow.capitalize())

cowCap = cow.capitalize()
cowCapCenter = cowCap.center(50)
print(cowCapCenter)

new_string = "I love oyu baby"
new_string.split()
print(new_string.split())
print(new_string.split(' ',1))
print(new_string.split('.'))
print(new_string.split(None,3))


# New lesson : DATA STRUCTURES - specilized format for orgonizing, processing, retrieving
# and storing data. In computer science or in programming data structure can be selected
# for using It with different algorithms or storing data

# In Python there are containers. Python is powerful when we work with containers of data
# which contain other data types and even containers.
# First containcer is LIST which is mutable ordered sequence of elements
# 
weeks = ["Monday", "tuesday" , "Wednesday", "Thirday", "Friday", "Saturday", "Sunday"]
print(weeks[-1]) 

print('Mon' in weeks, 'sat' not in weeks)

# lists mutable : strings not mutable

# These are useful functions for lists !!!      List methods !!!

#len() ; min() ; max(); sorted(); these are functions ::: ---- join.([]) append.([]) these are methods 
name = ["I love you", " You love me" , " we love you", "You love us"]
print(min(name))  # this ' function' shows minimum word in a list

print(max(name))  # and this on the contrary shows maximum words in a list by alphabet


numbers = [2,34,234,2342343,2423,2123,6546,34,3,44,3]
print(sorted(numbers))  # this one shows sorted numbers from little till the largest one
print(sorted(numbers, reverse = True)) # and this one is on the contrary 

# join, sorted and lists quiz
names = ["Tima", "Tmmy", "Tony", "Tim"]
print("#".join(sorted(names)))
names.append("Gulchapchap")
print(sorted(names))
#Data structures are containers that include different data types
# All data structures are data types

# New class
# Python provides another useful container, TUPLES- used to store related pieces of information
##### tuples are ordered immutable; lists are ordered mutable


# Data structures: SET- a data type for mutable unordered collections of unique elements
# They collect unique elementsThis is the one main use.
a = [1,2,2,3,3,3,4,4,4,4,5]
b = set(a)
b.add(6)
b.pop()
print(b)

a = [1,2,2,3,3,3,4,4,4,4,5]
c = set(a)
dep = len(a) - len(c)
print(dep)