from game.game_state import GameState
from game.game_board import ConsoleGameBoard
from game.game_state import State
from game.game_listener import GameListener

from menu.menu_action import MenuAction


class GameApp(MenuAction):

    def __init__(self):
        """
        Инициализация игрового приложения.
        """

        # Игровое состояние
        self.game_state = GameState()
        # Игровое поле в консоли
        self.game_board = ConsoleGameBoard()
        # Ввод пользователя
        self.game_listener = GameListener()

    def run(self):
        """
        Запуск игры.
        """

        # Загрузка базы слов
        self.game_state.load_word_database()
        # Инициализация слова для игры
        self.game_state.init_word()

        while self.game_state.game_state == State.PLAYING:
            # Обновление игрового поля
            self.game_board.update(self.game_state)

            # Чтение ввода пользователя
            letter = self.game_listener.read()

            # Проверка валидности ввода
            if not self.game_listener.is_valid(letter):
                continue

            # Проверка буквы
            if self.game_state.check_letter(letter):
                # Добавление буквы
                self.game_state.add_letter(letter)
            else:
                # Обновление числа ошибок
                self.game_state.update_mistakes()

            # Проверка завершения игры
            self.game_state.check_game_over()

        # Финальное обновление доски
        self.game_board.update(self.game_state)
        # Пауза перед окончанием
        self.pause()
        # Сброс состояния игры
        self.game_state.reset()

    def start_new_game(self):
        """
        Начать новую игру
        """
        self.game_state.reset()
        self.game_state.init_word()

    def pause(self):
        """
        Пауза перед окончанием игры.
        """
        input("Введите любой символ для продолжения... ")


class GameAppExit(MenuAction):
    def run(self):
        """
        Выход из игрового приложения.
        """
        exit()
