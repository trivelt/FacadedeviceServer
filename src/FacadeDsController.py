#!/usr/bin/python
import PyTango
#from FacadeDevice import FacadeDevice

class FacadeDeviceServerController(object):
    def __init__(self):
        self.db = PyTango.Database()

    def server_exists(self):
        """
        Check if FacadeDevice exists
        """
        if "FacadeDevice" in self.db.get_server_name_list():
            return True
        else:
            return False

    def create_server(self):
        """
        Create FacadeDevice server to store facades
        of elin/ devices with >>current<< attributes
        """
        devs = self.find_elin_devices()
        devs = self.filter_by_current_attribute(devs)
        facades = self.create_facade_names(devs)
        self.add_facade_devices_to_server(facades)
        # FacadeDevice.run(("elin")

    def find_elin_devices(self):
        elin_devices = list()
        dev_names = list()
        servers = self.db.get_server_list()
        for server in servers:
            dev_names.append(self.db.get_device_class_list(server))

        for device_group in dev_names:
            for name in device_group:
                if name.startswith("elin/"):
                    elin_devices.append(name)
        return elin_devices

    def filter_by_current_attribute(self, devices):
        devs_with_current = list()
        for device in devices:
            proxy_device = PyTango.DeviceProxy(device)
            try:
                if "Current" in proxy_device.get_attribute_list():
                    devs_with_current.append(device)
            except:
                continue
        return devs_with_current

    def create_facade_names(self, devices):
        facades = ["fcd_" + name for name in devices]
        return facades


    def add_facade_devices_to_server(self, facades):
        for facade in facades:
            dev_info = PyTango.DbDevInfo()
            dev_info.server = "FacadeDevice/elin"
            dev_info._class = "FacadeDevice"
            dev_info.name = facade

            self.db.add_device(dev_info)

    def get_facadedevice_names(self):
        """
        Get names of devices from FacadeDevice server
        """
        facades = list()
        dev_names = self.db.get_device_class_list("FacadeDevice/elin")
        for name in dev_names:
            if name.startswith("fcd_"):
                facades.append(name)
        return facades