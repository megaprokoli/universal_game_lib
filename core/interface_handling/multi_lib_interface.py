from core.interface_handling.interface_loader import InterfaceLoader
import constants
import re


class MultiLibInterface:
    def __init__(self, init_fail):
        self.init_fail_callback = init_fail
        self.if_loader = InterfaceLoader(constants.CONFIG_PATH, "core.game_interfaces")
        self.game_interfaces = self.if_loader.load()

    def init_interfaces(self, silent=True):
        for interf in self.game_interfaces.values():
            interf.initialize()

            if not silent:
                print("{} | state: {} - message: {}"
                      .format(interf.name, interf.init_ok["state"], interf.init_ok["msg"]))

            if not interf.init_ok["state"]:
                self.init_fail_callback("Initialization of {} failed. Detail: {}"
                                        .format(interf.name, interf.init_ok["msg"]))

    def find_by_game(self, game_name):
        for interf in self.game_interfaces.values():
            if interf.init_ok["state"]:
                names = interf.get_game_names()

                if names is None:
                    continue

                if game_name in names:
                    return interf
        return None

    def get_gamenames(self):
        names = list()

        for interf in self.game_interfaces.values():
            if interf.init_ok["state"]:
                games = interf.get_game_names()

                if games is None:
                    continue
                names.extend(games)
        return names

    def search(self, search_str):
        suggestions = []
        suggestions_lower = []
        gnames = self.get_gamenames()
        search_pattern = self._gen_search_pattern(search_str.lower())   # lower to simplify search

        for pattern in search_pattern:
            for name in gnames:
                match = pattern.search(name.lower())    # lower to simplify search

                if match is None:
                    continue

                if match.string in suggestions_lower:     # TODO maybe (common suggest size = 5 - 10) more efficient way
                    continue

                suggestions_lower.append(match.string)
                suggestions.append(name)
        return suggestions

    def _gen_search_pattern(self, search_str):   # TODO optimize search pattern
        return [re.compile(r"^{}$".format(search_str)),     # just the word
                re.compile(r"^{}.*".format(search_str)),    # the word and stuff after it
                re.compile(r".*{}$".format(search_str)),    # the word and stuff before it
                re.compile(search_str)]                     # the word anywhere
