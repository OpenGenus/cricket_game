# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog3.hide)
        self.lineEdit = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 201, 91))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Dialog3"))
        self.pushButton.setText(_translate("Dialog3", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

