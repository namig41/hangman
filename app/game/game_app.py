from game.game_state import GameState
from game.game_board import ConsoleGameBoard
from game.game_state import State

from menu.menu_action import MenuAction


class GameApp(MenuAction):

    def __init__(self):
        self.game_state = GameState()
        self.game_board = ConsoleGameBoard()

    def run(self):

        self.game_state.load_word_database()
        self.game_state.init_word()

        while self.game_state.game_state == State.PLAYING:
            self.game_board.update(self.game_state)
            letter = self.input()

            if self.game_state.check_letter(letter):
                self.game_state.add_letter(letter)
            else:
                self.game_state.update_mistakes()

            self.game_state.check_game_over()

        self.game_board.update(self.game_state)
        self.pause()
        self.game_state.reset()

    def start_new_game(self):
        self.game_state.reset()
        self.game_state.init_word()

    def input(self):
        letter = input("Введите букву: ")
        return letter

    def pause(self):
        input("Введите любой символ для продолжения: ")


class GameAppExit(MenuAction):
    def run(self):
        exit()
