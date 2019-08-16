

import pyAesCrypt

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
# decrypt

pyAesCrypt.decryptFile("data.txt.aes", "output.txt", password, bufferSize)
print(output)
