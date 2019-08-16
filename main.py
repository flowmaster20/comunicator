import encrypt
import web_interface
from simple_sha import sha

print("login")
login = input()
print("pssd")
pssd = input()

if (sha(login) == "0de1eff369facd15147c395bd2a71b1991666700a9e2bf58d8cbec4b"):
    if (sha(pssd) == "9dcc83ad783bd9fcac5417ab3fb91f26747503f8f88eeb8db0ed9f2d"):
        while (true):
