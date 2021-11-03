from validations import validate 
from project import createProject,getProjects,editProject,deleteProject,searchProject


####################################################################
########################            ################################
######################## Login options #############################
########################            ################################
####################################################################

def options():
    while True:
        choice = input("""
        to create project please enter 'c'\n
        to view all projects please enter 'v'\n
        to edit projects please enter 'e'\n
        to delete project please enter 'd'\n
        to search for a project using date example:'12-25-2018' please enter 's'\n
        """)
        if validate('c', choice):
            if choice == "c":
                createProject()
                continue
            elif choice == "v":
                getProjects()
                continue
            elif choice == "e":
                editProject()
                continue
            elif choice == "d":
                deleteProject()
                continue
            elif choice == "s":
                searchProject()
                continue
            else:
                print("enter valid choice")
        else:
            print("enter valid choice")