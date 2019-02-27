import os
import json

from steamfiles import acf

from core.game_interfaces.game import Game
from core.game_interfaces.repo_interface import RepoInterface

import constants


class SteamInterface(RepoInterface):
    def __init__(self, name):
        super().__init__(name)

        self.steam_path = None

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

    def _load_config(self):
        conf_path = "{}/{}_config.json".format(constants.INTERFACE_CONFIG, self.name)

        with open(conf_path, "r") as config:
            json_obj = json.load(config, encoding="UTF-8")
            self.steam_path = json_obj["path"]

    def _load_games(self):
        acf_path = "{}/steamapps".format(self.steam_path)
        files = os.listdir(acf_path)

        acf_files = list(filter(lambda f: f.split(".")[-1] == "acf", files))

        for f in acf_files:
            with open("{}/{}".format(acf_path, f), "r") as file:
                fcontent = acf.load(file)
                self.games_dict.update({fcontent["AppState"]["name"]: Game(name=fcontent["AppState"]["name"],
                                                                           appid=fcontent["AppState"]["appid"],
                                                                           extra_info=fcontent["AppState"])
                                        })

    def start_game(self, game):
        if self.steam_path is not None and game is not None:
            os.system("{}/steam.exe -applaunch {}".format(self.steam_path, game))
            return True
        return False

# GETTER

    def get_game_names(self):
        return list(self.games_dict.keys())

    def get_gameid_by_name(self, name):
        if name in self.games_dict:
            return self.games_dict[name].appid
        else:
            return None
