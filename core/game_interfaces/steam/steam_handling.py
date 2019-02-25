import os

from steamfiles import acf

from core.game_interfaces.game import Game
from core.game_interfaces.repo_handling import RepoHandler


class SteamHandler(RepoHandler):
    def __init__(self, steam_path):
        super().__init__()

        self.steam_path = steam_path

        self._load_games()

    def _load_games(self):
        acf_path = "{}/steamapps".format(self.steam_path)
        files = os.listdir(acf_path)

        acf_files = list(filter(lambda f: f.split(".")[-1] == "acf", files))

        for f in acf_files:
            with open("{}/{}".format(acf_path, f), "r") as file:
                fcontent = acf.load(file)
                self.game_list.append(Game(name=fcontent["AppState"]["name"],
                                           appid=fcontent["AppState"]["appid"],
                                           extra_info=fcontent["AppState"]))

    def start_game(self, game):
        os.system("{}/steam.exe -applaunch {}".format(self.steam_path, game))

# GETTER

    def get_game_names(self):
        names = list()

        for game in self.game_list:
            names.append(game.name)

        return names

    def get_gameid_by_name(self, name):
        for game in self.game_list:     # TODO better searching
            if game.name == name:
                return game.appid
        return None
