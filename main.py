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

def gen_passwd(lenOfPass) -> string:
    return very_hard_passwd(lenOfPass)

# Vhard pass generation
def very_hard_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation))
    return the_passwd


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
    else:
        print("something went wrong or number inputed")
else:
    #no arguments entered, tell user to try again
    print("No arguments entered, please try again. or enter HELP as arg for a list of uses")


## password generator



