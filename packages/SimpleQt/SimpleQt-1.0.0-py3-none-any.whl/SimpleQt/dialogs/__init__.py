#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import *

class Dialog(QDialog):
	def __init__(self, *args, buttons=QDialogButtonBox.Ok, title="Dialog", **kwargs):
		QDialog.__init__(self, *args, **kwargs)
		
		self.setWindowTitle(title)
		self.buttons = buttons
		
		self.lay = QVBoxLayout()
		self.setLayout(self.lay)
		
		self.main = QVBoxLayout()
		self.lay.addLayout(self.main)
		
		self.addButtonBox()
	
	def addWidget(self, widget):
		self.main.addWidget(widget)
	
	def addLayout(self, layout):
		self.main.addLayout(layout)
	
	def addButtonBox(self):
		self.buttonBox = QDialogButtonBox(self.buttons)
		self.buttonBox.clicked.connect(self.clicked)
		self.lay.addWidget(self.buttonBox)
	
	def clicked(self, button):
		self.destroy()

