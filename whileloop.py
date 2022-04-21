# Alright we use while loop when we want to repeat \
# a block code until the condition is true

# while loop statement repeadetly executes a block code while 
# a particular condition is true

# count = 1
# condition: run loop while count is less than 5
# while count < 5:
#     print(count)
#     count = count +1

# print(count)


# count = 0
# #condition: run loop till count less or equal to ten
# while count < 10:
#     print(count)
#     count= count+1
# print(count)

# count = 1
# while count> 4:
#     print(count)
#     count = count +1
# print(count)


# answer = input("Will you be one of the most famous person")
# while answer == "yes":
#     input("Will you be who you want to be?")
#     print(answer)

# number = int(input("Enter any number between 5 and 10: "))
# while number < 5 or number >10:
#     print("Number is incorrect. Please type correct number")
#     int(input("Enter a number between 5 and 10: "))
# else:
#     print("number is correct")



# number = int(input("Enter numb between 30 and 100: "))
# while number <30 and number >100:
#     print("number that you typed is incorrect.")
#     int(input("please type correct number that was asked above: "))
# else: 
#     print("Given number is true !")

# a=int(input("enter any num"))
# print(a % 2)


n = int(input("enter any num: "))
while n > 0:
    if n % 2 == 0:
        print(n,"is even.")
    else:
        print(n, " is odd")
    n = n - 1