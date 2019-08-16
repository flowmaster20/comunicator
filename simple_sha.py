import sha3


def sha(data):
    return sha3.sha3_224(data.encode('utf-8')).hexdigest()
