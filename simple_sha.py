import sha3


def simple_sha(data):
    return sha3.sha3_224(data.encode('utf-8')).hexdigest()
