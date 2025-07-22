# you are building a simple app that registers users.
# you want to separate concerns: getting input, validating it and saving it.
# Task : - write register_users() that calls:
# get_input(), validate_input(), save_to_db()

def get_input():
    print("getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("register user")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered")

register_user()