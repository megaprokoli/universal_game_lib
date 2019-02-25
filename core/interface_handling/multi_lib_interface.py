from core.interface_handling.interface_loader import InterfaceLoader
import constants


class MultiLibInterface:
    def __init__(self):
        self.if_loader = InterfaceLoader("{}/core/game_interfaces".format(constants.APP_ROOT), "core.game_interfaces")
        self.game_interfaces = self.if_loader.load()

