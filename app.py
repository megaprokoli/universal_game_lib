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
def get_game_names(filter=None):

    if filter is None:
        games = muli.get_gamenames()
    else:
        games = muli.search(filter)

    return wrap_data(games)


@eel.expose
def get_game_img(game_name):
    game = muli.find_by_game(game_name).games_dict[game_name]

    if game is not None:
        return json.dumps({"img_src": game.img_src})
    else:
        return json.dumps({"img_src": ""})


@eel.expose
def get_game_data(game_name):
    data = dict()
    interface = muli.find_by_game(game_name)
    game = interface.games_dict[game_name]

    if game is not None:

        data.update({"gamename": game.name})
        data.update({"appid": game.appid})
        data.update({"launcher": interface.name})
        data.update({"img_src": game.img_src})
        data.update({"extra": game.extra_info})

        return json.dumps(data)
    else:
        return json.dumps({})


def wrap_data(ls):
    obj = {"data": ls}
    return json.dumps(obj)


if __name__ == "__main__":
    eel.init("web")

    muli = MultiLibInterface(init_fail=eel.display_init_error)
    start_opt = {"chromeFlags": ["--incognito"]}

    muli.init_interfaces(silent=False)

    eel.start("main.html", block=False, options=start_opt)

    while True:
        eel.sleep(1)
