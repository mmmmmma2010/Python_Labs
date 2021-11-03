from datetime import datetime
import os
from validations import validate
from dbFunctions import ifDBExist,getUsers
from dbFunctions import getifexist
project={}
projects=[]

####################################################################
########################                    ########################
######################## Projects Functions ########################
########################                    ########################
####################################################################
def createProject():
    pas = ""
    while True:
        title = input("plz write project title : ")
        if validate('n', title):
            project["title"] = title
            break

    while True:
        details = input("plz write project details : ")
        if validate('n', details):
            project["details"] = details
            break

    while True:
        target = input("plz write campiagn Total target : ")
        if validate('num', target):
            project["target"] = target
            break

    while True:
        start = input(
            "plz write start date 'YYYY-MM-DD' : ")
        if validate('d', start):
            project["start"] = start
            pas = datetime.strptime(start, '%Y-%m-%d')
            break
    while True:
        end = input(
            "plz write end date 'YYYY-MM-DD': ")
        if validate('d', end):
            if pas < datetime.strptime(end, '%Y-%m-%d'):
                project["end"] = end
                break
            else:
                print("end date should be greater than start date")
    user=getifexist("email", os.getenv('email'))
    user["projects"].append(project)
    try:
        users=getUsers()
        db = ifDBExist()
        db.close()
        db = open("./db.txt", "w")
        
        for line in users:
            if line["email"] != user["email"]:
                db.write(f"{line}\n")
        db.write(f"{user}\n")
        db.close()
    except Exception as e:
        print(e)


####################################################################
####################################################################

####################################################################
###################  editProject    ################################
####################################################################


def editProject():
    global project
    getProjects()
    while True:
        choice = input(
            "\nPlease enter the number beside the project you want to edit : ")
        if validate("num", choice):
            try:
                project = projects[int(choice)]
            except Exception as e:
                print(e)
            if project:
                while True:
                    field = input(
                        "Please enter the Field that you want to edit : ")
                    fieldData = project[field]
                    if fieldData:
                        if field == "title" or field == "details":
                            while True:
                                string = input(
                                    "plz write the value you want update : ")
                                if validate('n', string):
                                    project[f"{field}"] = string
                                    break

                        elif field == "start" or field == "end":
                            while True:
                                string = input(
                                    "plz write the value you want update : ")
                                if validate('d', string):
                                    project[f"{field}"] = string
                                    break
                        else:
                            while True:
                                string = input(
                                    "plz write the value you want update : ")
                                if validate('num', string):
                                    project[f"{field}"] = string
                                    break
                        try:
                            user=getifexist("email", os.getenv('email'))
                            user["projects"].remove(
                                user["projects"][int(choice)])
                            user["projects"].append(project)
                            users=getUsers()
                            db = ifDBExist()
                            db.close()
                            db = open("./db.txt", "w")
                            
                            for line in users:
                                if line["email"] != user["email"]:
                                    db.write(f"{line}\n")
                            db.write(f"{user}\n")
                            db.close()
                        except Exception as e:
                            print(e)
                        break

                    else:
                        print("enter valid Field Please")
                break

####################################################################
####################################################################

####################################################################
###################  getProjects    ################################
####################################################################

def getProjects():
    global projects
    user=getifexist("email", os.getenv('email'))
    projects = user["projects"]
    if projects:
        for p in projects:
            print(f"\n{projects.index(p)}  : {p}")




####################################################################
####################################################################

####################################################################
###################  searchProject  ################################
####################################################################

def searchProject():
    count=0
    user=getifexist("email", os.getenv('email'))
    while True:
        sDate = input(
            "plz write  date to search 'YYYY-MM-DD' : ")
        if validate('d', sDate):
            sDate = datetime.strptime(sDate, '%Y-%m-%d')
            for p in user["projects"]:
                if datetime.strptime(p["start"], '%Y-%m-%d') == sDate or datetime.strptime(p["end"], '%Y-%m-%d') == sDate:
                   print(p)
                   count+=1                 
            if count==0:
                print ("no data match")
            break


####################################################################
####################################################################

####################################################################
###################  deleteProject  ################################
####################################################################


def deleteProject():
    user=getifexist("email", os.getenv('email'))
    global project
    getProjects()
    while True:
        choice = input(
            "\nPlease enter the number beside the project you want to delete : ")
        if validate("num", choice):
            try:
                users=getUsers()
                project = projects[int(choice)]
                user["projects"].remove(user["projects"][int(choice)])
                db = ifDBExist()
                db.close()
                db = open("./db.txt", "w")
                for line in users:
                    if line["email"] != user["email"]:
                        db.write(f"{line}\n")
                db.write(f"{user}\n")
                db.close()
                print(" project deleted")
                break
            except Exception as e:
                print("Project dose not exist")

####################################################################
####################################################################








