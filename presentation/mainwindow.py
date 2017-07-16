# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 368)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.selectList = QtWidgets.QComboBox(self.centralWidget)
        self.selectList.setObjectName("selectList")
        self.horizontalLayout.addWidget(self.selectList, 0, QtCore.Qt.AlignTop)
        self.song_shower = QtWidgets.QScrollArea(self.centralWidget)
        self.song_shower.setWidgetResizable(True)
        self.song_shower.setObjectName("song_shower")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 357, 304))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.song_shower.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.song_shower)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuManage = QtWidgets.QMenu(self.menuBar)
        self.menuManage.setObjectName("menuManage")
        self.menuPlayback = QtWidgets.QMenu(self.menuBar)
        self.menuPlayback.setObjectName("menuPlayback")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.btnAddPlay = QtWidgets.QAction(MainWindow)
        self.btnAddPlay.setObjectName("btnAddPlay")
        self.actionDelete_Playlist = QtWidgets.QAction(MainWindow)
        self.actionDelete_Playlist.setObjectName("actionDelete_Playlist")
        self.menuManage.addAction(self.btnAddPlay)
        self.menuManage.addAction(self.actionDelete_Playlist)
        self.menuBar.addAction(self.menuManage.menuAction())
        self.menuBar.addAction(self.menuPlayback.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "List"))
        self.menuManage.setTitle(_translate("MainWindow", "Manage"))
        self.menuPlayback.setTitle(_translate("MainWindow", "Playback"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.btnAddPlay.setText(_translate("MainWindow", "Add playlist"))
        self.actionDelete_Playlist.setText(_translate("MainWindow", "Delete Playlist"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

