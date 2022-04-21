def describe_pet(pet_name, animal_type="dog"):

    """Display information about a pet"""

    print("I have a {}.".format(animal_type.lower()))

    print("My {}'s name is {}.".
    format(animal_type.lower(),pet_name.title()))

describe_pet("willie")

describe_pet(pet_name="willie",animal_type="dog")

describe_pet(animal_type="dog",pet_name="willie")

describe_pet("willie","dog")

describe_pet(pet_name="willie")

#describe_pet("Mia","cat")

#describe_pet(animal_type="hamster",pet_name="harry")
#describe_pet(pet_name="harry",animal_type="hamster")