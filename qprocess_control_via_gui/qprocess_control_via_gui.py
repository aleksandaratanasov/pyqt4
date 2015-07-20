#!/usr/bin/python

# Title: QProcess Control via GUI
# Author: Aleksandar Vladimirov Atanasov
# Description: Launches and terminates a detached process using a toggable push button

import sys, subprocess, os
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt4.QtCore import QProcess

class QProcessControl(QWidget):

    
    def __init__(self):
        super(QProcessControl, self).__init__()
	self.command = './testCommand.py'
	self.status = False
	self.pid = 0
	self.pidFilePath = 'qpc.pid'

        if os.path.isfile(self.pidFilePath):
		print 'Found \"qpc.pid\". Restoring connection to detached process'
		with open(self.pidFilePath) as f:
			self.pid = int(f.readline())	# TODO: this has to be long but damn it's so hard to parse long values in Python O_O
			print 'PID: ', self.pid
			self.status = True
	else:
		print 'Warning: No \"qpc.pid\" detected. If you have started the detached process, closed the UI and deleted this file, the application will be unable to restore its state and the external process will be orphaned!'

	self.args = ['']
        self.initUI()
        
    def initUI(self):
        
	self.hbox = QHBoxLayout()

	self.qbtn = QPushButton('Start', self)
	self.qbtn.setCheckable(True)
	if self.status:
		self.qbtn.setChecked(True)
		self.qbtn.setText('Stop')
	self.qbtn.clicked.connect(self.toggleProcess)
	self.qbtn.resize(self.qbtn.sizeHint())
	self.hbox.addWidget(self.qbtn)

	self.setLayout(self.hbox)
	self.setGeometry(300, 300, 250, 150)
	self.setWindowTitle('QProcess controlled by a button')    
	self.show()

    def toggleProcess(self, val):
	if val:
		print 'Starting process'
		self.status, self.pid = QProcess.startDetached(self.command, self.args, '.')
		if self.status:
			print 'PID: ', self.pid
			pidFile = open(self.pidFilePath, 'w')
			pidFile.write(str(self.pid))
			pidFile.close()
			self.qbtn.setText('Stop')			
		else:
			self.qbtn.setChecked(False)
			print 'Error: Failed to create process!'
	else:
		print 'Stopping process'
		if self.status:
			# kill takes a very short amount of time hence we can call it from inside the main thread without freezing the UI
			success = subprocess.call(['kill', '-SIGTERM', str(self.pid)])
			if success == 0:
				print 'Process stopped!'
				self.status = False
				self.pid = 0
				os.remove(self.pidFilePath)
				self.qbtn.setText('Start')
			else:
				print 'Error: Failed to stop process!'
				self.qbtn.setChecked(True)

def main(): 
    app = QApplication(sys.argv)
    ex = QProcessControl()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
