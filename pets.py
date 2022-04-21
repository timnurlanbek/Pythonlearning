def describe_pet(animal_type, pet_name):

    """Display information about a pet"""

    print("I have a {}.".format(animal_type.lower()))

    print("My {}'s name is {}.".
    format(animal_type.lower(),pet_name.title()))

describe_pet("dog","Teka")
describe_pet("cat","Mia")

describe_pet(animal_type="hamster",pet_name="harry")
describe_pet(pet_name="harry",animal_type="hamster")