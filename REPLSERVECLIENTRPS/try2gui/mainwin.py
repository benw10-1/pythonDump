from PyQt5 import QtCore, QtGui, QtWidgets
from dialog1 import Ui_rpshand

codes = {"msg":"222", "challenge":"798", "error":"545", "throw":"877", "connectr":"133", "done": "099","aord":"344"}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setFixedSize(800,592)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/Untitled-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 291, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.conlist = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.conlist.setGeometry(QtCore.QRect(-1, -1, 291, 551))
        self.conlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.conlist.setObjectName("conlist")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.send = QtWidgets.QLineEdit(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(310, 530, 481, 20))
        self.send.setObjectName("send")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(310, 0, 481, 521))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 479, 519))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.chat = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.chat.setGeometry(QtCore.QRect(0, 0, 481, 521))
        self.chat.setReadOnly(True)
        self.chat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.chat.setObjectName("chat")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menuMade_by = QtWidgets.QMenu(self.menuInfo)
        self.menuMade_by.setObjectName("menuMade_by")
        self.menuHelp = QtWidgets.QMenu(self.menuInfo)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBen_W = QtWidgets.QAction(MainWindow)
        self.actionBen_W.setObjectName("actionBen_W")
        self.actionNo_help_for_now = QtWidgets.QAction(MainWindow)
        self.actionNo_help_for_now.setObjectName("actionNo_help_for_now")
        self.menuMade_by.addAction(self.actionBen_W)
        self.menuHelp.addAction(self.actionNo_help_for_now)
        self.menuInfo.addAction(self.menuMade_by.menuAction())
        self.menuInfo.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.send.returnPressed.connect(self.sendmsg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPS"))
        self.send.setPlaceholderText(_translate("MainWindow", "Send message...."))
        self.chat.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menuMade_by.setTitle(_translate("MainWindow", "Made by"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBen_W.setText(_translate("MainWindow", "Ben W"))
        self.actionNo_help_for_now.setText(_translate("MainWindow", "No help for now :("))


    def sendmsg(self):
        c.send(bytes(codes["msg"],"utf-8"))
        c.send(bytes(self.send.text(),"utf-8"))
        self.send.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
