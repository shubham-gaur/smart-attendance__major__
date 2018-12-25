#!/usr/bin/env python

# ==========================================
# LOGIN SETUP

login_SourceFile = open('Login_Dialog_RAW.py', 'r')
login_SourceCode = login_SourceFile.read()
login_SourceFile.close()
login_SourceCodeSplit = login_SourceCode.split('class Ui_Login_Dialog(object):')
beginningLines = '''
#!/usr/bin/env python

import sys
import DB_manager as db
'''
login_ConstructorCode = '''
class Ui_Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('UsernamePassword_DB', 'masterTable')
        self.setupUi(self)
        self.confirm = None
        '''
login_EndCode = '''
    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    @QtCore.pyqtSignature("on_login_btn_clicked()")
    def Login_btn(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not password:
            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
        t = self.dbu.GetTable()
        print (t)
        for col in t:
            if username == col[1]:
                if password == col[2]:
                    QtGui.QMessageBox.information(self, 'BOOYA!', 'Success!!')
                    self.close()
                else:
                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                    return

    @QtCore.pyqtSignature("on_newUser_btn_clicked()")
    def NewUser_btn(self):
        self.newUser = Ui_Register(self.dbu)
        self.newUser.show()
'''

# ==========================================
# NEW USER SETUP

newUser_SourceFile = open('NewUser_Dialog_RAW.py', 'r')
newUser_SourceCode = newUser_SourceFile.read()
newUser_SourceFile.close()
newUser_SourceCodeSplit = newUser_SourceCode.split('class Ui_Register_Dialog(object):')

newUser_ConstructorCode = '''
class Ui_Register(QtGui.QDialog):
    def __init__(self, dbu):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.dbu = dbu
'''

newUser_EndCode = '''
    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    @QtCore.pyqtSignature("on_add_btn_clicked()")
    def Add_btn(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        cpassword = self.confirmPassword_lineEdit.text()
        if not username:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
        elif password != cpassword:
            QtGui.QMessageBox.warning(self, 'Dang it!', 'Passwords Do Not Match')
        else:
            t = self.dbu.GetTable()
            print (t)
            for col in t:
                if username == col[1]:
                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')
            else:
                self.dbu.AddEntryToTable (username, password)
                QtGui.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
                self.close()
'''

# ==========================================
# COMBINE IT!

finalLines = '''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Login()
    ex.show()
    sys.exit(app.exec_())
'''


f = open('Main.py', 'w')
f.write(beginningLines)
f.write(login_SourceCodeSplit[0])
f.write(login_ConstructorCode)
f.write(login_SourceCodeSplit[1])
f.write(login_EndCode)

f.write(newUser_ConstructorCode)
f.write(newUser_SourceCodeSplit[1])
f.write(newUser_EndCode)

f.write(finalLines)
f.close()














