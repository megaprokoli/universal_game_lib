from core.interface_handling.interface_loader import InterfaceLoader
import constants


class MultiLibInterface:
    def __init__(self):
        self.if_loader = InterfaceLoader(constants.APP_ROOT, "core.game_interfaces")
        self.game_interfaces = self.if_loader.load()

    def init_interfaces(self, silent=True):
        for interf in self.game_interfaces.values():
            interf.initialize()

            if not silent:
                print("{} | state: {} - message: {}".format(interf.name, interf.init_ok["state"], interf.init_ok["msg"]))