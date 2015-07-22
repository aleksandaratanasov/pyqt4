#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:44:35 2015

@author: Aleksandar Vladimirov Atanasov
"""

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QSizePolicy
from grid_generator import get_dim

"""
ZetCode PyQt4 tutorial 

In this example, we create a skeleton
of a calculator using a QtGui.QGridLayout.

author: Jan Bodnar
website: zetcode.com 
last edited: July 2014
"""

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        grid = QtGui.QGridLayout()
        grid.setMargin(20)
        grid.setContentsMargins(5,5,5,5)
        self.setLayout(grid)

        # This is just a sample
        # The list can be filled with data for example from a YAML file or similar 
        names = []
        num_of_items = 13
        for i in range(0, num_of_items):
            names.append(str(i))
                 
        (rows, cols) = get_dim(len(names))
        print 'grid (rows x cols): ' + str(rows) + 'x' + str(cols)
        
        positions = []
        for r in range(0, rows):
            for c in range(0, cols):
                positions.append([r, c])
                             
                 
        nameIdx = 0
        for (name, position) in zip(names, positions):
            if nameIdx < len(names):
                button = QtGui.QPushButton(name)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                grid.addWidget(button, position[0], position[1])
            else:
                pass
            nameIdx = nameIdx + 1
            
        self.move(300, 400)
        self.setWindowTitle('Square grid of buttons')
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
