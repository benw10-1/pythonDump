file1 = open("asd.rtf", "r")

for x in file1.readlines():
    print (x)
file1.close()