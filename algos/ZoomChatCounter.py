from tkinter import Tk
from tkinter.filedialog import askopenfilename
import datetime
from numpy import std, mean
import time
import os


Tk().withdraw()
filename = askopenfilename(filetypes=[("Text files", "*.txt")], title="Select Zoom Message Log")
print()
try:
    with open(filename, "r") as file:
        count = 0
        acount = 0
        studentlist = {}
        messagecount = {}
        contents = file.readlines()
        for x in contents:
            if x:
                x = x.split()
                if "From" in x:
                    if "to" not in x:
                        name = " ".join(x).split(":")[2].split("From")[1].strip().lower()
                        message = " ".join(x).split(":")[3].strip()
                        if name not in studentlist or name not in messagecount:
                            messagecount[name] = 1
                            studentlist[name] = [message]

                        else:
                            messagecount[name] = messagecount[name] + 1
                            studentlist[name].append(message)

                    else:
                        name = " ".join(x).split(":")[2].split("From")[1].split("to")[0].strip().lower()
                        message = " ".join(x).split(":")[3].strip()
                        if name not in studentlist or name not in messagecount:
                            messagecount[name] = 1
                            studentlist[name] = [message]

                        else:
                            messagecount[name] = messagecount[name] + 1
                            studentlist[name].append(message)

    with open(os.path.join(os.getcwd(), filename.split("/")[len(filename.split("/")) - 1].replace(".txt", "")) + "_numberlog.txt", "w+") as file1:
        sortlist = [x for x in messagecount]
        calc = []
        ood = []
        sortlist.sort()
        for y in sortlist:
            calc.append(messagecount[y])

        stdd = std(calc)
        mean1 = int(mean(calc).round())
        for s in messagecount:
            if (messagecount[s]) > (mean1 + stdd) or (messagecount[s]) < (mean1 - stdd):
                calc.remove(messagecount[s])
                ood.append(s)
        mean2 = int(mean(calc).round())

        for y in sortlist:
            splitter = y.split(" ")
            uppered = []
            for p in splitter:
                uppered.append(p[0].upper() + p[1:])

            file1.writelines(" ".join(uppered) + ": " + str(messagecount[y]) + "\n")
            file1.writelines("Percent deviation: " + str(round(messagecount[y]/mean2 * 100)) + "%\n\n")
        file1.writelines("\nMean with outliers: " + str(mean1))
        file1.writelines("\nOutliers: \n")
        for l in ood:
            file1.writelines((" " * 9) + l + ": " + str(messagecount[l]) + "\n")
        file1.writelines("\nMean without outliers: " + str(mean2))
        file1.close()

    with open(os.path.join(os.getcwd(), filename.split("/")[len(filename.split("/")) - 1].replace(".txt", "")) + "_messagelog.txt", "w+") as file2:
        sortlist = [x for x in studentlist]
        sortlist.sort()
        for y in sortlist:
            count = 1
            splitter = y.split(" ")
            uppered = []
            for p in splitter:
                uppered.append(p[0].upper() + p[1:])
            file2.writelines(" ".join(uppered) + ":" + "\n")
            for x in studentlist[y]:
                file2.writelines((" " * (len(y) + 1)) + str(count) + ". " + x + "\n")
                count += 1
        file2.close()
except Exception as e:
    print(str(e))
