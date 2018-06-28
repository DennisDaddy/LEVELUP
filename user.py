users = {}
option = ""

def welcome_message():
    option = input("Press Yes if Registered or No if you have an account to login ? Yes/No? ")
    if option == "Yes":
        log_user()
    elif option == "No":
        register()

def register():
    user_enter = input("Enter user name: ")
    first_name = input("Enter First name: ")
    last_name = input("Enter last name: ")
    user_email = input("Enter email address: ")


    if user_enter in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create a new password: ")
        users[user_enter] = createPassw
        print("\nUser successfully created\n")

def log_user():
    login = input("Enter user name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")

while option != "q":
    welcome_message()
    