# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showupdates.ui'
#
# Created: Fri Aug 09 15:41:17 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Scanning for media files, please do not close until scanning is complete.")
        Form.resize(640, 480)
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Form")


