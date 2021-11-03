import ast
import os


####################################################################
###################  check if database exist ######################
####################################################################

def ifDBExist():
    try:
        db = open("./db.txt", "a")
        return db
    except:
        print("DB file is not exist i will create one for you")
        db = open("./db.txt", "w")
        return db



####################################################################
####################################################################

####################################################################
###################      get all users       ######################
####################################################################


def getUsers():
    users=[]
    db = ifDBExist()
    db.close()
    db = open("./db.txt", "r")
    for record in db:
        users.append(ast.literal_eval(record))
    db.close()
    return users

####################################################################
####################################################################
####################################################################
###################  Check for user if exist ######################
####################################################################

def getifexist(field, val):
    try:
        users=getUsers()
    except Exception as e:
        return False
    for u in users:
        if u[field] == val:
            os.environ['email']=val
            print(os.getenv('email'))
            return u
        
    return False


####################################################################
####################################################################







