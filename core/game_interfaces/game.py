from collections import OrderedDict


class Game:
    def __init__(self, name, appid, img_src, extra_info):
        self.name = name
        self.appid = appid
        self.img_src = img_src
        self.extra_info = OrderedDict(extra_info)
