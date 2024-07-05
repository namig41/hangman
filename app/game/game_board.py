import os
from abc import ABC, abstractmethod

from game.game_state import State


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
        if game_state.game_state == State.PLAYING:
            print(game_state.current_word)

            print(f"Слово: {game_state.letters}")
            print(f"Ошибки: ({game_state.current_number_mistakes})")

        elif game_state.game_state == State.WIN:
            print(f"Вы выиграли!")
            print(f"Ваше слово: {game_state.current_word}")
            print(f"Ошибки:  {game_state.current_number_mistakes}")
            print(f"Количество побед: {game_state.win_score}")
            print(f"Количество поражений: {game_state.lose_score}")

        elif game_state.game_state == State.LOSE:
            print(f"Вы проиграли!")
            print(f"Ваше слово: {game_state.current_word}")
            print(f"Количество побед: {game_state.win_score}")
            print(f"Количество поражений: {game_state.lose_score}")

    def update(self, game_state):
        self.clear()
        self.render(game_state)
