from abc import ABC, abstractmethod


class RepoHandler(ABC):
    def __init__(self, name):
        self.name = name
        self.init_ok = {"state": False, "msg": "not initialized"}
        self.games_dict = dict()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def _load_config(self):
        pass

    @abstractmethod
    def _load_games(self):
        pass

    @abstractmethod
    def start_game(self, game):
        pass

    @abstractmethod
    def get_game_names(self):
        pass

    @abstractmethod
    def get_gameid_by_name(self, name):
        pass
