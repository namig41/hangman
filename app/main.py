from menu.menu import Menu, MenuItem
from game.game_app import GameApp, GameAppExit

if __name__ == "__main__":

    menu = Menu()
    menu.add_item(MenuItem("Играть", GameApp()))
    menu.add_item(MenuItem("Выйти", GameAppExit()))

    menu.show()
