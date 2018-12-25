
#!/usr/bin/env python

import sys
import DB_manager as db
import cv2
from cv2 import *
import os
import numpy as np
from PIL import Image
from os.path import join,basename
import db_connect as DB
import datetime
from datetime import datetime as date

camera_port = 0
camera = VideoCapture(camera_port)
ret, frame = camera.read()
ramp_frames = 0

faceCascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_eye.xml')

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Dialog.ui'
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

login_SourceFile = open('Login_Dialog_RAW.py', 'r')
login_SourceCode = login_SourceFile.read()
login_SourceFile.close()
login_SourceCodeSplit = login_SourceCode.split('class Ui_Login_Dialog(object):')

class Ui_Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('db', 'login')
        self.setupUi(self)
        self.confirm = None
        
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
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Admin Login", None))
        self.groupBox.setTitle(_translate("Login_Dialog", "Welcome!", None))
        self.label.setText(_translate("Login_Dialog", "Username", None))
        self.label_2.setText(_translate("Login_Dialog", "Password", None))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User", None))
        self.login_btn.setText(_translate("Login_Dialog", "Login", None))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel", None))


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
                    self.admin = admin_Ui_Dialog(self.dbu)
                    self.admin.show()
                    self.close()
                else:
                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                    return

    @QtCore.pyqtSignature("on_newUser_btn_clicked()")
    def NewUser_btn(self):
        self.newUser = Ui_Register(self.dbu)
        self.newUser.show()

admin_SourceFile = open('admin.py', 'r')
admin_SourceCode = admin_SourceFile.read()
admin_SourceFile.close()
admin_SourceCodeSplit = admin_SourceCode.split('class admin_Ui_Dialog(object):')

class admin_Ui_Dialog(QtGui.QDialog):
    def __init__(self,dbu):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.dbu = dbu
        

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(333, 295)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.logOut = QtGui.QPushButton(Dialog)
        self.logOut.setObjectName(_fromUtf8("logOut"))
        self.horizontalLayout_3.addWidget(self.logOut)
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout_3.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.addStudent = QtGui.QPushButton(self.splitter)
        self.addStudent.setObjectName(_fromUtf8("addStudent"))
        self.addTeacher = QtGui.QPushButton(self.splitter)
        self.addTeacher.setDefault(False)
        self.addTeacher.setFlat(False)
        self.addTeacher.setObjectName(_fromUtf8("addTeacher"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pushButton_3 = QtGui.QPushButton(self.splitter_2)
        self.pushButton_3.setObjectName(_fromUtf8("report"))
        self.monitor = QtGui.QPushButton(self.splitter_2)
        self.monitor.setObjectName(_fromUtf8("monitor"))
        self.gridLayout.addWidget(self.splitter_2, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.logOut.setText(_translate("Dialog", "Log out", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))
        self.groupBox.setTitle(_translate("Dialog", "Welcome", None))
        self.addStudent.setText(_translate("Dialog", "Add Student", None))
        self.addTeacher.setText(_translate("Dialog", "Add Teacher", None))
        self.pushButton_3.setText(_translate("Dialog", "Report", None))
        self.monitor.setText(_translate("Dialog", "Monitor", None))

    @QtCore.pyqtSignature("on_cancel_clicked()")
    def Cancel_btn(self):
        self.close()

    @QtCore.pyqtSignature("on_addTeacher_clicked()")
    def addTeacher_btn(self):
        self.add_Teacher = add_Teacher_Dialog(self.dbu)
        self.add_Teacher.show()

    @QtCore.pyqtSignature("on_addStudent_clicked()")
    def addStudent_btn(self):
        self.studentForm = student_Ui_Dialog(self.dbu)
        self.studentForm.show()

    @QtCore.pyqtSignature("on_monitor_clicked()")
    def start(self):
    	execfile("face_recognizer.py")
        #execfile("latest.py")

    @QtCore.pyqtSignature("on_report_clicked()")
    def Report_btn(self):
        self.reportForm = report_Dialog(self.dbu)
        self.reportForm.show()

reportForm_SourceFile = open('report.py', 'r')
reportForm_SourceCode = reportForm_SourceFile.read()
reportForm_SourceFile.close()
reportForm_SourceCodeSplit = reportForm_SourceCode.split('class report_Dialog(object):')
class report_Dialog(QtGui.QDialog):
    def __init__(self,dbu):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('db', 'master')
        self.setupUi(self)
        self.confirm = None
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(602, 536)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(Dialog)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.search = QtGui.QLineEdit(self.widget)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textBrowser = QtGui.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.buttonBox = QtGui.QDialogButtonBox(self.splitter)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Search by  :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Enrollment", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Date", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Subect", None))
        self.pushButton.setText(_translate("Dialog", "Search", None))



studentForm_SourceFile = open('studentform.py', 'r')
studentForm_SourceCode = studentForm_SourceFile.read()
studentForm_SourceFile.close()
studentForm_SourceCodeSplit = studentForm_SourceCode.split('class student_Ui_Dialog(object):')
class student_Ui_Dialog(QtGui.QDialog):
    def __init__(self,dbu):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('db', 'student')
        self.setupUi(self)
        self.confirm = None
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(494, 295)
        Dialog.setMinimumSize(QtCore.QSize(494, 289))
        Dialog.setMaximumSize(QtCore.QSize(494, 295))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line_6 = QtGui.QFrame(self.groupBox)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_2.addWidget(self.line_6, 3, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 0, 1, 1, 1)
        self.year_Spin = QtGui.QSpinBox(self.groupBox)
        self.year_Spin.setMinimumSize(QtCore.QSize(72, 0))
        self.year_Spin.setMinimum(1)
        self.year_Spin.setMaximum(4)
        self.year_Spin.setObjectName(_fromUtf8("year_Spin"))
        self.gridLayout_2.addWidget(self.year_Spin, 3, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.line_5 = QtGui.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.name = QtGui.QLineEdit(self.groupBox)
        self.name.setMinimumSize(QtCore.QSize(215, 20))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.enroll = QtGui.QLineEdit(self.groupBox)
        self.enroll.setMinimumSize(QtCore.QSize(215, 0))
        self.enroll.setObjectName(_fromUtf8("enroll"))
        self.gridLayout_2.addWidget(self.enroll, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.line_4 = QtGui.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 1, 1, 1, 1)
        self.branch_Combo = QtGui.QComboBox(self.groupBox)
        self.branch_Combo.setMinimumSize(QtCore.QSize(70, 0))
        self.branch_Combo.setObjectName(_fromUtf8("branch_Combo"))
        self.branch_Combo.addItem(_fromUtf8(""))
        self.branch_Combo.addItem(_fromUtf8(""))
        self.branch_Combo.addItem(_fromUtf8(""))
        self.branch_Combo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.branch_Combo, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.display_btn = QtGui.QPushButton(self.layoutWidget1)
        self.display_btn.setObjectName(_fromUtf8("display_btn"))
        self.horizontalLayout_2.addWidget(self.display_btn)
        self.add_btn = QtGui.QPushButton(self.layoutWidget1)
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.horizontalLayout_2.addWidget(self.add_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name, self.enroll)
        Dialog.setTabOrder(self.enroll, self.branch_Combo)
        Dialog.setTabOrder(self.branch_Combo, self.year_Spin)
        Dialog.setTabOrder(self.year_Spin, self.display_btn)
        Dialog.setTabOrder(self.display_btn, self.add_btn)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_3.setText(_translate("Dialog", "Branch", None))
        self.branch_Combo.setItemText(0, _translate("Dialog", "CSE", None))
        self.branch_Combo.setItemText(1, _translate("Dialog", "IT", None))
        self.branch_Combo.setItemText(2, _translate("Dialog", "MECH", None))
        self.branch_Combo.setItemText(3, _translate("Dialog", "CIVIL", None))
        self.label_2.setText(_translate("Dialog", "Enrollment No.", None))
        self.label_4.setText(_translate("Dialog", "Year", None))
        self.display_btn.setText(_translate("Dialog", "Dislpay", None))
        self.add_btn.setText(_translate("Dialog", "Add", None))

    def valuechange(self):
        self.year_Spin.value()

    @QtCore.pyqtSignature("on_display_btn_clicked()")   
    def Display_btn(self):
        name = self.lineEdit.text()
        enrollment = self.lineEdit_2.text()
        branch = self.comboBox.currentText()
        year = str(self.spinBox.value())
        QtGui.QMessageBox.information(self, enrollment , year)

    @QtCore.pyqtSignature("on_add_btn_clicked()")
    def Add_btn(self):
        name = self.name.text()
        enrollment = self.enroll.text()
        branch = self.branch_Combo.currentText()
        year = str(self.year_Spin.value())
        if not name:
            QtGui.QMessageBox.warning(self, 'Name Missing', 'Enter Name')
        elif not enrollment:
            QtGui.QMessageBox.warning(self, 'Enrollment Missing', 'Enter Enrollment')
        elif not branch:
            QtGui.QMessageBox.warning(self, '', 'Enter Branch')
        elif not year:
            QtGui.QMessageBox.warning(self, '', 'Enter Year')
        else:
            t = self.dbu.GetTable()
            print t
            for col in t:
                if enrollment == col[0]:
                    QtGui.QMessageBox.warning(self, 'Check Enrollment', 'Enrollment can\'t be duplicate')
                else:
                    self.dbu.AddEntryToStudent (name,enrollment,branch,year)
                    QtGui.QMessageBox.information(self, 'Awesome!!', 'Student Information Added')
                    self.close()
                    break
                                    
add_TeacherForm_SourceFile = open('Add_teacher.py', 'r')
add_TeacherForm_SourceCode = add_TeacherForm_SourceFile.read()
add_TeacherForm_SourceFile.close()
add_TeacherForm_SourceCodeSplit = add_TeacherForm_SourceCode.split('class add_Teacher_Dialog(object):')
class add_Teacher_Dialog(QtGui.QDialog):
    def __init__(self,dbu):
        QtGui.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('db', 'faculty')
        self.setupUi(self)
        self.confirm = None
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(257, 138)
        Dialog.setMaximumSize(QtCore.QSize(424, 138))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(424, 89))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.teacher_name = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacher_name.sizePolicy().hasHeightForWidth())
        self.teacher_name.setSizePolicy(sizePolicy)
        self.teacher_name.setObjectName(_fromUtf8("teacher_name"))
        self.horizontalLayout_2.addWidget(self.teacher_name)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(24, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.subject_name = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_name.sizePolicy().hasHeightForWidth())
        self.subject_name.setSizePolicy(sizePolicy)
        self.subject_name.setObjectName(_fromUtf8("subject_name"))
        self.horizontalLayout_3.addWidget(self.subject_name)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label.raise_()
        self.teacher_name.raise_()
        self.label_2.raise_()
        self.subject_name.raise_()
        self.subject_name.raise_()
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.back = QtGui.QPushButton(Dialog)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout.addWidget(self.back)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Add Teacher", None))
        self.label.setText(_translate("Dialog", "Teacher\'s Name", None))
        self.label_2.setText(_translate("Dialog", "Subject", None))
        self.pushButton.setText(_translate("Dialog", "Add", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))
        self.back.setText(_translate("Dialog", "Back", None))

    @QtCore.pyqtSignature("on_pushButton_clicked()")
    def Add(self):
        teacherName = self.teacher_name.text()
        subject = self.subject_name.text()
        QtGui.QMessageBox.information(self, 'Awesome!!', 'Faculty Information Added')
        if not teacherName:
            QtGui.QMessageBox.warning(self, 'Name Missing', 'Enter Name')
        elif not subject:
            QtGui.QMessageBox.warning(self, 'Subject Missing', 'Enter Subject')
        else:
            t = self.dbu.GetTable()
            print (t)
            for col in t:
                if teacherName == col[0]:
                    QtGui.QMessageBox.warning(self, '','Faculty already added')
                else:
                    self.dbu.AddEntryToFaculty(teacherName,subject)
                    self.close()
                    break
                    QtGui.QMessageBox.information(self, 'Awesome!!', 'Faculty Information Added')
             
    @QtCore.pyqtSignature("on_cancel_clicked()")
    def Cancel(self):
        self.close()


        
newUser_SourceFile = open('NewUser_Dialog_RAW.py', 'r')
newUser_SourceCode = newUser_SourceFile.read()
newUser_SourceFile.close()
newUser_SourceCodeSplit = newUser_SourceCode.split('class Ui_Register_Dialog(object):')
class Ui_Register(QtGui.QDialog):
    def __init__(self, dbu):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.dbu = dbu

    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName(_fromUtf8("Register_Dialog"))
        Register_Dialog.resize(372, 187)
        Register_Dialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Register_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Register_Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.username_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.confirmPassword_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.confirmPassword_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmPassword_lineEdit.setObjectName(_fromUtf8("confirmPassword_lineEdit"))
        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtGui.QPushButton(self.groupBox)
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

    def retranslateUi(self, Register_Dialog):
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User", None))
        self.groupBox.setTitle(_translate("Register_Dialog", "Credentials", None))
        self.label_2.setText(_translate("Register_Dialog", "Username", None))
        self.label.setText(_translate("Register_Dialog", "Password", None))
        self.label_3.setText(_translate("Register_Dialog", "Confirm Password", None))
        self.label_4.setText(_translate("Register_Dialog", "Not Included: Phone, Address, Social Security Number, Credit Card...", None))
        self.add_btn.setText(_translate("Register_Dialog", "Add", None))
        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel", None))


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
                self.dbu.AddEntryToAdmin (username, password)
                QtGui.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
                self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Login()
    ex.show()
    sys.exit(app.exec_())
