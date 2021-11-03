from registration import registration
from login import login
from validations import validate


####################################################################
########################            ################################
########################  Starter    ###############################
########################            ################################
####################################################################
def run():
    while True:
        choice = input("plz write l for login , r for registeration ")
        if validate('c', choice):
            if choice == "r":
                registration()
                continue
            if choice == "l":

                login()

            else:
                print("enter valid choice")
        else:
            print("enter valid choice")


if __name__ == "__main__":
    run()
