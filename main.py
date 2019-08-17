import time

import encrypt
import web_interface
from simple_sha import simple_sha


def run(usr):
    while (0 == 0):

        web_interface.get_file(usr)
        encrypt.decrypt(["mati2000", "koniec"])
        msg = input()
        encrypt.encrypt(msg, ["mati2000", "koniec"])
        web_interface.upload_file(usr % 1)

        print("would you like to send another file (y/n)")
        response = input()

        if(response == "n"):
            break


print("login")
login = input()
print("pssd")
pssd = input()
print(time.time())


if(simple_sha(login) == "1f89ff93b5534d0954255a21a476e4a005d92e61468d54c5ad156b65"):
    if(simple_sha(pssd) == "394208e8e18d92c06e588ec990da0109e42d51132ad70f59fb4a052e"):
        run(0)


if (simple_sha(login) == "0de1eff369facd15147c395bd2a71b1991666700a9e2bf58d8cbec4b"):
    if (simple_sha(pssd) == "9dcc83ad783bd9fcac5417ab3fb91f26747503f8f88eeb8db0ed9f2d"):
        run(1)


# Piotr
"""


"""

# Mateusz
"""


"""
