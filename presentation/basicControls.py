# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicControls.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(60, 40, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(60, 120, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stopBtn.setFont(font)
        self.stopBtn.setObjectName("stopBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(60, 200, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(60, 280, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.sgnInBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sgnInBtn.setGeometry(QtCore.QRect(180, 10, 91, 21))
        self.sgnInBtn.setObjectName("sgnInBtn")
        self.sgnUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sgnUpBtn.setGeometry(QtCore.QRect(280, 10, 91, 21))
        self.sgnUpBtn.setObjectName("sgnUpBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.addBtn.setText(_translate("MainWindow", "Add Playlist"))
        self.removeBtn.setText(_translate("MainWindow", "Remove Playlist"))
        self.sgnInBtn.setText(_translate("MainWindow", "Sign in"))
        self.sgnUpBtn.setText(_translate("MainWindow", "Sign up"))

