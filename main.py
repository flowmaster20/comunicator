import time

import encrypt
import web_interface
from simple_sha import simple_sha

print("login")
login = input()
print("pssd")
pssd = input()
print(time.time())
if (simple_sha(login) == "0de1eff369facd15147c395bd2a71b1991666700a9e2bf58d8cbec4b"):
    if (simple_sha(pssd) == "9dcc83ad783bd9fcac5417ab3fb91f26747503f8f88eeb8db0ed9f2d"):
        while (0 == 0):
            msg = input()
            encrypt.encrypt(msg, ["mati2000", "koniec"])
            web_interface.upload_file()
            print("would you like to send another file (y/n)")
            response = input()
            if(response == "n"):
                break
