import os

from core.game_interfaces.game import Game
from core.game_interfaces.repo_interface import RepoInterface


class OriginInterface(RepoInterface):
    def __init__(self, name):
        super().__init__(name)

    def _load_games(self):
        game_dirs = os.listdir(self.config["game_path"])

        for dir_name in game_dirs:
            game_files = os.listdir(self.config["game_path"] + "/" + dir_name)

            mfst_file = list(filter(lambda f: f.split(".")[-1] == "mfst", game_files))

            length = len(mfst_file)
            if length != 1:
                continue

            mfst_file = mfst_file[0]  # extract from list
            mfst_file = os.path.splitext(mfst_file)[0]  # cut extension

            self.games_dict.update({dir_name: Game(name=dir_name,
                                                   appid=mfst_file,
                                                   img_src="",
                                                   extra_info={})
                                    })  # TODO get extra_info

    def start_game(self, game):
        os.system("start origin://launchgame/" + game)
