from lib2to3.pytree import convert


# format function
def print_full_name(fname,lname):
    print("Hello {} {}! You just delved into python.".format(fname.title(),lname.title()))

print_full_name("Tim","Thompson")

# hours and min to seconds

def hourstomin(hour,min):
    sec = ((hour * 60) + min)*60
    return sec

# print(hourstomin(1,3))
# print(hourstomin(2,0))
# print(hourstomin(1,0))

# days to min, do it !
def weekdaytohrs(day,hour):
    min= ((day*24)+hour)*60
    return min

print(weekdaytohrs(1,0)) 
#--------------------------------------------------------

# num = int(input("Enter any number")) #      bergen sanyna cheyn kaytalagych
# def add_up_while(number):
#     if number >=1:
#         i=1
#         sum=0
#         while i<=number:
#             sum+= i 
#             i+=1
#         return sum
#     else:
#         return "wrong argument"

# print(add_up_while(4))
# print(add_up_while(13))
# print(add_up_while(600))
# print(add_up_while(8))
# print(add_up_while(20))
# print(add_up_while(3))


# def add_up_while(number):
#     if number >=1:
#         sum=0
#         for i in range(1,number+1,1):
#             sum+=i




# def  findinglyear(year):
#     if year%4==0 and year%100!=0:
#         print(str(year)+": This is a leap year")
#     elif year%4 == 0 and year%400==0:
#         print(str(year)+": This is a leap year")
#         # return True
#     else:
#         print(str(year)+": this is not a leap year")
    
#     # return False

# year=int(input("enter a year: "))
# print(findinglyear(year))
# # print(findinglyear(1990))
# print(findinglyear(2002))
# print(findinglyear(2022))
# print(findinglyear(2389))
# print(findinglyear(4392))



    

