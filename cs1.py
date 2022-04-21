#controlled conditional loop

#for loop

# for item in range(0,10):
#     print(item)

# for tim in range(11,20):
#     print(tim)

# #deff range(start, stop, step) is a funtioin that takes at least one input or maximum three

# print()
# for t in range(50,100,49):
#     print(t)


# for item in range(30):
#   if item%7 == 0:
#     print(item)

# print()
# for item in range(0,30,7):
#     print(item)

# for t in range(30):
#     print(t)

# t = ''' Love
#         is ... '''

# print(t)    

# for t in range(10,0,-1):
#     print(t*"*")    

# height = int(input("enter height of triangle: "))
# for item in range(height,0,-1):
#     print(item*"*")

# from asyncore import loop
# from math import factorial


# for item in ([-10,-1]):     #solution for item in range(-10,-1):
#                                           #print( item)
#     print(item)




# num = int(input("enter a number less than 20: "))
# factorial = 1
# for i in range(1, num + 1): 
#  factorial = factorial * i
# print("factorial of ", num, " is ", factorial)



num=int(input("enter any number: "))
evens = 0
odds= 0
for i in range(num):
    if i %2==0:
        evens=evens+1
    else:
        odds=odds+1
print("number of evens: ",evens)
print("number of odd: ",odds)








# 2.17.22                                                                                     new day
 

# print("Python program to print squares of numbers")

# # take an input from the user
# num = int(input ("enter a numer: "))

# # use te absolute number 
# num = abs(num)

# #integer variable i to count from 0 to N(N+1 numbers)

# for i in range(0,num+1,1):
#     #for each i in the range
#     print(i**2)