def get_full_name(first_name, last_name):
    
    """ Return a formatted full name"""
    
    full_name="{} {}".format(first_name, last_name)

    return full_name.title()

musician = get_full_name("jimi","hendrix")

print(musician)
    