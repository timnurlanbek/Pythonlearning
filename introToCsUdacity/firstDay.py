from time import time
from tokenize import Exponent


print("Hello Slave!")

# Exponentiation is ... ?
# We can raise one number to the power another number with 2 asterisks fx:
print(2**3,3**5,2**2,5**3 ," As you see power of a number is performed in this way!")
# One more thing is do not mix exponantiations with the "caret= ^" this is different!

# another useful operator is 'percent sign = % ' which performs the modulo operation.
# for example if we divide 10 to 3 result should be 3.33... with the remainder one and in order to get of
#-this division we put percent sign. Let's perform it
print(10%3)

# Two forward slashes = rounds the answer down or up instead of giving the exact answer!
print(10//3,11//3,234//3)
print()
print("average payment...")
#expression that calculates the average of numbers: for example:
# my first month bill was 24$, second 42$, third 63$. what is average monthly electricity bill:
# illustration:

print((24+42+63)/3)  #this will show the average monthly payment.

# when we write variables this does not matter if we write in width or in height:...
x,y,z= "tim", "tony" , "temirbek"
x='tim'
y = 'tony'
z='temirbek'
print(z)

#instead of writing mv_mountain twice we can write += and in this way this is easier.
mv_mountain = 34123
mv_mountain *= 2
print(mv_mountain)

#next lesson is integers and floats 
print(float(3/6))
print(int(3/6))

#                                       new day 
# TOPIC "strings"      We can define strings with double quote or single quote marks
#and when we have quotation marks in our string, we must be careful, because this is
#a little bit tricky. Illustratin...:
string_1 = "this is a string"
string_2 = 'this is also a string'
# if we want to add quotation mark in our string which consist of quotation marks. We
#use backslash and single quote to the word which is in quotation mark.
thisIsString = 'He said \'I love you\''
print(thisIsString)    #He said 'I love you'      # One more useful infomation. Awesome!
# also we can multiply words 
print(thisIsString*3)  #He said 'I love you'He said 'I love you'He said 'I love you'
print(thisIsString+ "Sh " + string_2)
#also we can index to the strings with [this one] and know how many spaces in strings
# with len() function
print(len(thisIsString))
thisIsString[0]

first_name = "Temirbek"
last_name = "Nurlanbekuulu"
family_name = "Nurlanbekov"
#todo: How many words do we have in whole name including spaces between them.

Whole_name = len(first_name + last_name + family_name) + 2
print("Whole name consists of", Whole_name ,"words including spaces")

# until now We have discussed four DATA TYPES 1) int: 2)float: 3)bool: 4)str:

house_number = 928
street_name = "Fountain Lake"
city_name = "Stafford"
address = str(house_number) + " at " + street_name + " in " + city_name
print(address)

# Lets write the name of the place where you live.
apartment_num = 164
name_of_the_house = "Uy"
street_name = "Gazybekov"
city_name = "Khalmion"
state = "Batken"
country_name = "kyrgyzstan"

address = "#" + str(apartment_num)+" at "+name_of_the_house+" "+street_name+" in "+city_name+", "+state+" in the "+ country_name
print(address)

# End of the lesson. Please review all lessons, Examples !!!!
