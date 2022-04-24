# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\benja\Desktop\qtp\try1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib, ssl, string, random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global username
        global password
        global subj
        global ran1
        global ran2
        global ran3
        global ran4
        global ran5
        global i
        global names
        global emails
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 543)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadfilebut = QtWidgets.QPushButton(self.centralwidget)
        self.uploadfilebut.setEnabled(True)
        self.uploadfilebut.setGeometry(QtCore.QRect(262, 22, 75, 23))
        self.uploadfilebut.setCheckable(False)
        self.uploadfilebut.setObjectName("uploadfilebut")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 21, 253, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sendemailsbut = QtWidgets.QPushButton(self.centralwidget)
        self.sendemailsbut.setGeometry(QtCore.QRect(385, 22, 75, 23))
        self.sendemailsbut.setObjectName("sendemailsbut")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(2, 51, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 52, 27, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 71, 24, 16))
        self.label_4.setObjectName("label_4")
        self.codefinder = QtWidgets.QLineEdit(self.centralwidget)
        self.codefinder.setGeometry(QtCore.QRect(10, 354, 133, 20))
        self.codefinder.setObjectName("codefinder")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 332, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.checkcodebut = QtWidgets.QPushButton(self.centralwidget)
        self.checkcodebut.setGeometry(QtCore.QRect(10, 380, 75, 23))
        self.checkcodebut.setObjectName("checkcodebut")
        self.scrollbox = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollbox.setGeometry(QtCore.QRect(160, 80, 541, 421))
        self.scrollbox.setWidgetResizable(True)
        self.scrollbox.setObjectName("scrollbox")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.visualtxt = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.visualtxt.setGeometry(QtCore.QRect(-1, -1, 541, 421))
        self.visualtxt.setReadOnly(False)
        self.visualtxt.setObjectName("visualtxt")
        self.scrollbox.setWidget(self.scrollAreaWidgetContents)
        self.subjectset = QtWidgets.QPushButton(self.centralwidget)
        self.subjectset.setGeometry(QtCore.QRect(10, 286, 75, 23))
        self.subjectset.setObjectName("subjectset")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 240, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.codefinder_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.codefinder_2.setGeometry(QtCore.QRect(10, 260, 133, 20))
        self.codefinder_2.setText("")
        self.codefinder_2.setObjectName("codefinder_2")
        self.loginuser = QtWidgets.QLineEdit(self.centralwidget)
        self.loginuser.setGeometry(QtCore.QRect(42, 144, 111, 20))
        self.loginuser.setText("")
        self.loginuser.setObjectName("loginuser")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 120, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.loginpass = QtWidgets.QLineEdit(self.centralwidget)
        self.loginpass.setGeometry(QtCore.QRect(42, 170, 111, 20))
        self.loginpass.setText("")
        self.loginpass.setObjectName("loginpass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 31, 21))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 31, 21))
        self.label_10.setObjectName("label_10")
        self.emailsetter = QtWidgets.QPushButton(self.centralwidget)
        self.emailsetter.setGeometry(QtCore.QRect(60, 200, 75, 21))
        self.emailsetter.setObjectName("emailsetter")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 422, 92, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.outputtxtname = QtWidgets.QLineEdit(self.centralwidget)
        self.outputtxtname.setGeometry(QtCore.QRect(10, 444, 133, 20))
        self.outputtxtname.setObjectName("outputtxtname")
        self.outputtxtbut = QtWidgets.QPushButton(self.centralwidget)
        self.outputtxtbut.setGeometry(QtCore.QRect(10, 470, 75, 23))
        self.outputtxtbut.setObjectName("outputtxtbut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        self.menuZoom_Codes_Plus_Email_App = QtWidgets.QMenu(self.menubar)
        self.menuZoom_Codes_Plus_Email_App.setObjectName("menuZoom_Codes_Plus_Email_App")
        self.menuMade_By = QtWidgets.QMenu(self.menuZoom_Codes_Plus_Email_App)
        self.menuMade_By.setObjectName("menuMade_By")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBen_W = QtWidgets.QAction(MainWindow)
        self.actionBen_W.setObjectName("actionBen_W")
        self.menuMade_By.addAction(self.actionBen_W)
        self.menuZoom_Codes_Plus_Email_App.addAction(self.menuMade_By.menuAction())
        self.menubar.addAction(self.menuZoom_Codes_Plus_Email_App.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.uploadfilebut.clicked.connect(self.uploadFile)
        self.emailsetter.clicked.connect(self.setuserpass)
        self.subjectset.clicked.connect(self.setsubj)
        self.sendemailsbut.clicked.connect(self.sendemails)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EmailsUI"))
        self.uploadfilebut.setText(_translate("MainWindow", "Upload File"))
        self.label.setText(_translate("MainWindow", "List of emails.txt from txt file"))
        self.sendemailsbut.setText(_translate("MainWindow", "Send Emails"))
        self.label_2.setText(_translate("MainWindow", "Format is: "))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_6.setText(_translate("MainWindow", "Enter code"))
        self.checkcodebut.setText(_translate("MainWindow", "Check Code"))
        self.visualtxt.setPlainText(_translate("MainWindow", "\n"
"\n"
""))
        self.subjectset.setText(_translate("MainWindow", "Set"))
        self.label_8.setText(_translate("MainWindow", "Subject of email"))
        self.label_9.setText(_translate("MainWindow", "Login for email(gmail only!)"))
        self.label_5.setText(_translate("MainWindow", "User:"))
        self.label_10.setText(_translate("MainWindow", "Pass:"))
        self.emailsetter.setText(_translate("MainWindow", "Set"))
        self.label_7.setText(_translate("MainWindow", "Output txt name"))
        self.outputtxtbut.setText(_translate("MainWindow", "Output"))
        self.menuZoom_Codes_Plus_Email_App.setTitle(_translate("MainWindow", "Zoom Codes Plus Email App"))
        self.menuMade_By.setTitle(_translate("MainWindow", "Made By"))
        self.actionBen_W.setText(_translate("MainWindow", "Ben W (With Qt Designer)"))

    def uploadFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Txt File", "", "Txt Files (*.txt)")
        global i
        i=0
        j=0
        l=0
        k=0
        global emails
        global names
        if filename:
            f = open(filename, 'r')
            
            with f:
                data = f.readlines()                
                print(data)    
            for x in data:
                i += 1
            z = (i+1)/2
            data2="".join(data)
            print(data2)
            try:
                names = [None]*z.__trunc__()
                emails = [None]*z.__trunc__()
            except:
                return 0

            for y in data:
                
                if (k/2).__trunc__() == k/2:
                    names[j] = y.strip()
                    j += 1
                else:
                    emails[l]=y.strip()
                    l+=1

                k += 1
            print(names)
            print(emails)
            self.visualtxt.setPlainText(data2)
            ran1 = True
            f.close()


    def setuserpass(self):
        global username
        global password
        username = self.loginuser.text()
        password = str(self.loginpass.text())
        print (username)
        print (password)
        print (type(username))
        self.loginuser.clear()
        self.loginpass.clear()
        if username and password != "":
            ran2 = True
        else:
            ran2 = False
        
        print (str(ran2))


    def setsubj(self):
        global subj
        subj = str(self.codefinder_2.text())
        print (subj)
        self.codefinder_2.clear()
        
        
    def sendemails(self):
        print ("yes")
        j=0
        try:
            thissub = subj
        except Exception as e:
            print(e)
        port = 465
        print("yes")
        smtp_server = "smtp.gmail.com"
        print("yes")
        message = "Subject: " + thissub
        
        print ("yes")
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(username+"@gmail.com", password)
        print ("yes")
        old = ""
        try:
            code = [None] * i
        except Exception as e:
            print (e)
        try:
            while j < (i/2).__trunc__():
                print("yes")
                code[j] = "".join(random.choice(string.digits) for i in range(4))
                print ("yes")
                ppp=code[j]
                print ("yes")
                lll=names[j].strip()+"#"+ppp.strip()
                print (lll)
                server.sendmail(username, emails[j],message+"\nDear: "+names[j]+"\nWrite your name exactly as indicated below BEFORE entering the waiting room.\n"+lll+"\nRemember, this code changes for every class and you will not be let in without the appropriate name.\nThank you, Dolores")
            
                new = lll+"\n"
                old = old + new
                self.visualtxt.setPlainText(old)
                
                j = j + 1
        except Exception as e:
            print (e)
            
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
