# functions:>>> ------     not to repeat and write one code/task again and again, we
# we have functions 

def greeting_user():
    #display a simple greeting
    print('Hello')
greeting_user()

def greeting_user(username):
    # display simple greeting
    print('Hello ' + username.title()+ " Welcome to your world !")
greeting_user('Temirbek')

def display_message(topics):
    #Topics that we are learning  in this chapter
    print('You are learning '+topics.title()+' in this chapter')
display_message('functions')
display_message('while loop and dictionaries')
display_message('for loop')



def favorite_books(title):
    #my favorite books with titles.
    print('My one of the most favorite book is '+title.title()+'\nThis is an amazing book')
favorite_books('Oshibki na million')
favorite_books('cheksiz nur')