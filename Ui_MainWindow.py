# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created: Mon Jun 30 12:02:45 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(616, 448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.labLogo = QtGui.QLabel(self.centralwidget)
        self.labLogo.setGeometry(QtCore.QRect(0, 10, 301, 71))
        self.labLogo.setStyleSheet(_fromUtf8("background-image: url(:/rc/xportscan_2.png);"))
        self.labLogo.setText(_fromUtf8(""))
        self.labLogo.setObjectName(_fromUtf8("labLogo"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(312, 10, 301, 421))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pteReturnInfo = QtGui.QPlainTextEdit(self.groupBox)
        self.pteReturnInfo.setGeometry(QtCore.QRect(10, 20, 281, 391))
        self.pteReturnInfo.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 172, 0);"))
        self.pteReturnInfo.setObjectName(_fromUtf8("pteReturnInfo"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 90, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 320, 301, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.letTargetIP = QtGui.QLineEdit(self.groupBox_2)
        self.letTargetIP.setGeometry(QtCore.QRect(76, 14, 131, 27))
        self.letTargetIP.setObjectName(_fromUtf8("letTargetIP"))
        self.btnTargetIPAdd = QtGui.QPushButton(self.groupBox_2)
        self.btnTargetIPAdd.setGeometry(QtCore.QRect(211, 14, 81, 27))
        self.btnTargetIPAdd.setObjectName(_fromUtf8("btnTargetIPAdd"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 48, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.letTargetPort = QtGui.QLineEdit(self.groupBox_2)
        self.letTargetPort.setGeometry(QtCore.QRect(90, 43, 71, 27))
        self.letTargetPort.setObjectName(_fromUtf8("letTargetPort"))
        self.btnTargetPortAdd = QtGui.QPushButton(self.groupBox_2)
        self.btnTargetPortAdd.setGeometry(QtCore.QRect(164, 43, 81, 27))
        self.btnTargetPortAdd.setObjectName(_fromUtf8("btnTargetPortAdd"))
        self.btnScan = QtGui.QPushButton(self.groupBox_2)
        self.btnScan.setGeometry(QtCore.QRect(10, 74, 98, 27))
        self.btnScan.setObjectName(_fromUtf8("btnScan"))
        self.btnClear = QtGui.QPushButton(self.groupBox_2)
        self.btnClear.setGeometry(QtCore.QRect(111, 74, 98, 27))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.lstIP = QtGui.QListWidget(self.centralwidget)
        self.lstIP.setGeometry(QtCore.QRect(10, 114, 141, 192))
        self.lstIP.setObjectName(_fromUtf8("lstIP"))
        self.lstPort = QtGui.QListWidget(self.centralwidget)
        self.lstPort.setGeometry(QtCore.QRect(170, 114, 121, 192))
        self.lstPort.setObjectName(_fromUtf8("lstPort"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XPortScan", None))
        self.groupBox.setTitle(_translate("MainWindow", "ReturnInfo", None))
        self.pteReturnInfo.setPlainText(_translate("MainWindow", "[+]XPortScan", None))
        self.label_2.setText(_translate("MainWindow", "Target IP List", None))
        self.label_3.setText(_translate("MainWindow", "Target Port List", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Controler", None))
        self.label.setText(_translate("MainWindow", "TargetIP:", None))
        self.btnTargetIPAdd.setText(_translate("MainWindow", "Add", None))
        self.label_4.setText(_translate("MainWindow", "TargetPort:", None))
        self.btnTargetPortAdd.setText(_translate("MainWindow", "Add", None))
        self.btnScan.setText(_translate("MainWindow", "Scan", None))
        self.btnClear.setText(_translate("MainWindow", "Clear", None))

import Ui_MainWindow_rc
