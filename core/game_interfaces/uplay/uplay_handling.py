from core.game_interfaces.game import Game
from core.game_interfaces.repo_interface import RepoInterface


class UplayInterface(RepoInterface):
    def __init__(self, name):
        super().__init__(name)

    def initialize(self):
        super().initialize()

    def _load_config(self):
        super()._load_config()

    def _load_games(self):
        super()._load_games()

    def get_gameid_by_name(self, name):
        super().get_gameid_by_name(name)

    def start_game(self, game):
        super().start_game(game)

    def get_game_names(self):
        super().get_game_names()
