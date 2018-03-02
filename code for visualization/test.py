# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:18:19 2017

@author: Air
"""

"""
ZetCode PySide tutorial 

In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel,QGridLayout, QTableWidget, QTextEdit, QLineEdit, QPushButton, QGroupBox, QSizePolicy



class Example(QtWidgets.QWidget):
	def createButton(self, text, member):
		button = QPushButton(text)
		button.clicked.connect(member)
		return button

	def __init__(self):
		super(Example, self).__init__()

		self.initUI()

	def initUI(self):
		title = self.createButton('Title', self.close)
		author = QLabel('Author')
		review = QLabel('Review')
		imgBox = QGroupBox("Image")
		imageLabel = QLabel()
		imageLabel.setAlignment(Qt.AlignCenter)
		imageLabel.setSizePolicy(QSizePolicy.Expanding,
		                         QSizePolicy.Expanding)

		imgBox.setSizePolicy(QSizePolicy.Expanding,
		                            QSizePolicy.Expanding)
		Imageslabels = QGridLayout()
		Imageslabels.addWidget(imageLabel)
		imgBox.setLayout(Imageslabels)


		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(title, 1, 0)
		grid.addWidget(titleEdit, 1, 1)

		grid.addWidget(author, 2, 0)
		grid.addWidget(authorEdit, 2, 1)

		grid.addWidget(review, 3, 0)
		grid.addWidget(reviewEdit, 3, 1, 5, 1)
		grid.addWidget(imgBox, 4, 1)
		self.setLayout(grid)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Review')
		self.show()

	def show_img(self):
		img


def main():
	DS_APP = QApplication(sys.argv)
	DS_Widget = Example()
	DS_Widget.show()
	sys.exit(DS_APP.exec_())


if __name__ == '__main__':
	main()