# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Dialog.ui'
#
# Created: Mon Nov 24 22:56:20 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName(_fromUtf8("Login_Dialog"))
        Login_Dialog.resize(285, 134)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Login_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Login_Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.user_lineEdit.setObjectName(_fromUtf8("user_lineEdit"))
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.password_lineEdit.setInputMask(_fromUtf8(""))
        self.password_lineEdit.setText(_fromUtf8(""))
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.newUser_btn = QtGui.QPushButton(self.groupBox)
        self.newUser_btn.setObjectName(_fromUtf8("newUser_btn"))
        self.horizontalLayout_4.addWidget(self.newUser_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.login_btn = QtGui.QPushButton(self.groupBox)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "TPayne\'s User Login", None))
        self.groupBox.setTitle(_translate("Login_Dialog", "Super Ham!", None))
        self.label.setText(_translate("Login_Dialog", "Username", None))
        self.label_2.setText(_translate("Login_Dialog", "Password", None))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User", None))
        self.login_btn.setText(_translate("Login_Dialog", "Login", None))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel", None))
