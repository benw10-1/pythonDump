from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib, ssl, string, random
from PyQt5.QtWidgets import QMessageBox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global ran
        ran = [False]*3
        msg1 = QMessageBox()
        msg1.setWindowTitle("EmailSender")
        msg1.setText("Remember to set your newly created gmail to \"enable\" less secure applications(Look it up if you don't know how)")
        msg1.setIcon(QMessageBox.Information)
        x = msg1.exec_()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 543)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.windowIcon = "C:/Users/benja/Downloads/Benjamin Wirth - IMG_2353"

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
        self.codefinder.setGeometry(QtCore.QRect(11, 449, 133, 20))
        self.codefinder.setObjectName("codefinder")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 451, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.checkcodebut = QtWidgets.QPushButton(self.centralwidget)
        self.checkcodebut.setGeometry(QtCore.QRect(11, 475, 75, 23))
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
        self.visualtxt.setReadOnly(True)
        self.visualtxt.setPlainText("")
        self.visualtxt.setObjectName("visualtxt")
        self.scrollbox.setWidget(self.scrollAreaWidgetContents)
        self.subjectset = QtWidgets.QPushButton(self.centralwidget)
        self.subjectset.setGeometry(QtCore.QRect(10, 256, 75, 23))
        self.subjectset.setObjectName("subjectset")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.codefinder_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.codefinder_2.setGeometry(QtCore.QRect(10, 230, 133, 20))
        self.codefinder_2.setText("")
        self.codefinder_2.setObjectName("codefinder_2")
        self.loginuser = QtWidgets.QLineEdit(self.centralwidget)
        self.loginuser.setGeometry(QtCore.QRect(42, 114, 111, 20))
        self.loginuser.setText("")
        self.loginuser.setObjectName("loginuser")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 90, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.loginpass = QtWidgets.QLineEdit(self.centralwidget)
        self.loginpass.setGeometry(QtCore.QRect(42, 140, 111, 20))
        self.loginpass.setText("")
        self.loginpass.setObjectName("loginpass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 31, 21))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 140, 31, 21))
        self.label_10.setObjectName("label_10")
        self.emailsetter = QtWidgets.QPushButton(self.centralwidget)
        self.emailsetter.setGeometry(QtCore.QRect(60, 170, 75, 21))
        self.emailsetter.setObjectName("emailsetter")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.outputtxtname = QtWidgets.QLineEdit(self.centralwidget)
        self.outputtxtname.setGeometry(QtCore.QRect(10, 320, 133, 20))
        self.outputtxtname.setObjectName("outputtxtname")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 298, 92, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 350, 131, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 370, 131, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 390, 51, 16))
        self.label_14.setObjectName("label_14")
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
        self.uploadfilebut.clicked.connect(self.uploadFile1)
        self.emailsetter.clicked.connect(self.setuserpass)
        self.subjectset.clicked.connect(self.setsubj)
        self.sendemailsbut.clicked.connect(self.sendemails)
        self.pushButton.clicked.connect(self.uploadFile2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EmailsUI"))
        self.uploadfilebut.setText(_translate("MainWindow", "Upload File"))
        self.label.setText(_translate("MainWindow", "List of emails.txt from txt file"))
        self.sendemailsbut.setText(_translate("MainWindow", "Send Emails"))
        self.label_2.setText(_translate("MainWindow", "Format is: "))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.checkcodebut.setText(_translate("MainWindow", "Check Code"))
        self.subjectset.setText(_translate("MainWindow", "Set"))
        self.label_8.setText(_translate("MainWindow", "Subject of email"))
        self.label_9.setText(_translate("MainWindow", "Login for email(gmail only!)"))
        self.label_5.setText(_translate("MainWindow", "User:"))
        self.label_10.setText(_translate("MainWindow", "Pass:"))
        self.emailsetter.setText(_translate("MainWindow", "Set"))
        self.label_11.setText(_translate("MainWindow", "Not set"))
        self.pushButton.setText(_translate("MainWindow", "Upload File"))
        self.label_7.setText(_translate("MainWindow", "Output txt name"))
        self.label_12.setText(_translate("MainWindow", "If you closed the app after"))
        self.label_13.setText(_translate("MainWindow", "sending emails.txt upload file"))
        self.label_14.setText(_translate("MainWindow", "with codes"))
        self.menuZoom_Codes_Plus_Email_App.setTitle(_translate("MainWindow", "Zoom Codes Plus Email App"))
        self.menuMade_By.setTitle(_translate("MainWindow", "Made By"))
        self.actionBen_W.setText(_translate("MainWindow", "Ben W (With Qt Designer)"))

    def error(self, error):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(error)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


    def uploadFile1(self):
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
    
            for x in data:
                i += 1
            z = (i+1)/2
            data2="".join(data)
            
            try:
                names = [None]*z.__trunc__()
                emails = [None]*z.__trunc__()
            except:
                return 0

            for y in data:
                if y == "\n":
                    self.error("Incorrect format")
                    names=[""]
                    emails=[""]
                    return 0
                if (k/2).__trunc__() == k/2:
                    names[j] = y.strip()
                    j += 1
                else:
                    if "@" not in y:
                        self.error("Incorrect format")
                        emails =[""]
                        names =[""]
                        return 0
                    emails[l]=y.strip()
                    l+=1

                k += 1
            
            self.visualtxt.setPlainText(data2)
            ran[0]=(True)
            f.close()


    def uploadFile2(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Txt File", "", "Txt Files (*.txt)")
        i = 0
        a = 0
        final = []
        global code1
        if filename:
            g = open (filename, "r")
            
            with g:
                imported = g.readlines()
            for x in imported:
                i += 1
            code1 = [None]*(i+1)
            for y in imported:
                if "#" not in y:
                    self.error("Wrong file")
                    return 0
                code1[a] = y.split("#")
                a += 1
            for p in imported:
                final.append(p.strip()+": \n")
                
            self.visualtxt.setPlainText("".join(final))
            

    def setuserpass(self):
        global username
        global password
        port = 465

        smtp_server = "smtp.gmail.com"
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        except Exception as e:
            print(e)
            self.error("Connection failed")
            self.loginuser.clear()
            self.loginpass.clear()
            return 0

        username = self.loginuser.text()
        password = str(self.loginpass.text())
        print (username)
        print (password)
        if not username or not password:
            self.error("Please enter a username AND a password")
            self.loginuser.clear()
            self.loginpass.clear()
            return 0
        try:
            server.login(username + "@gmail.com", password)
        except:
            self.error("Error with email server(maybe wronge username or password)")
        self.loginuser.clear()
        self.loginpass.clear()
        if username and password != "":
            ran[1] = True
        else:
            ran[1] = False
        
        self.label_11.setText("Set")


    def setsubj(self):
        global subj
        subj = str(self.codefinder_2.text())
        if subj == "":
            self.error("No subject")
            return 0
        self.codefinder_2.clear()
        ran[2]=True

    def sendemails(self):
        if not ran[0]:
            self.error("No file uploaded")
            return 0
        if self.outputtxtname.text() == "":
            self.error("No output name")
            return 0
        if not ran[1]:
            self.error("No username or password")
            return 0
        if not ran[2]:
            self.error("No subject")
            return 0

        j=0
        try:
            thissub = subj
        except Exception as e:
            print(e)
        port = 465
        
        smtp_server = "smtp.gmail.com"
        
        message = "Subject: " + thissub
        
        
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(username+"@gmail.com", password)
        
        global old
        old = ""
        try:
            code = [None] * i
        except Exception as e:
            print (e)
        try:
            while j < (i/2).__trunc__():
                
                code[j] = "".join(random.choice(string.digits) for i in range(4))
                
                ppp=code[j]
                
                lll=names[j].strip()+"#"+ppp.strip()
                print (lll)
                server.sendmail(username, emails[j],message+"\nDear: "+names[j]+"\nWrite your name exactly as indicated below BEFORE entering the waiting room.\n"+lll+"\nRemember, this code changes for every class and you will not be let in without the appropriate name.\nThank you, Dolores")
            
                new = lll+"\n"
                old = old + new
                self.visualtxt.setPlainText(old)
                
                j = j + 1
        except Exception as e:
            print (e)
        try:
            file2 = open(self.outputtxtname.text()+"_log.txt","w+")
            file2.write(old)
            file2.close()
        except:
            pass


        def checkCode(self):
            codecheck = self.codefinder.text()
            self.codefinder.clear()
            print (code1)
            


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
