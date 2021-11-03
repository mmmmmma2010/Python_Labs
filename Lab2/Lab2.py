# def genratelist(length, start):

#     if start and length and length > 0 :
#         mylist = list(range(start, length))
#         print(mylist)
#     else:
#         print("enter valid length or start")
#     return 0

# genratelist(5,-1)


#################################################
# listitem=[]
# for i in range(1,3):
#     el=input(f"enter the element number {i}  : ")
#     listitem.append(el)

# listitem.sort()
# print(listitem)
# listitem.sort(reverse=True)
# print(listitem)

#################################################
# def getlongest(string):
#     if str(string).isalpha():
#         orderd = []
#         listofordered = []
#         prev = ""
#         maxlen = 0
#         for al in string:
#             if al >= prev:
#                 orderd.append(al)
#                 prev = al
#             else:
#                 s="".join(orderd)
#                 listofordered.append(s)
#                 orderd.clear()
#                 prev = ""

#         for i in listofordered:
#             if len(i) > maxlen:
#                 maxlen = len(i)
#                 orderd.clear()
#                 orderd = i

#         print(f"Longest substring in alphabetical order is: {orderd}")


# getlongest("abdulrahman")

#######################################################################

#################################crowd-funding###################
import re

user = {}
users = []


def validemail(email):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True

    else:
        return False


def getifexist(email):
    for u in users:
        if u["email"] == email:
            user = u
        else:
            print("user not exist ")


def checkpass(password):
    if user["password"] == password:
        print("login sucess")
    else:
        print("wrong password please try again")


def validate(vtype, string):
    string.strip()
    string.lower()
    if vtype == 'c':
        if string.isalpha() and len(string) == 1:
            return True
        else:
            return False
    elif vtype == 'n':
        if string.isalpha():
            return True
        else:
            return False

    elif vtype == 'e':
        if validemail(string):
            return True
        else:
            return False
    elif vtype == 'p':
        if len(string) > 6:
            return True
        else:
            return False
    elif vtype == 'ph':
        if string.isdigit() and len(string) == 11:
            return True
        else:
            return False


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
    users.append(user)


def login():
    if users:
        while True:
            email = input("plz write your email")
            if validate('e', email):
                getifexist(email)
                break

        while True:
            password = input(
                "plz write your password should be mor than 6 charachters")
            if validate('p', password):
                checkpass(password)
                break


while True:
    choice = input("plz write l for login , r for registeration ")
    if validate('c', choice):
        if choice == "r":
            registration()
            continue
        if choice == "l":
            if users:
                login()
            else:
                print("please add user fristly")
        else:
            print("enter valid choice")
    else:
        print("enter valid choice")
