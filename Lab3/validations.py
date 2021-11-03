from datetime import datetime
import os
import re
from dbFunctions import getifexist


####################################################################
########################            ################################
######################## Validations ###############################
########################            ################################
####################################################################


####################################################################
###################  Validation of date  ###########################
####################################################################

def isdate(val):
    format = '%Y-%m-%d'
    try:
        if datetime.strptime(val, format):
            return True
    except Exception as e:
        return False

####################################################################
####################################################################



####################################################################
###################  email Validation        ######################
####################################################################
def validemail(email):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True

    else:
        return False


####################################################################
####################################################################


####################################################################
###################  Check for Login Password ######################
####################################################################

def checkpass(password):
    user = getifexist("email", os.getenv('email'))
    if user["password"] == password:
        return True
    else:
        return False


####################################################################
####################################################################

####################################################################
###################  Multi validation Function ######################
####################################################################
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
    elif vtype == 'num':
        if string.isdigit() and int(string) >= 0:
            return True
        else:
            return False
    elif vtype == 'd':
        if isdate(string):
            return True
        else:
            return False



####################################################################
####################################################################





