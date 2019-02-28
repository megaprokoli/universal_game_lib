from abc import ABC, abstractmethod
import json
import constants


class RepoInterface(ABC):
    def __init__(self, name):
        self.name = name
        self.init_ok = {"state": False, "msg": "not initialized"}
        self.games_dict = dict()
        self.config = dict()

    @abstractmethod
    def _load_games(self):
        pass

    @abstractmethod
    def start_game(self, game):
        pass

    def _load_config(self):
        conf_path = "{}/{}_config.json".format(constants.INTERFACE_CONFIG, self.name)

        with open(conf_path, "r") as config:
            json_obj = json.load(config, encoding="UTF-8")
            self.config = json_obj

    def initialize(self):
        try:
            self._load_config()
            self._load_games()
        except KeyError:
            self.init_ok["state"] = False
            self.init_ok["msg"] = "corrupted interface config"
        except FileNotFoundError:
            self.init_ok["state"] = False
            self.init_ok["msg"] = "no config file found"
        except Exception as err:
            self.init_ok["state"] = False
            self.init_ok["msg"] = "unknown error! detail: " + str(err)
        else:
            self.init_ok["state"] = True
            self.init_ok["msg"] = "ok"

    def get_game_names(self):
        return list(self.games_dict.keys())

    def get_gameid_by_name(self, name):
        if name in self.games_dict:
            return self.games_dict[name].appid
        else:
            return None
