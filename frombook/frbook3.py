# prompt = '\nTell me a word or a sentence and I will repeat it back to you: \n'
# prompt+= '(When you are done, just write "quit" and bot stops asking)'

# active = True
# while active:
#     message = input("\t"+prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# 7-5 movie tickets

# name= '''Hello!. Welcome to AMC theater!\tYou can get discounts by telling me your age
# Please enter here your age: \n'''
# name+='(When you are done, enter "quit" and bot stops working): '

# yesn= "Would you like to continue>>> Yes/No: "




# active = True

# while active:
#     name1=int(input('\t'+name))

    
#     if name1<=3 :
#         print('Alright. Tickets under the third age are free')
#         yes = input(yesn)
#         if yesn=='no':
#             break
#         else:
#             print(name1)

#     elif name1 <=12:
#         print('Good. Your ticket will be $10 for each person with a discount')
#         yes = input(yesn)
#         if yesn=='no':
#             active = False
#         else:
#             print(name1)
#     elif name1>13:
#         print('Tickets over 12 age are $15 with discount')
#         yes = input(yesn)
#         if yesn=='no':
#             active=False
#         else:
#             print(name1)
#     else:
#         print('I do not understand you')
#         yes = input(yesn)
#         if yesn=='no':
#             active=False
#         else:
#             print(name1)
  


# prompt2 = '\nHow old are you?: '
# prompt2+= '\n(Enter "quit" when your are done): '
# active =True
from tkinter.messagebox import YESNO


young='are you a child?: '
# while active:
   
#     age = input(prompt2)
   
#     if age == 'quit':
#         break
    
#     age = int(age)

#     if age<3:
#         print('Tickets are free')
#         child=input(young.title())
#         if child=='yes':
#             print('ok')
#         else:
#             print('you are liar bitch!')
#             active=False
#     elif age<13:
#         print('Tickets are $10 for each person')
#     else:
#         print('Tickets are $15!')    


# while True:
#     child = input(young.capitalize())
#     if child == 'no':
#         print('LIAR')
#     else:
#         print('Good')


# prompt3 = '\tHi! \tPlease tell me the password: '
# money_in_bank = 1500000000
# active = True
# while active:
#     password = input(prompt3.casefold())

#     if password==str(123321):
#         print('\tWelcome Mr.Johnson')
#         print('\tYou have $'+str(money_in_bank)+' in bank accaunt.\t')
#         taken_money= input('How much money will you get?: ')
#         reamaining= int(money_in_bank)-int(taken_money)
#         print('Done! Remaining money $'+str(reamaining))
#         YESNO=input('Done? (yes/no)')
#         if YESNO=='no':
#             print()
#         else:
#             active=False
            
#     else:
#         print('Invalid password!')
        

# while loop wiith lists

atheists = ['Nurbek','Asan','Tim','Brian']
muslims = []

while atheists:
    converting = atheists.pop()

    print('Converting atheists: '+converting.title())
    muslims.append(converting)

print('\nThe following atheists have been converted: ')
for muslim in muslims:
    print(muslim.title())






        