# removing all instances

# from http.client import responses


# prefereble_food= ['egg','plov','kuurma','egg','nan','egg']

# print(prefereble_food)
# while 'egg' in prefereble_food:
#     prefereble_food.remove('egg')
# print('Foods without egg\t')
# print(prefereble_food)

# responses = {}

# polling_active = True

# while polling_active:
#     name = input('Enter your name: ')
#     mountain = input('Which mountain would you like to climb someday: ')

#     responses[name]=mountain

#     repeat = input('Would you like to give the poll to another one?>>>(yes/no)\n')


#     if repeat =='no':
#         polling_active=False

# print('\n---------- Poll Results ----------')
# for name,mountain in responses.items():
#     print('\n'+name.title()+' would like to climb to '+mountain.title())


from pickle import TRUE


ordered_sandwiches = [
    'chicken sandwich',
    'egg sandwich',
    'pastrami sandwich',
    'seafood sandwich',
    'roast beef sandwich',
    'pastrami sandwich',
    'grilled cheese',
    'pastrami sandwich',
]

finished_sandwiches = []

while ordered_sandwiches:

    cooking = ordered_sandwiches.pop()

    print(cooking.title()+' is ordered ...')

    finished_sandwiches.append(cooking)

while 'pastrami sandwich' in finished_sandwiches:
        finished_sandwiches.remove('pastrami sandwich')
print('\n\tSorry we run out pastrami sandwich')
    
print('\n\tFollowing sandwiches are ready ...')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


# poll favorite place

prompt4 = 'Enter your name: '

responses = {}
while True:
    name = input('\n'+prompt4)
    favorite_place= input('\nIf you could visit one place in the world, where would you go?: ')

    responses[name]=favorite_place

    repeat = input('Would you like to give the poll to another person to try? (yes/no)')

    if repeat == 'no':
        break
print('\n\t-------------- Poll Results --------------')
for name, favorite_place in responses.items():
    print(name.title()+' would like to go to '+favorite_place.title())