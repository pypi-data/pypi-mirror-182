def binary(message):
    var = " ".join(format(ord(c), 'b') for c in message)
    return var

def normalize(File_Or_Message):
    var2 = "".join(chr(int(c,2)) for c in File_Or_Message.split(" "))
    return var2
