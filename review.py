def get_eshak_name(first_name, last_name):
    full_name = " {} {}" .format(first_name, last_name)
    return full_name.title()

football_player = get_eshak_name("Karim","Benzema")

print(football_player)

def describe_pet(animal_type, pet_name):
    print("I have a {}." .format(animal_type.lower()))
    print("My {}'s name is {}.".
    format(animal_type.lower(), pet_name.title()))

describe_pet("dog", "Mike")
describe_pet("cat", "Mia")
describe_pet("friend", "Kerven")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")


def get_full_name(firstName, lastName, middleName = ''):

    if middleName:
        fullName = "{} {} {}".format(firstName, middleName, lastName)
    else:
        fullName="{} {}".format(firstName, lastName)
    return fullName.title()

musician = get_full_name("Tim","Thompson", "Nurlanbekov")
print(musician)

# functions in module 
#stroing your functions in modules(files.py)
# import module_name                                import petsD
#module_name.function_name()                        petsD.describe_pet()

# import module_name as mn                          import pandas as pd

#from module_name import function_name              


def get_grade(final_grade):
    if final_grade > 91:
        return "A"
    elif final_grade >76:
        return "B"
    elif final_grade >65:
        return "C"
    elif final_grade >50:
        return "D"
    else:
        return "Fck off"
