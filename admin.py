# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
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
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
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


