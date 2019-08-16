

import io

import pyAesCrypt
import sha3

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
"""
binary_data = b"This is encoded text \x00\x01"
msg = input()

fin = io.BytesIO(msg)
fciph = io.BytesIO()
fdec = io.BytesIO()

pyAesCrypt.encryptStream(fin, fciph, password, bufferSize)

print("encrypted: " + str(fciph.getvalue()))

ctlen = len(fciph.getvalue())

fciph.seek(0)

pyAesCrypt.decryptStream(fciph, fdec, password, bufferSize, ctlen)

print("decrypted: " + str(fdec.getvalue()))
"""

# pobieram dane so wyslania
msg = input()

# tworzenie hashu do sprawdzenia
s = sha3.sha3_224(msg.encode('utf-8')).hexdigest()

# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
pyAesCrypt.encryptFile("data.txt.aes", "output.txt.aes", password, bufferSize)

# decrypt
wynik = pyAesCrypt.decryptFile(
    "output.txt.aes", "data.txt.aes", password, bufferSize)
wynik = pyAesCrypt.decryptFile(
    "data.txt.aes", "output.txt", password, bufferSize)

print(s)
print(wynik)
