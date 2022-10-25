import hashlib


def peek(obj):
    for key in dir(obj):
        if key.startswith('_'):
            continue
        print('[{}]:{}'.format(key, getattr(obj, key, '')))


def hash(salt, content):
    salted = content + salt
    return hashlib.sha512(salted.encode("utf8")).hexdigest()


if __name__ == '__main__':
    obj = dict()
    peek(obj)
    print(hash('ddddddd', 'dddddddd'))
