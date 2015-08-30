Facadedevice server
==============

Simple program allowing to display values of attribute "current" from "elin" TANGO devices. 
It creates Facededevice server to store names of found devices. After that, user is able to 
get list of "elin" devices with "current" attribute values. 

### Usage 
The application has two modes:

  - Graphical User Interface, based on PyQt4 framework. To start, type: ./run.py
  - Command-line Interface. To start, type: ./run --cli or ./run -c

### TANGO Device Server
This part of program is under construction, so Facadedevice server is used only to 
collect list of devices. There are plans to create Facadedevices with appropriate
proxy attributes. 
