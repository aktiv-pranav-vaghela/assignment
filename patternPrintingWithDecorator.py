#This shall adds a line of stars as a message
def add_stars(func):
    def wrapper():
        print("**********")
        func()
        print("**********")
    return wrapper

# This shall adds a line of dashes as a message
def add_dashes(func):
    def wrapper():
        print("----------")
        func()
        print("----------")
    return wrapper

# The original function we wanted to be decorated
@add_stars
@add_dashes
def say_hello():
    print("Hello!")

# Calls the decorated function
say_hello()