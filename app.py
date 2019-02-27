from core.interface_handling.multi_lib_interface import MultiLibInterface
import eel
import json


@eel.expose
def start_game(game):
    handler = muli.find_by_game(game)

    if handler is None:
        return False

    return handler.start_game(handler.get_gameid_by_name(game))


@eel.expose
def get_game_data():
    games = muli.get_all_gamenames()
    return wrap_data(games)


def wrap_data(ls):
    obj = {"data": ls}
    return json.dumps(obj)


if __name__ == "__main__":
    muli = MultiLibInterface()

    muli.init_interfaces(silent=False)
    eel.init("web")

    start_opt = {"chromeFlags": ["--incognito"]}

    eel.start("main.html", block=False, options=start_opt)

    while True:
        eel.sleep(1)
