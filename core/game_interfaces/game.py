from collections import OrderedDict


class Game:
    def __init__(self, name, appid, extra_info):
        self.name = name
        self.appid = appid
        self.extra_info = OrderedDict(extra_info)
