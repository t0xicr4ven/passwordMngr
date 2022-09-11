import random
import string

print("""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═

""")


## password generator
password = ""
"""
1. just lower case no numbers
2. lowe case and numbers
3. upper/lower and numbers
4. upper/lower/numbers and special chars
"""
def gen_passwd(lenOfPass,complexOfPass) -> string:
    the_passwd = ""
    # default complex to 4 if the input was incorrect
    if  isinstance(complexOfPass, int):
        if complexOfPass == 1:
            the_passwd = easy_passwd(lenOfPass)
        elif complexOfPass == 2:
            the_passwd = med_passwd(lenOfPass)
        elif complexOfPass == 3:
            the_passwd = hard_passwd(lenOfPass)
        else:
            the_passwd = very_hard_passwd(lenOfPass)
    else:
        the_passwd = very_hard_passwd(lenOfPass)

    return the_passwd 

# easy pass generation
def easy_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase))
    return the_passwd

# med pass generation
def med_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase + string.digits))
    return the_passwd

# hard pass generation
def hard_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))
    return the_passwd

# Vhard pass generation
def very_hard_passwd(lenOfPass):
    the_passwd = ""
    for _ in range(lenOfPass):
        the_passwd += "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation))
    return the_passwd


length_of_password = int(input("How long would you like your password: "))
complex_passwd = ''
while complex_passwd == '':
    complex_passwd = input("How difficult would you like your password? 1:easy, 2:med, 3:hard, 4:very hard:[Default is 4]:  ")



new_word = gen_passwd(length_of_password, complex_passwd)

print(new_word)
print(len(new_word))