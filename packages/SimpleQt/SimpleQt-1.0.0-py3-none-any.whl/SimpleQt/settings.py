#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import os

from lxml import etree
from pyproptree import Node, io

class Settings(Node):
	def __init__(self, path=None):
		Node.__init__(self, "settings")
		self.path = path
	
	def load(self):
		if self.path != None:
			if not os.path.exists(self.path):
				os.makedirs(os.path.join(*os.path.split(self.path)[:-1]), exist_ok=True)
				self.save()
				return
			try:
				self = io.loadFile(self.path, self)
			except etree.XMLSyntaxError as e:
				if "document is empty" in str(e).lower():
					self.save()
				else:
					raise
	
	def save(self):
		if self.path != None:
			io.writeFile(self, self.path)

settings = Settings()

