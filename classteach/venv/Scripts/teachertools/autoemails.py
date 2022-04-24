import smtplib, ssl, string, random


while True:
    nametxt1 = input("Enter name of txt with emails in it: ")
    try:
        file1 = open(nametxt1+".txt", "r")
    except:
        print("Invalid text file entered please try again")
        continue
    break
nametxt = input("Input class and date(name of log txt): ")
index1 = input("Enter number of students in class: ")
subjcc = input("Enter the subject that you want to send in the email: ")


file2 = open(nametxt+"_log.txt", "w+")

text = file1.readlines()


def randomNums(Length):
    return ''.join(random.choice(string.digits) for i in range(Length))


port = 465  # For SSL

smtp_server = "smtp.gmail.com"

sender_email = "WirthMath80@gmail.com"
password = "12345classemail"
message = """\
Subject: Zoom Code """+subjcc

context = ssl.create_default_context()

i=0
j=0
p=0

server = smtplib.SMTP_SSL(smtp_server, port, context=context)
server.login(sender_email, password)
code = [None]*int(index1)
while j < int(index1):
    code[j] = randomNums(4)

    sss=text[p]
    ppp=code[j]
    lll=sss.strip()+"#"+ppp.strip()
    print("Sending email...\n")
    server.sendmail(sender_email, text[p+1],message+"\nDear: "+text[p]+"\nWrite your name exactly as indicated below BEFORE entering the waiting room.\n"+lll+"\nRemember, this code changes for every class and you will not be let in without the appropriate name.\nThank you, Dolores")
    print("Writting to txt...\n")
    L = [lll+"\n"]
    file2.writelines(L)
    j = j + 1
    p = p + 4
file1.close()
file2.close()











