import pyperclip
import random
import sys
import string


# print("""
# ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
# ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
# ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
# ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
# ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
# ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═

# """)

### Creation of password
def gen_passwd(lenOfPass) -> string:
    passwd = very_hard_passwd(lenOfPass)
    pyperclip.copy(passwd)
    return passwd

# Vhard pass generation
def very_hard_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation))
    return the_passwd

# password health checker
def check_passwd(passwd_to_check):
    print("The password you want to check: " + passwd_to_check)


### possible for a switch statment here
# check to see if use has put in any args
if len(sys.argv) >= 2:
    # if user want to make a password
    if sys.argv[1] == "gen":
        #user wants to make a password, need to get length
        if len(sys.argv) == 3:
           print("Your Password is: ")
           print(gen_passwd(int(sys.argv[2])))
        else:
            print("you have not entered length of password it will now default to 16")
            print("Your Password is: ")
            print(gen_passwd(16))
    # user wants to check the health of the password.
    elif sys.argv[1] == "check":
        print("You want to check the health of your password")
        check_passwd(sys.argv[2])
else:
    #no arguments entered, tell user to try again
    print("No arguments entered, please try again. or enter HELP as arg for a list of uses")



