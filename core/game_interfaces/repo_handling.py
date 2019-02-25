from abc import ABC, abstractmethod


class RepoHandler(ABC):
    def __init__(self):
        self.game_list = list()

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
