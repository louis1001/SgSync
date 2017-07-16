# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 311)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.signBtn = QtWidgets.QPushButton(Dialog)
        self.signBtn.setGeometry(QtCore.QRect(10, 260, 101, 29))
        self.signBtn.setObjectName("signBtn")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(120, 260, 101, 29))
        self.cancelBtn.setObjectName("cancelBtn")
        self.usrnmTxt = QtWidgets.QLineEdit(Dialog)
        self.usrnmTxt.setGeometry(QtCore.QRect(10, 50, 241, 29))
        self.usrnmTxt.setObjectName("usrnmTxt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.label_2.setObjectName("label_2")
        self.pswdTxt = QtWidgets.QLineEdit(Dialog)
        self.pswdTxt.setGeometry(QtCore.QRect(10, 200, 241, 29))
        self.pswdTxt.setObjectName("pswdTxt")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.label_3.setObjectName("label_3")
        self.emailTxt = QtWidgets.QLineEdit(Dialog)
        self.emailTxt.setGeometry(QtCore.QRect(10, 120, 241, 29))
        self.emailTxt.setObjectName("emailTxt")
        self.warningLbl = QtWidgets.QLabel(Dialog)
        self.warningLbl.setGeometry(QtCore.QRect(260, 50, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.warningLbl.setFont(font)
        self.warningLbl.setText("")
        self.warningLbl.setObjectName("warningLbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.signBtn.setText(_translate("Dialog", "Sign  Up"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Email"))

