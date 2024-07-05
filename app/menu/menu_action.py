from abc import ABC, abstractmethod


class MenuAction(ABC):
    @abstractmethod
    def run():
        """
        Абстрактный метод для выполнения действия меню.
        """
        pass
