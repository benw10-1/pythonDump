import string


def encrypt(word):
    store = [None]*len(word)
    i = 0
    char1 = [char for char in word]
    while "a" in char1:
        if "a" == char1[i]:
            char1[i] = "0"
        i += 1
    i = 0
    while "e" in char1:
        if "e" == char1[i]:
            char1[i] = "1"
        i += 1
    i = 0
    while "o" in char1:
        if "o" == char1[i]:
            char1[i] = "2"
        i += 1
    i = 0
    while "u" in char1:
        if "u" == char1[i]:
            char1[i] = "3"
        i += 1

    i = len(char1)
    while i > 0:
        store[len(char1) - i] = char1[i-1]
        i -= 1

    return "".join(store) + "aca"

print (encrypt("burak"))