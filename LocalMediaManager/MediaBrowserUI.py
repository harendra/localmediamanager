# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mediabrowser.ui'
#
# Created: Wed Jul 31 13:38:37 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from MediaFinder import MediaFinder
import os
from updatewidget import *
import ConfigParser
import time
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

class Updater(QtCore.QThread):
    trigger = QtCore.pyqtSignal(object,object)
    def __init__(self,obj,list_widget,value,stopwords,rootfolders):
        QtCore.QThread.__init__(self)
        self.list_widget=list_widget
        self.value=value
        self.customstopwords=stopwords
        self.rootfoldersfile=rootfolders
    
    def run(self):
        MediaFinder(self.rootfoldersfile,self.customstopwords,self.list_widget,self.trigger.emit)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        config=ConfigParser.RawConfigParser()
        config.read("config.cfg")
        self.rootfoldersfile=config.get("mainoptions","rootfolders").split(",")
        self.stoplistfile=config.get("mainoptions","stoplistfile")
        self.url=os.path.join(os.path.abspath("."),"web/html/index.html")
        
        MainWindow.setObjectName(_fromUtf8("Home Media Manager"))
        MainWindow.resize(640, 558)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 451, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setText(self.stoplistfile)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 281, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 431, 221))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.addItems(self.rootfoldersfile)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 120, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 150, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 350, 101, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 350, 121, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 390, 611, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 410, 501, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 50, 461, 41))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 430, 256*2, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Home Media Manager", "Home Media Manager", None))
        self.pushButton.setText(_translate("MainWindow", "Stopword file", None))
        self.label.setText(_translate("MainWindow", "Video folders (.mp4,.avi,.wmv will be indexed)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_4.setText(_translate("MainWindow", "Start Indexing", None))
        self.pushButton_5.setText(_translate("MainWindow", "Open Application", None))
        self.label_2.setText(_translate("MainWindow", "Note: The application will open in default browser. Google chrome and Opera are recommended browsers", None))
        self.label_3.setText(_translate("MainWindow", "You can copy and paste the url to the recommended browsers.", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is for automatic tag generation. Tags are generated using filenames. Enter the list of words (1 word per line) in a plain text file that you do not want to see as tags.</p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">URL:"+self.url+" </span></p></body></html>", None))


    
    def selectFile(self):
        # print "button clicked"
        self.lineEdit.setText(QFileDialog.getOpenFileName())
    
    def addFile(self):
        self.listWidget.addItems([QFileDialog.getExistingDirectory()])
    
    def removeFile(self):
        items = self.listWidget.selectedItems()
        self.listWidget.takeItem(self.listWidget.row(items[0]))
    
    def openApplication(self):
        os.system(self.url)
    
    def startIndexing(self):
        #first save config
        stoplistfile=str(self.lineEdit.text())
        rootfolderlist= self.getAllItems()
        outtext='''[mainoptions]
rootfolders={rootfolders}
stoplistfile={stoplistfile}
        '''.format(rootfolders=",".join(rootfolderlist),stoplistfile=stoplistfile)
        f=open("config.cfg","w")
        f.write(outtext)
        f.close()
        
        Form = QtGui.QMainWindow(MainWindow)
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        threadlist=[]
        self.u=Updater(Form,ui.plainTextEdit,0,stoplistfile,rootfolderlist)
        self.u.trigger.connect(self.ondataReady)
        threadlist.append(self.u)
        self.u.start()
    
    def ondataReady(self,listwidget,data):
        listwidget.appendPlainText(str(data)+"\n")
    
    def getAllItems(self):
        length=self.listWidget.count()
        items=[]
        for i in range(length):
            item=self.listWidget.item(i).text()
            items.append(str(item))
        self.getStopwordFile()
        return items
    
    def getStopwordFile(self):
        stopwordfile=self.lineEdit.text()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), ui.selectFile)
    app.connect(ui.pushButton_2, QtCore.SIGNAL("clicked()"), ui.addFile)
    app.connect(ui.pushButton_3, QtCore.SIGNAL("clicked()"), ui.removeFile)
    app.connect(ui.pushButton_5, QtCore.SIGNAL("clicked()"), ui.openApplication)
    app.connect(ui.pushButton_4, QtCore.SIGNAL("clicked()"), ui.startIndexing)
    MainWindow.show()
    sys.exit(app.exec_())
