from CurrentAttributeHelper import CurrentAttributeHelper
from FacadeDsController import FacadeDeviceServerController

class Options():
    CREATE_SERVER = 0
    GET_LIST = 1
    QUIT = 2
    OTHER = 3

class CommandLineInterface(object):
    def __init__(self):
        self.facadeController = FacadeDeviceServerController()

    def start(self):
        selected_option = None
        while selected_option is not Options.QUIT:
            selected_option = self.show_menu()
            if selected_option is Options.CREATE_SERVER:
                self.create_server()
            elif selected_option is Options.GET_LIST:
                self.get_list()

    def show_menu(self):
        if self.facadeController.server_exists():
            options = "Select option:\n[U]pdate Facedevice Server, [G]et devs and attrs list, [Q]uit: "
            allowed_choices = ("U", "G", "Q")
        else:
            options = "Select option:\n[C]reate Facadedevice Server, [Q]uit: "
            allowed_choices = ("C", "Q")

        choice = raw_input(options)
        if choice not in allowed_choices:
            return Options.OTHER
        elif choice == "U" or choice == "C":
            return Options.CREATE_SERVER
        elif choice == "G":
            return Options.GET_LIST
        elif choice == "Q":
            return Options.QUIT

    def create_server(self):
        self.facadeController.create_server()

    def get_list(self):
        facades = self.facadeController.get_facadedevice_names()
        devs_and_attrs = CurrentAttributeHelper.get_devs_and_attributes(facades)
        print(devs_and_attrs)

