#!/usr/bin/python
from PyTango import DeviceProxy

class CurrentAttributeHelper(object):

    @staticmethod
    def get_devs_and_attributes(facades):
        """
        Get as a String list of real (non-facade) devices and
        values of their >>current<< attribute
        """
        returned_string = ""
        for facade in facades:
            real_dev_name = facade[4:]
            dev_proxy = DeviceProxy(real_dev_name)
            current_value = dev_proxy.current

            returned_string += real_dev_name + "\t - \t"
            returned_string += str(current_value) + "\n"

        return returned_string