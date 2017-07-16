#!/usr/lib/python3.5

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from presentation.basicControls import Ui_MainWindow
import presentation.addPlaylist as addPlay
import presentation.delete_playlist as deletePlay
import presentation.signin as signIn
import presentation.signup as signUp
import dataAccess.dataAccess as dataAccess
import entities.musicEntities as me
import commands
from time import sleep

class GUIApp(Ui_MainWindow):
    def say_hi():
        print("Hello!")
    
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        
mainwindow = None
class GUIlist(QtWidgets.QWidget):
    def __init__(self):
        
        QtWidgets.QWidget.__init__(self)
        self.ui = addPlay.Ui_Dialog()
        self.ui.setupUi(self)

class GUIdelete(QtWidgets.QWidget):
    def __init__(self):
        
        QtWidgets.QWidget.__init__(self)
        self.ui = deletePlay.Ui_Dialog()
        self.ui.setupUi(self)
    
class GUISignIn(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = signIn.Ui_Dialog()
        self.ui.setupUi(self)
        
class GUISignUp(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = signUp.Ui_Dialog()
        self.ui.setupUi(self)

def already_in_list(ls, new):
    for x in ls:
        if x.id == new.id:
            return True
    
    return False

def create_playlist():
    lists = dataAccess.load_songs()
    new_playlist = me.Playlist(child_frame.ui.lineEdit.text())
    new_playlist.service = str(child_frame.ui.comboBox.currentText())
    
    if not already_in_list(lists, new_playlist):
        lists.append(new_playlist)
        dataAccess.json_pickle(lists)
        child_frame.close()

def load_songs_view():
    lists = dataAccess.load_songs()
    
    child_frame2.ui.listWidget.clear()
    
    for x in lists:
        child_frame2.ui.listWidget.addItem(x.name if x.name else str(x.id))

def remove_playlist():
    lists = dataAccess.load_songs()
    for x in lists:
        curr = child_frame2.ui.listWidget.currentItem().text()
        if x.id == curr or x.name == curr:
            lists.remove(x)
            dataAccess.json_pickle(lists)
            dataAccess.delete_playlist(x.id)
            load_songs_view()
            break

def delete_playlist():
    global child_frame2
    #app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    child_frame2 = GUIdelete()
    
    #ui.setupUi(Dialog)
    
    load_songs_view()
    
    child_frame2.ui.pushButton.clicked.connect(remove_playlist)
    child_frame2.setWindowTitle('Delete Playlist')
    child_frame2.show()

def add_playlist():
    global child_frame
    #app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    child_frame = GUIlist()
    
    #ui.setupUi(Dialog)
    
    child_frame.ui.pushButton.clicked.connect(create_playlist)
    #child_frame.setWindowTitle('Add playlist')
    child_frame.ui.comboBox.addItems(me.supported_services)
    child_frame.setWindowTitle('Add playlist')
    child_frame.show()

def sign_in():
    global child_signIn
    #app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    child_signIn = GUISignIn()
    
    #ui.setupUi(Dialog)
    
    child_signIn.ui.signBtn.clicked.connect(create_playlist)
    #child_frame.setWindowTitle('Add playlist')
    child_signIn.setWindowTitle('Sign In')
    child_signIn.show()
    
    
    
def sign_up():
    global child_signUp
    #app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    child_signUp = GUISignIn()
    
    #ui.setupUi(Dialog)
    
    child_signUp.ui.signBtn.clicked.connect(create_playlist)
    #child_signUp.setWindowTitle('Add playlist')
    child_signUp.ui.comboBox.addItems(me.supported_services)
    child_signUp.setWindowTitle('Sign Up')
    child_signUp.show()
    
def check_login():
    global session_user, mainwindow
    session_user = dataAccess.current_user()
    valid = bool(session_user.login())
    
    if valid:
        ui.startBtn.setDisabled(False)
        ui.stopBtn.setDisabled(False)
        ui.addBtn.setDisabled(False)
        ui.removeBtn.setDisabled(False)
        ui.sgnInBtn.setDisabled(True)
        ui.sgnInBtn.setText(session_user.name)
        ui.sgnUpBtn.setText("Log out")
    else:
        mainwindow.ui.startBtn.setDisabled(True)
        mainwindow.ui.stopBtn.setDisabled(True)
        mainwindow.ui.addBtn.setDisabled(True)
        mainwindow.ui.removeBtn.setDisabled(True)
        ui.sgnInBtn.setDisabled(False)
        ui.sgnInBtn.setText("Sign in")
        ui.sgnUpBtn.setText("Sign out")        
    
    return valid
    
if __name__ == '__main__':
    app= QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('/home/louis_/Documents/Python/Projects/DeezerConnection/resources/Logo.png'))
    mainwindow = QtWidgets.QMainWindow()
    ui = GUIApp(mainwindow)
    ui.setupUi(mainwindow)
    ui.startBtn.clicked.connect(commands.start)
    ui.stopBtn.clicked.connect(commands.stop)
    ui.addBtn.clicked.connect(commands.addPlaylist)    
    ui.removeBtn.clicked.connect(commands.removePlaylist)
    ui.sgnInBtn.clicked.connect(sign_in)
    ui.sgnUpBtn.clicked.connect(sign_up)
    
    
    mainwindow.ui = ui
    
    
    
    mainwindow.setWindowTitle('SgSync')
    mainwindow.show()
    
    if not check_login():
        print("Not logged in.")
        sign_in()     
    
    sys.exit(app.exec_())
    
