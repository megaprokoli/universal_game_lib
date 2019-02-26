from core.interface_handling.multi_lib_interface import MultiLibInterface
import eel


@eel.expose
def start_game(game):
    handler = muli.game_interfaces["steam"]

    if not handler.start_game(handler.get_gameid_by_name(game)):
        print("gamestart failed")


# TODO windows path stuff
muli = MultiLibInterface()
# steam_handler = SteamHandler()

muli.init_interfaces(silent=False)
eel.init("web")

start_opt = {"chromeFlags": ["--incognito"]}

# steam_handler.start_game("499440")
# print(steam_handler.get_game_names())

eel.start("main.html", block=False, options=start_opt)

while True:
    eel.sleep(1)
