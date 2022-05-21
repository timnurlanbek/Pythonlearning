from tkinter import N


favorite_places = {
    "Daniiar":["bishkek",'kadamjai','batken'],
    'nurtilek':['talas','texas','stafford'],
    'kerven':['turkmenistan','austin','california'],
    'temirbek':['hawaii','Mekka','world'],

}
for names,placs in favorite_places.items():
    a=names.title()+"'s favorite places are: "
    print(a)
    for place in placs:
        print(place.title())


cities = {
    "stafford":{
        "country":"USA",
        "population":'17666',
        "fact":'''Stafford is a city in the U.S. state of Texas, in the Houston.
        The Woodlands–Sugar Land metropolitan area. The city is mostly in Fort Bend County, 
        with a small part in Harris County. As of the 2010 census''',
        },
    "kadamjai":{
        'country':'kyrgyzstan',
        'population': '14049',
        'fact':'''Kadamjay (Kyrgyz: Кадамжай; Russian: Кадамжай, earlier also Кадамджай) is
         a city[1] located in Kadamjay District of Batken Region of Kyrgyzstan.''',
        },
    "abdusamat":{
        'country':'kyrgyzstan',
        'population':'6274',
        'fact':"one of the greatest community",
    }

}

for cities,informations in cities.items():
    print('about '+cities.title()+"'s information is: ")
    for information,detail in informations.items():
        print(information.title()+': '+detail.title())

    
#------------------------------------------------------------------------------------

# Whiile loop and input from book

# active = True
# sen="Tell me a sentence and I will repeat it to you: "
# sen+= "\nType 'quit' whenever you want to quit: "
# while active:
#     mesage=input(sen)

#     if mesage=="quit":
#         active=False
#     else:
#         print(mesage)



# prompt = '\nTell me smth and I will repeat it back to you: '
# prompt+='\nEnter "quit" to end the program: '
# active = True
# while active:
#     message=input(prompt)

#     if message=="quit":
#         active=False
#     else:
#         print(message)



# pizza toppings
# prompt='\nTell me what kind of toppings would you like to add to pizza? '
# prompt+='\n(Enter "quit" whenever you want to quit): '
# listtop=[]

# while True:
#     topping=input(prompt)
#     if topping == "quit":
#         print("Alright! Your order will be ready in few minutes!")
#         break
        
#     else:
#         print("\nAlright. Your topping added! "+topping.title())
#         listtop.append(topping)
#         print(listtop)

print()
print()
print()
# writing movie tickets
tickets_active = True
age_dict = {}

age= input(int("\nPlease enter your age and we will try to make a discount: "))
yesno='Would you like to take more tickets? : '

while tickets_active:
    
    print(int(age))
    if age<=3:
        print('ticket is free for you')
    elif age <=12:
        print('Ticket with discount is $10')
    else:
        print('Ticket is $15 without discount')
    print(input(yesno))
    if yesno=='no':
        tickets_active=False
   
    


