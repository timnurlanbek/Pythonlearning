# Condition is always True
while True:
    print("\nPlease enter the name of a city you have visited: ")
    city = input("enter 'quit' when you are finished. ")

    if city == "quit":
        break
        #using break to Exit a loop

    else:
        print(f"I'd love to go to {city.title()}")