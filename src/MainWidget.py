#!/usr/bin/python
from PyQt4.QtGui import QMainWindow, QWidget, QPushButton, QVBoxLayout, QPlainTextEdit
from PyQt4 import QtCore
from FacadeDsController import FacadeDeviceServerController
from CurrentAttributeHelper import CurrentAttributeHelper

class mainWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.create_layout()
        self.update_buttons_state()
        self.connect_slots()

    def create_layout(self):
        self.facadeserver_button = QPushButton(self)
        self.elindevices_button = QPushButton(self)
        self.devlist_edit = QPlainTextEdit(self)
        self.elindevices_button.setText("Get list of devices and 'current' attribute values")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.facadeserver_button, 0)
        self.layout.addWidget(self.elindevices_button, 1)
        self.layout.addWidget(self.devlist_edit, 2)

    def update_buttons_state(self):
        self.facadeController = FacadeDeviceServerController()
        if self.facadeController.server_exists():
            self.facadeserver_button.setText("Update Facadedevice Server")
            self.elindevices_button.setEnabled(True)
        else:
            self.facadeserver_button.setText("Create Facadedevice Server")
            self.elindevices_button.setEnabled(False)

    def connect_slots(self):
        self.connect(self.facadeserver_button, QtCore.SIGNAL("clicked()"), self.create_server)
        self.connect(self.elindevices_button, QtCore.SIGNAL("clicked()"), self.get_devs_and_attr_list)

    def create_server(self):
        print("Creating/Updating Facadedevice server...")
        self.facadeController.create_server()
        self.update_buttons_state()
        print("...done")

    def get_devs_and_attr_list(self):
        facades = self.facadeController.get_facadedevice_names()
        devs_and_attrs = CurrentAttributeHelper.get_devs_and_attributes(facades)

        self.devlist_edit.clear()
        self.devlist_edit.setPlainText(devs_and_attrs)


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("Facadedevice server GUI")
        self.setFixedSize(600, 400)

        mWidget = mainWidget(self)
        self.setCentralWidget(mWidget)