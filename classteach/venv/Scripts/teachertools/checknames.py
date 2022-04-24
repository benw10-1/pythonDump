import string

txt =input("Input the name of the log file (without _log.txt extension): ")
filem = open(txt+"_log.txt")
textin = filem.readlines()
name=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
code=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
store=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
i=0
p=0
j=0
for k in textin:
    name[p] = k.split("#")[0]
    code[p]= k.split("#")[1]
    p=p+1
while True:
    input1 =input("Enter code: ")
    yes=False
    for m in code:
        if input1 in m:
            print(name[i])
            yes=True
            storecur=name[i]
        i=i+1
    i = 0
    if yes==True:
        if storecur in store:
            print("Already marked")
            continue
        if storecur not in store:
            store[j]=storecur
            j=j+1
    if input1.lower() == "finish":
        file1 = open(txt+"_recap", "w+")
        for s in store:
            if s != "":
                print(s)
                L=s+"\n"
                file1.writelines(L)
        file1.close()
        filem.close()
        break
    if input1.lower() == "here":
        for s in store:
            if s != "":
                print(s)
        continue
    if yes==False:
        print("Invalid code please try agian")



