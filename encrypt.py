

import io

import pyAesCrypt
import sha3

# encryption/decryption buffer size - 64K

password = ["password1", "password2"]


def encrypt(msg, password):
    bufferSize = 64 * 1024
    # pobieram dane so wyslania
    f = open("data.txt", "a")
    f.write(msg)
    # tworzenie hashu do sprawdzenia wyjsciowej wiadomosci
    s = sha3.sha3_224(msg.encode('utf-8')).hexdigest()

    # encrypt
    pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password[0], bufferSize)

    # unlimited layers of encoding
    """
    for i in range(len(password)-2):
        pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password[0], bufferSize)
    """

    pyAesCrypt.encryptFile("data.txt.aes", "output.txt.aes",
                           password[len(password) - 1], bufferSize)

    return s


def decrypt(password, input_file, sha_):
    bufferSize = 64 * 1024
    wynik = pyAesCrypt.decryptFile(
        input, "data.txt.aes", password[1], bufferSize)

    wynik = pyAesCrypt.decryptFile(
        "data.txt.aes", "output.txt", password[0], bufferSize)
    f = open("output.txt", "r")
    wynik = f.read()
    if (sha3.sha3_224(wynik.encode('utf-8')).hexdigest() == sha_):
        print(wynik)
    else:
        print("message corupted")
