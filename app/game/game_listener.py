import re

from core.listener import Listener


class GameListener(Listener):
    def read(self):
        """
        Метод для чтения ввода пользователя (буквы).
        :return: Введенная пользователем буква.
        """
        letter = input("Буква: ")
        return letter

    def is_valid(self, user_input):
        """
        Метод для проверки валидности введенной пользователем буквы.
        :param user_input: Введенная пользователем буква.
        :return: True, если буква валидна (одна буква и кириллическая), иначе False.
        """

        # Проверка на длину (должна быть ровно одна буква)
        if len(user_input) != 1:
            return False

        # Проверка на наличие кириллической буквы
        if not bool(re.search('[а-яА-Я]', user_input)):
            return False

        return True
