import os

from abc import ABC, abstractmethod


class GameBoard(ABC):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def render(self, game_state):
        pass

    @abstractmethod
    def update(self, game_state):
        pass


class ConsoleGameBoard(GameBoard):
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self, game_state):
        print("_" * game_state.word_length)
        print(f"Ошибки: ({game_state.current_number_mistakes})")
        

    def update(self, game_state):
        self.clear()
        self.render(game_state)

     
