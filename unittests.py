#!/usr/bin/python
import unittest
import PyTango
from src.FacadeDsController import FacadeDeviceServerController

class FacadeControllerTest(unittest.TestCase):

    def setUp(self):
        self.facadeCtrl = FacadeDeviceServerController()
        self.db = PyTango.Database()

        # clear FacadeDevices
        dev_names = self.db.get_device_class_list("FacadeDevice/elin")
        for dev in dev_names:
            if "/" in dev:
                self.db.delete_device(dev)


    def testServerExists(self):
        self.assertEqual(self.facadeCtrl.server_exists(), False)

        devs = ["1", "2", "77", "44"]
        for dev in devs:
            dev_info = PyTango.DbDevInfo()
            dev_info.server = "FacadeDevice/elin"
            dev_info._class = "FacadeDevice"
            dev_info.name = "fcd_something/to/test" + dev
            self.db.add_device(dev_info)

        self.assertEqual(self.facadeCtrl.server_exists(), True)

        for dev in self.db.get_device_class_list("FacadeDevice/elin"):
            if "/" in dev:
                self.db.delete_device(dev)

        self.assertEqual(self.facadeCtrl.server_exists(), False)

    def testFacadeNames(self):
        names = ["elin/sth/test1", "elin/sth/test2", "a/b/c"]
        facades = self.facadeCtrl.create_facade_names(names)
        self.assertEqual(len(names), len(facades))
        self.assertEqual("fcd_" + names[0], facades[0])
        self.assertEqual("fcd_" + names[1], facades[1])
        self.assertEqual("fcd_" + names[2], facades[2])

    def testAddFacadeToServer(self):
        self.assertEqual(self.facadeCtrl.server_exists(), False)
        self.facadeCtrl.add_facade_devices_to_server(["fcd_a/b/c"])
        self.assertEqual(self.facadeCtrl.server_exists(), True)
        self.assertTrue("fcd_a/b/c" in self.db.get_device_class_list("FacadeDevice/elin"))

        retrievedNames = self.facadeCtrl.get_facadedevice_names()
        self.assertEqual(["fcd_a/b/c"], retrievedNames)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()