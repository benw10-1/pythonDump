import os

file = "form.ui"
ui_folder = "C:/Users/benja/PycharmProjects/qtproj/ui_files/attempt_1"
dest = "C:/Users/benja/PycharmProjects/qtproj/pythonuis/"

os.chdir(ui_folder)
print("cd " + ui_folder + " & " + "pyuic5 -o " + dest + file.replace(".ui", ".py") + " " + file)
os.system("cd " + ui_folder + " & " + "pyuic5 -o " + dest + file.replace(".ui", ".py") + " " + file)
