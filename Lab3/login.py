from dbFunctions import getifexist
from validations import validate, checkpass
from userOptions import options

####################################################################
###################       login     ################################
####################################################################
def login():

    while True:
        email = input("plz write your email : ")
        if validate('e', email):
            if getifexist("email", email):
                break
            else:
                print("user dose not exist")

    while True:
        password = input(
            "plz write your password should be mor than 6 charachters : ")
        if validate('p', password):
            if checkpass(password):
                options()
                break


####################################################################
####################################################################

