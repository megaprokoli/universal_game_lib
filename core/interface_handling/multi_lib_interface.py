from core.interface_handling.interface_loader import InterfaceLoader
import constants


class MultiLibInterface:
    def __init__(self):
        self.if_loader = InterfaceLoader(constants.CONFIG_PATH, "core.game_interfaces")
        self.game_interfaces = self.if_loader.load()

    def init_interfaces(self, silent=True):
        for interf in self.game_interfaces.values():
            interf.initialize()

            if not silent:
                print("{} | state: {} - message: {}".format(interf.name, interf.init_ok["state"], interf.init_ok["msg"]))

    def find_by_game(self, game_name):
        for interf in self.game_interfaces.values():
            if interf.init_ok["state"]:
                if game_name in interf.get_game_names():
                    return interf
        return None

    def get_all_gamenames(self):
        names = list()

        for interf in self.game_interfaces.values():
            if interf.init_ok["state"]:
                names.append(interf.get_game_names())
        return names
