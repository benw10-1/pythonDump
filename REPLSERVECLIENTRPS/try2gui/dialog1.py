from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_rpshand(object):
    def setupUi(self, rpshand):
        rpshand.setObjectName("rpshand")
        rpshand.resize(323, 113)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        rpshand.setPalette(palette)
        self.playingvs = QtWidgets.QLabel(rpshand)
        self.playingvs.setGeometry(QtCore.QRect(40, 0, 221, 20))
        self.playingvs.setObjectName("playingvs")
        self.pushButton = QtWidgets.QPushButton(rpshand)
        self.pushButton.setGeometry(QtCore.QRect(203, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(rpshand)
        self.pushButton_2.setGeometry(QtCore.QRect(122, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(rpshand)
        self.pushButton_3.setGeometry(QtCore.QRect(41, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.loading = QtWidgets.QLabel(rpshand)
        self.loading.setGeometry(QtCore.QRect(40, 70, 41, 31))
        self.loading.setText("")
        self.gif = QMovie('C:/Users/benja/Downloads/loading.gif')
        self.loading.setMovie(self.gif)
        self.gif.start()
        self.loading.setObjectName("loading")
        self.waitingfor = QtWidgets.QLabel(rpshand)
        self.waitingfor.setGeometry(QtCore.QRect(100, 80, 151, 16))
        self.waitingfor.setObjectName("waitingfor")

        self.retranslateUi(rpshand)
        QtCore.QMetaObject.connectSlotsByName(rpshand)

    def retranslateUi(self, rpshand):
        _translate = QtCore.QCoreApplication.translate
        rpshand.setWindowTitle(_translate("rpshand", "RPS"))
        self.playingvs.setText(_translate("rpshand", " Playing versus:"))
        self.pushButton.setText(_translate("rpshand", "Scissors"))
        self.pushButton_2.setText(_translate("rpshand", "Paper"))
        self.pushButton_3.setText(_translate("rpshand", "Rock"))
        self.waitingfor.setText(_translate("rpshand", "Waiting for "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rpshand = QtWidgets.QMainWindow()
    ui = Ui_rpshand()
    ui.setupUi(rpshand)
    rpshand.show()
    sys.exit(app.exec_())
