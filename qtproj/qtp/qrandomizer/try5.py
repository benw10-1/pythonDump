from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit

from PyQt5.QtGui import QPixmap

picts = [None]*500
txt = [None]*500
used = [False]*500

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global picts


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 390, 591, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Inpuptext = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Inpuptext.setObjectName("Inpuptext")
        self.verticalLayout.addWidget(self.Inpuptext)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pixmaper = QtWidgets.QLabel(self.centralwidget)
        self.pixmaper.setGeometry(QtCore.QRect(610, 400, 171, 141))
        self.pixmaper.setObjectName("pixmaper")
        self.imgchooser = QtWidgets.QPushButton(self.centralwidget)
        self.imgchooser.setGeometry(QtCore.QRect(650, 360, 91, 23))
        self.imgchooser.setObjectName("imgchooser")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItem("Question 1")

        self.imgchooser.clicked.connect(self.pic)
        self.comboBox.activated.connect(self.holder)
        self.Inpuptext.textChanged.connect(self.texter)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgchooser.setText(_translate("MainWindow", "Upload Image"))


    def pic(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Images (*.jpg .webm .png)")

        pixmap = QPixmap(filename)
        pixmap2 = pixmap.scaled(self.pixmaper.width(),self.pixmaper.height())

        self.pixmaper.setPixmap(pixmap2)

        picts[self.comboBox.currentIndex()] = pixmap2




    def holder(self):

        print("yee")
        if picts[self.comboBox.currentIndex()] != None:
            self.pixmaper.setPixmap(picts[self.comboBox.currentIndex()])

        if txt[self.comboBox.currentIndex()] != None or "":

            self.Inpuptext.setText(txt[self.comboBox.currentIndex()])
        if txt[self.comboBox.currentIndex()] == None or "":
            self.Inpuptext.setText("")
        print(txt[self.comboBox.currentIndex()])



    def texter(self):
        if not used[self.comboBox.currentIndex()]:
            if self.Inpuptext.toPlainText() != "" or None:
                if self.comboBox.currentIndex() == 0:
                    used[self.comboBox.currentIndex()] = True
                    self.comboBox.addItem("Question 2")

                else:

                    used[self.comboBox.currentIndex()] = True
                    b = self.comboBox.currentIndex() + 2
                    self.comboBox.addItem(f"Question {b}")
        txt[self.comboBox.currentIndex()] = self.Inpuptext.toPlainText()
        print (str(self.comboBox.currentIndex())+ ". "+txt[self.comboBox.currentIndex()])





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
