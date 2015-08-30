#!/usr/bin/python
__author__ = 'Maciej Michalec'
from facadedevice import common, device, objects
from PyTango import AttrWriteType

"""
FacadeDevice is a server for facades of devices
It uses lib-maxiv-facadedevice library and provides
proxy attribute >>current<< to use in the future
It hosts devices which names are corresponding with
names of real devices having adequate attribute
"""
class FacadeDevice(device.Facade):
    __metaclass__ = device.FacadeMeta

    # This attribute will be used to store current values of
    # TANGO devices. Currently it is only an element which indicates
    # that real-device (not facade) contains such attribute
    current = objects.proxy_attribute(device="FacadeDevice",
                                      attr="Current",
                                      dtype=float,
                                      access=AttrWriteType.READ_WRITE,
                                      format="%6.2f")
    run = common.run_server

if __name__ == "__main__":
    FacadeDevice.run()
