import os
from abc import ABC, abstractmethod

from game.game_state import State
from core.render import Render


class ConsoleGameBoard(Render):
    def clear(self):
        """
        Метод для очистки экрана консоли.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def show(self, game_state):
        """
        Метод для отображения текущего состояния игры.
        :param game_state: Объект игрового состояния GameState.
        """
        if game_state.game_state == State.PLAYING:
            print(f"Слово: {game_state.get_letters()}")
            print(f"Использованые буквы: {game_state.get_used_letters()}")
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
        """
        Метод для обновления отображения игровой доски.
        :param game_state: Объект игрового состояния GameState.
        """
        self.clear()
        self.show(game_state)
