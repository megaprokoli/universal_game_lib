import os

from steamfiles import acf

from core.game_interfaces.game import Game
from core.game_interfaces.repo_interface import RepoInterface


class SteamInterface(RepoInterface):
    def __init__(self, name):
        super().__init__(name)

    def _load_games(self):
        acf_path = "{}/steamapps".format(self.config["path"])
        files = os.listdir(acf_path)

        acf_files = list(filter(lambda f: f.split(".")[-1] == "acf", files))

        for f in acf_files:
            with open("{}/{}".format(acf_path, f), "r") as file:
                fcontent = acf.load(file)
                self.games_dict.update({fcontent["AppState"]["name"]: Game(name=fcontent["AppState"]["name"],
                                                                           appid=fcontent["AppState"]["appid"],
                                                                           img_src=self.config["img_src"]
                                                                           .format(fcontent["AppState"]["appid"]),
                                                                           extra_info=fcontent["AppState"])
                                        })

    def start_game(self, game):
        if self.config["path"] is not None and game is not None:
            os.system("{}/steam.exe -applaunch {}".format(self.config["path"], game))
            return True
        return False
