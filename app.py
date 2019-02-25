from core.game_interfaces.steam.steam_handling import SteamHandler
from core.interface_handling.multi_lib_interface import MultiLibInterface
import eel


@eel.expose
def start_game(game):
    steam_handler.start_game(steam_handler.get_gameid_by_name(game))


# TODO windows path stuff
muli = MultiLibInterface()
steam_handler = SteamHandler("D:/Steam")

eel.init("web")

start_opt = {"chromeFlags": ["--incognito"]}

# steam_handler.start_game("499440")
# print(steam_handler.get_game_names())

eel.start("main.html", block=False, options=start_opt)

while True:
    eel.sleep(1)
