import os
from validations import validate
from dbFunctions import ifDBExist

user={}
####################################################################
###################  registration   ################################
####################################################################


def registration():
    
    pas = ""
    while True:
        fname = input("plz write your first name : ")
        if validate('n', fname):
            user["firstname"] = fname
            break

    while True:
        lname = input("plz write your last name : ")
        if validate('n', lname):
            user["lastname"] = lname
            break

    while True:
        email = input("plz write your email : ")
        if validate('e', email):
            user["email"] = email
            break

    while True:
        password = input(
            "plz write your password should be mor than 6 charachters : ")
        if validate('p', password):
            pas = password
            break
    while True:
        chpassword = input("plz repeat your password : ")
        if validate('p', chpassword):
            if pas == chpassword:
                user["password"] = chpassword
                break
    while True:
        phone = input("plz write your phone : ")
        if validate('ph', phone):
            user["phone"] = phone
            break
    user["projects"] = []
    db = ifDBExist()
    db.write(f"{user}\n")
    db.close()


####################################################################
####################################################################

