# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:43:09 2017

@author: Air
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        #设置按钮和输入
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()
        
        redb = QtGui.QPushButton('Red', self)
        redb.setCheckable(True)
        redb.clicked[bool].connect(self.addpicture)


        #####
        self.comboLabel = QtGui.QLabel(self)  
        png=QtGui.QPixmap('Users/linhangyu19960303/Desktop/trans_zxh151.png')
        self.comboLabel.setPixmap(png)  
        self.comboLabel.setScaledContents(True)
        #####


        #self.comboLabel.setGeometry(10, 10, 40, 50)
        #设置位置
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.comboLabel, 1, 1)
        
        grid.addWidget(redb,2,0)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        self.setGeometry(300, 300, 400, 350)
        self.setWindowTitle('Review')    
        self.show()
        #####
    def addpicture(self): 
        
        png=QtGui.QPixmap('Users/linhangyu19960303/Desktop/trans_zxh151.png')
        self.comboLabel.setPixmap(png)  
    
        
        #self.show()
        ####


        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()