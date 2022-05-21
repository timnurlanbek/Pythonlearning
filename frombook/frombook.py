# print("\thello world".title())
# print("hello world")
# print()
# print("\nHi Tim!")
# print("hi tim")
# print("\nHI Tim")


# aliens=[]

# for number_aliens in range(30):
#     new_alien={"color":"green","points":"5","speed":"slow"}
#     aliens.append(new_alien)

# for alien in aliens[0:3]:
#     if alien["color"]=='green':
#         alien['color']='yellow'
#         alien['points']='10'
#         alien['speed']='medium'
#     if alien['color']=='yellow':
#         alien['color']='red'
#         alien['points']='15'
#         alien['speed']='high'

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print("Total number of aliens " + str(len(aliens)))


# orders={
#     'crust':'thick',
#     'toppings':['mailuu','extra cheese']
# }

# print ( "You ordered " + orders['crust'] + "-crust with the following toppings")

# for topping in orders['toppings']:
#     print("\t" + topping)


# favorite_langugages = {
#     'Asan':['Ruby','Python','C'],
#     'Uson':['Java','PHP'],
#     'Altynai':['javascript','c++']
# }

# for name,languages in favorite_langugages.items():
#     print(name.title() + "'s favorite languages are: " )
#     for language in languages:
#         print("\t" + language.title())

                                                                    # dictionary in dictionary



Daniiar={
        'first_name':'daniiar',
        'last_name':'Zholmatov',
        'country':'Kyrgyzstan',
        'age':'21',
        'gender':'male',
        'number':'+1 832-503-3968',
        'birthday':'8-august',}
nurtilek={
        'first_name':'nurtilek',
        'last_name':'Tobokelov',
        'country':'kyrgyzstan',
        "age":'20',
        'gender':'male',
        'number':'+1 832-503-3405',
        'birthday':'unknown',
         },
kerven={
    'first_name':"Kerven",
    'last_name':'Poltaev',
    'country':'turkmenistan',
    'age':'20',
    'gender':'male',
    'number':'+1 346-399-6808',
    'birthday':'28-september'

}    
people =[Daniiar,nurtilek,kerven]


for i in people:
    print(i)






    


# for name,information in cascade_guys.items():
#     print('\n Username: ' + name.title())
#     full_name= information['last_name']+ " is " +information["age"]+" years old"
#     location=information['country']

#     print('\tUsername: ' + full_name)
#     print('\tlocation: ' + location)


Shimshek = {
    "cat":"Mehmet Han"
}
Jolbors = {
    "dog":"temirbek"
}
Reks = {
    "dog":"asan"
}

pets = [Shimshek,Jolbors,Reks]

for pet in pets:
    print("\t Your pet is: ")
    print(pet)


def name(fname,lname):
    name[fname]= "Tim"
    name[lname]="Thompson"
    full_name = "My first name is " + fname + " and last name is "+lname
    return full_name
    
