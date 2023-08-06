#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from plum import dispatch

from SimpleQt.box import HBox, VBox
from SimpleQt.settings import settings
from SimpleQt.dialogs import Dialog
from SimpleQt.buttons import FontChooserButton

class Setting(HBox):
	changed = pyqtSignal(HBox)
	reset = pyqtSignal(HBox)
	
	def __init__(self, text, path, default):
		HBox.__init__(self)
		
		self.default = default
		self.path = path
		self.unsaved = False
		
		self.label = QLabel(text)
		self.addWidget(self.label)
		
		self.changed.connect(self.onChanged)
	
	@pyqtSlot(HBox)
	def onChanged(self, setting):
		settingsValue = settings.getValue(self.path)
		
		if self.value() != settings.getValue(self.path):
			self.unsaved = True
		else:
			self.unsaved = False
	
	def update(self):
		self.resetToSaved()
	
	def value(self):
		return self.widget.value()
	
	def setValue(self, value):
		self.widget.setValue(value)
	
	@pyqtSlot(HBox)
	def resetToSaved(self):
		self.setValue(settings.getValue(self.path, self.default))
		self.reset.emit(self)
	
	def save(self):
		settings.setValue(self.value(), self.path)

class IntegerSetting(Setting):
	def __init__(self, text, path, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QLineEdit()
		self.widget.setValidator(QIntValidator())
		value = settings.getIntValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
	
		self.widget.textChanged.connect(lambda text: self.changed.emit(self))
	
	def value(self):
		return int(self.widget.text())
	
	def setValue(self, value):
		self.widget.setText(str(value))

class DoubleSetting(Setting):
	def __init__(self, text, path, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QLineEdit()
		self.widget.setValidator(QDoubleValidator())
		value = settings.getFloatValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
	
		self.widget.textChanged.connect(lambda text: self.changed.emit(self))
	
	def value(self):
		return float(self.widget.text())
	
	def setValue(self, value):
		self.widget.setText(str(value))

class StringSetting(Setting):
	def __init__(self, text, path, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QLineEdit()
		value = settings.getStringValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
		
		self.widget.textChanged.connect(lambda text: self.changed.emit(self))
	
	def value(self):
		return str(self.widget.text())
	
	def setValue(self, value):
		self.widget.setText(str(value))

class BoolSetting(Setting):
	def __init__(self, text, path, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QCheckBox()
		value = settings.getBoolValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
		
		self.widget.toggled.connect(lambda checked: self.changed.emit(self))
	
	def value(self):
		return self.widget.isChecked()
	
	def setValue(self, value):
		self.widget.setChecked(bool(value))

class IntegerRangeSetting(Setting):
	def __init__(self, text, path, min, max, step, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QSpinBox()
		self.widget.setRange(min, max)
		self.widget.setSingleStep(step)
		value = settings.getIntValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
	
		self.widget.valueChanged.connect(lambda value: self.changed.emit(self))
	
	def value(self):
		return int(self.widget.value())
	
	def setValue(self, value):
		self.widget.setValue(int(value))

class DoubleRangeSetting(Setting):
	def __init__(self, text, path, min, max, step, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QDoubleSpinBox()
		self.widget.setRange(min, max)
		self.widget.setSingleStep(step)
		value = settings.getFloatValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
	
		self.widget.valueChanged.connect(lambda value: self.changed.emit(self))
	
	def value(self):
		return float(self.widget.value())
	
	def setValue(self, value):
		self.widget.setValue(float(value))

class ChoicesSetting(Setting):
	def __init__(self, text, path, choices, default):
		Setting.__init__(self, text, path, default)
		
		self.widget = QComboBox()
		self.widget.addItems(choices)
		self.widget.setEditable(False)
		value = settings.getStringValue(path, default)
		self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
	
		self.widget.currentTextChanged.connect(lambda text: self.changed.emit(self))
	
	def value(self):
		return self.widget.currentText()
	
	def setValue(self, value):
		self.widget.addItem(value)
		self.widget.setCurrentText(value)

class ListSetting(Setting):
	def __init__(self, text, path, items, selectionMode, itemFlags, default=None):
		Setting.__init__(self, text, path, default)
		
		self.widget = QListWidget()
		self.widget.setSelectionMode(selectionMode)
		self.addItems(items)
		value = settings.getStringValue(path, default)
		if value != None:
			self.setValue(value)
		settings.getNode(path, True).addListener(lambda n: self.setValue(n.getValue()))
		self.addWidget(self.widget)
		
		self.widget.currentRowChanged.connect(lambda text: self.changed.emit(self))
	
	def addItems(self, items):
		for item in items:
			self.addItem(item)
	
	def addItem(self, item, flags=None):
		if item == None:
			return
		
		if not isinstance(item, QListWidgetItem):
			item = QListWidgetItem(item)
		
		if flags:
			item.setFlags(flags)
		self.widget.addItem(item)
	
	def value(self):
		return self.widget.currentItem().text()
	
	def setValue(self, value):
		if not isinstance(value, str):
			raise ValueError(f"cannot set setting to a non-string value (got {type(value)}({value}))")
		
		found = self.widget.findItems(value, Qt.MatchFixedString | Qt.MatchCaseSensitive)
		if not len(found):
			self.widget.addItem(value)
			self.widget.setCurrentRow(self.widget.count() - 1)
			self.widget.item(self.widget.count() - 1)
		else:
			self.widget.setCurrentRow(self.widget.row(found[0]))
			self.widget.item(self.widget.row(found[0])).setSelected(True)

class FontSetting(Setting):
	def __init__(self, text, path, default):
		Setting.__init__(self, text, path, default)
		
		self._font = QFont()
		self.setValue(default)
		
		self.node = settings.initNode(path)
		self.sizeNode = self.node.initNode("size", int, self.fontSize)
		self.familyNode = self.node.initNode("family", str, self.fontFamily)
		self.node.addListener(lambda n, subn: self.setValue(n.getStringValue("family"), n.getIntValue("size")))
		
		self.widget = FontChooserButton(default=default)
		self.widget.fontChanged.connect(self.setValue)
		
		self.addWidget(self.widget)
	
	def value(self):
		return self._font
	
	@dispatch
	def setValue(self, font: QFont):
		if font.family() != self._font.family():
			self._font = font
			self.fontFamily = font.family()
			self.fontSize = max(font.pointSize(), font.pixelSize())
			self.changed.emit(self)
	
	@dispatch
	def setValue(self, family: str, size: int):
		if family != self._font.family():
			self._font = QFont(family, size)
			self.fontFamily = family
			self.fontSize = size
			self.changed.emit(self)
	
	def resetToSaved(self):
		self.setValue(QFont(self.familyNode.getStringValue(), self.sizeNode.getIntValue()))
		self.widget.fontChanged.emit(self._font)
		self.reset.emit(self)
	
	def save(self):
		self.familyNode.setValue(self.fontFamily)
		self.sizeNode.setValue(self.fontSize)

class SettingsDialogPage(VBox):
	def __init__(self, ident, label, *args, **kwargs):
		VBox.__init__(self, *args, **kwargs)
		
		self.ident = ident
		self.label = label

class SettingsDialogPageList(list):
	def __contains__(self, ident_or_page):
		if isinstance(ident_or_page, str):
			return any(page.ident == ident_or_page for page in self)
		else:
			return list.__contains__(self, ident_or_page)
	
	def index(self, ident_or_page):
		if isinstance(ident_or_page, str):
			for i, page in enumerate(self):
				if page.ident == ident_or_page:
					return i
			else:
				raise ValueError(f"no page with identifier {ident_or_page.ident}")
		else:
			if ident_or_page in self:
				return list.index(self, ident_or_page)
			else:
				raise ValueError(f"no page with identifier {ident_or_page.ident}")

class SettingsDialog(Dialog):
	def __init__(self, *args, **kwargs):
		Dialog.__init__(self, *args, buttons=(QDialogButtonBox.Apply | QDialogButtonBox.Ok |
											QDialogButtonBox.Reset | QDialogButtonBox.Cancel),
						title="Preferences", **kwargs)
		
		self.unsavedSettings = False
		self.buttonBox.button(QDialogButtonBox.Reset).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Cancel).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Apply).setDisabled(True)
		
		self.items = []
		self.pages = SettingsDialogPageList()
		
		self.tabWidget = QTabWidget()
		self.addWidget(self.tabWidget)
	
	def show(self):
		for item in self.items:
			item.update()
		Dialog.show(self)
	
	# Add a page to the settings dialog, to group settings
	# @param str ident Identifier of the page - must be unique within an instance of SettingsDialog
	# @param str label Displayed name of the page
	def addPage(self, ident: str, label: str):
		if ident in self.pages:
			raise ValueError(f"this SettingsDialog already contains a page with identifier {ident}")
		
		page = SettingsDialogPage(ident, label)
		self.pages.append(page)
		self.tabWidget.addTab(page, label)
		return page
	
	def page(self, ident: str):
		if ident in self.pages:
			return self.pages[self.pages.index(ident)]
	
	def onSettingChanged(self, setting):
		if setting.unsaved:
			self.unsavedSettings = True
		else:
			self.unsavedSettings = all(setting.unsaved for setting in self.items)
		self.buttonBox.button(QDialogButtonBox.Reset).setDisabled(not self.unsavedSettings)
		self.buttonBox.button(QDialogButtonBox.Cancel).setDisabled(not self.unsavedSettings)
		self.buttonBox.button(QDialogButtonBox.Apply).setDisabled(not self.unsavedSettings)
	
	def addSetting(self, page, text, path, typ, default=None, **kwargs):
		setting = None
		if typ == int:
			if default == None:
				default = 0
			setting = IntegerSetting(text, path, default)
		elif typ == float:
			if default == None:
				default = 0.0
			setting = DoubleSetting(text, path, default)
		elif typ == str:
			if default == None:
				default = ""
			setting = StringSetting(text, path, default)
		elif typ == bool:
			if default == None:
				default = False
			setting = BoolSetting(text, path, default)
		elif typ == range:
			if "max" not in kwargs:
				raise TypeError("'max' keyword argument is mandatory when adding a setting with type range")
			
			min = kwargs.get("min", 0)
			max = kwargs["max"]
			step = kwargs.get("step", 1)
			
			if default == None:
				default = 0
			if type(min) == int and type(step) == int:
				setting = IntegerRangeSetting(text, path, min, int(max), step, default)
			else:
				setting = DoubleRangeSetting(text, path, float(min), float(max), float(step), float(default))
		elif typ == tuple:
			if "choices" not in kwargs:
				raise TypeError("'choices' keyword argument is mandatory when adding a setting with type tuple")
			
			if default == None:
				default = ""
			setting = ChoicesSetting(text, path, kwargs["choices"], default)
		elif typ == list:
			if "items" not in kwargs:
				raise TypeError("'items' keyword argument is mandatory when adding a setting with type list")
			items = kwargs["items"]
			selectionMode = kwargs.get("selectionMode", QListWidget.SingleSelection)
			itemFlags = kwargs.get("itemFlags", Qt.ItemIsEditable)
			
			if len(items) == 0:
				items[0] = None
			default = kwargs.get("default", items[0])
			setting = ListSetting(text, path, items, selectionMode, itemFlags, default)
		elif typ == QFont:
			if default == None:
				default = QFont()
			setting = FontSetting(text, path, default)
		else:
			raise NotImplementedError(f"setting type {typ} is not implemented")
		
		setting.changed.connect(self.onSettingChanged)
		self.items.append(setting)
		
		page = self.page(page)
		if not page:
			page = self.addPage(page)
		page.addWidget(setting)
		
		return setting
	
	def saveSettings(self):
		for setting in self.items:
			setting.save()
		self.unsavedSettings = False
		self.buttonBox.button(QDialogButtonBox.Reset).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Cancel).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Apply).setDisabled(True)
	
	def resetSettingsToSaved(self):
		for setting in self.items:
			setting.resetToSaved()
		self.unsavedSettings = False
		self.buttonBox.button(QDialogButtonBox.Reset).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Cancel).setDisabled(True)
		self.buttonBox.button(QDialogButtonBox.Apply).setDisabled(True)
		
	def clicked(self, button):
		button = self.buttonBox.standardButton(button)
		if button in (QDialogButtonBox.Cancel, QDialogButtonBox.Reset):
			self.resetSettingsToSaved()
		elif button in (QDialogButtonBox.Apply, QDialogButtonBox.Ok):
			self.saveSettings()
		
		if button in (QDialogButtonBox.Ok, QDialogButtonBox.Cancel):
			self.destroy()

