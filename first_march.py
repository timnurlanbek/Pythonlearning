# myString = "Hello Python"

# print(myString[0])
# print(myString[3])
# print(myString[2])
# print(myString[-1])
# length = len(myString)
# print(myString[length-1]) # >>>>>

# explanation
#-5-4-3-2-1 
# H e l l o     As you can see. Python counts from zero from 
# 0 1 2 3 4     the beginning, and from backward this counts
#               from minus one. EX:
# word = "hello"
# print(word[0])
# print(word[2])
# print(word[4])
# print()
# print(word[-1])
# print(word[-3])
# print(word[-5])

# asg = "python"
# asg [-1]
# asg [0]

# # string method 
# # print("a".isupper)

# string.islower()
# string.isdigit()
# string.isupper()

myText = "hello python"
# print(myText.isupper())
# print(myText.islower())
age = "23"
salary = "123k"
# print(myText.isupper())
# print(myText.islower())
# print(age.isdigit())
# print(salary.isdigit())
# print(age.isascii())

# anc youay eadray histay odecay?
# ifay yesay hentay hentay elltay y;)

my_lyric = "The sky is blue, sun is shiNing, I wrote this 2 years 34 days ago"


print(my_lyric)
tom = 0
lower = 0
digit = 0
for letter in my_lyric:
    if letter.isupper():
        tom=tom-1
    if letter.islower():
        lower+=1
    if letter.isdigit():
        digit+=1
print("Number of uppercases " + str(tom))
print("Number of lowercases " + str(lower))
print("Number of digits " + str(digit))    

# given a string of digits, write a code to get resersed version of digits,
# ex: a = "120Ab4s" expected output: b="4021"

# a = "120Ab4s"
# digits = 0
# for num in a:
#     if a.isdigit():

#         digits=digits+1
# print(num)      
#                      solution:::......:::::
# a = "120Ab4s"
# reversed_digits=""
# for letter in range(len(a)-1,-1,-1):
#     if a[letter].isdigit():
#         reversed_digits = reversed_digits+a[letter]
# print(reversed_digits)

# n = 1204
# rev = 0
 
# while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10

# print(rev)

# given a string of names, ask user to enter his her name, say this name exists if it is in string of 
# names, otherwise, as k if he or she watn to add, oif yes add, otherwise say goodbye
 
# database = "martin, clark, abi, james"

# name = input("enter ur name: ")
# print(name)
# if name in database:
#     print("You name exists in our database")
# else:
#     a=input("do you wanna add you name into our database system: ")
#     if a.lower() == "yes":
#         database=database+" ,"+name
#         print("your name is successfully added", database)
#     else:
#         print("Goodbye!")

# name= input("enter your nhjm,