import eel
import json


@eel.expose
def start_game(handler, game):
    handler.start_game(handler.get_gameid_by_name(game))


def _json_wrap(data):
    return
