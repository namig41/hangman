from game_state import GameState
from game_board import GameBoard

class GameApp:

    def __init__(self):
        self.game_state = GameState()
        self.game_board = GameBoard()
        self.game_state.load_word_database()
        self.init_word()

    def run(self):
       while self.game_state.game_running:
           self.game_board.render(self.game_state)
           self.game_state.check_game_over()


    def start_new_game(self):
        self.game_state.reset()
        self.init_word()
