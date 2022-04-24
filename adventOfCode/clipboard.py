import pyperclip

with open("outputs/output4.txt", "w") as file:
    file.write(pyperclip.paste())
    file.close()
