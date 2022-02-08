# a program that creates and confirms a password 

def create_password():
    name = input("whats your name: ")
    password = input("create a password: ")
    guess_attempt = 0
    guess_limit = 3
    while guess_attempt < guess_limit:
        confirm_password = input("confirm password: ")
        guess_attempt += 1
        if password == confirm_password:
            print("Hello " + name.upper() + " You have fully created your passcode thanks ")
            break
    else:
        print(f"Hello {name.upper()} the passcode do not match please try again later thanks")

create_password()