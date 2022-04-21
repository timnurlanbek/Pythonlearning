def show_options():
    print("----------select----------")
    print()
    print("1--Login: 2--Register New Accaunt: 3--Deposit: 4--Exit:")
user_db={"admin": "Abc123!"}
# if "admin" in user_db:
#if user_db["admin"] == "Abcs123!"
deposits=0


while True:
    show_options()
    option=input("enter your option:")
    if option=="1": # login
        user_name = input("enter your username")
        if user_name in user_db:
            password= input("Enter your passcode please:")
            if user_db[user_name]==password:
                print("You logged in succesfully")
            else:
                print("Incorrect password")
        else:
            print("No such user name")
    if option=="2": # register new accaunt
        user_name=input("Enter your new username:") # randomname
        if user_name not in user_db: #user_db = {"admin":"Abc123!"}
            password = input("type your six digit new password:")
            if len(password)>=6:
                user_db[user_name]=password
                print("Your have successfully created new accaunt")
            else:
                print("Password does not match requirements")
        else:
            print(user_name, "already exists")
    
    if option=="3": # deposit
        amount=input("Enter amount:")
        deposits+=int(amount)
        print("Your current total amount ", deposits)

    if option=="4": # withdraw
        amount=input("Enter amount to withdraw:")
        deposits-=int(amount)
        print("Your current total amount ", deposits)

    if option==5: # exit
        print("Good bye")
        break
print(user_db)
