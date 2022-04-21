def get_full_name(first_name, last_name, middle_name=''):
    
    """ Return a formatted full name"""
    
    if middle_name:
        full_name="{} {} {}".format(first_name, middle_name, last_name)
    else:
        full_name="{} {}".format(first_name, last_name)

    return full_name.title()

musician = get_full_name("jimi","hendrix")
print(musician)

musician = get_full_name("john","hooker","lee")
print(musician)  