from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения ввода.
        """
        pass

    @abstractmethod
    def is_valid(self, user_input):
        """
        Абстрактный метод для проверки валидности ввода.
        :param user_input: Введенное пользователем значение.
        :return: True, если ввод валиден, иначе False.
        """
        pass
