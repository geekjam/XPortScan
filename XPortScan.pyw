#!/usr/bin/env python
#encoding:utf-8
import sys
from PyQt4 import QtCore,QtGui
from Ui_MainWindow import Ui_MainWindow
import ComNet
import rscan
import threading

class MainWindow(QtGui.QMainWindow):
    ReturnMsg = []
    def CenterOnScreen (self):
        '''centerOnScreen() Centers the window on the screen.'''
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def TargetPortAdd(self, port):
        rscan.addport(port)

    def TargetIPAdd(self, ip):
        rscan.addip(ip)
        

    def BtnTargetIPAddClicked(self):
        ip = str(self.ui.letTargetIP.text())
        self.TargetIPAdd(ip)
        self.ui.lstIP.addItem(QtGui.QListWidgetItem(ip))


    def BtnTargetPortAddClicked(self):
        port = int(self.ui.letTargetPort.text())
        self.TargetPortAdd(port)
        self.ui.lstPort.addItem(QtGui.QListWidgetItem(str(port)))

    def CallBackEcho(self, echoStr):
        self.ReturnMsg.append(echoStr)
 	
    def ThreadScan(self):
        rscan.scan()

    def BtnScanClicked(self):
        self.ui.btnScan.setEnabled(False)
        rscan.CallBackEcho = self.CallBackEcho
        t = threading.Thread(target=self.ThreadScan,)
	t.setDaemon(True)
    	t.start()

    

    def GuiSync(self):
        if self.ReturnMsg != []:
            msg = self.ReturnMsg.pop(0)
            if msg == "end":
                self.ui.btnScan.setEnabled(True)
            self.ui.pteReturnInfo.appendPlainText(msg) 

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.GuiSyncTimer = QtCore.QTimer(self)
        self.GuiSyncTimer.timeout.connect(self.GuiSync)
        self.GuiSyncTimer.start(500)
        self.ui.letTargetIP.setText(ComNet.GetLocalIpAddr())
        self.ui.btnTargetPortAdd.clicked.connect(self.BtnTargetPortAddClicked)
        self.ui.btnTargetIPAdd.clicked.connect(self.BtnTargetIPAddClicked)
        self.ui.btnScan.clicked.connect(self.BtnScanClicked)
        self.CenterOnScreen()


app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
