import os
from abc import ABC, abstractmethod


class Render(ABC):

    @abstractmethod
    def clear(self):
        """
        Метод для очистки экрана или интерфейса.
        """
        pass

    @abstractmethod
    def show(self):
        """
        Абстрактный метод для отображения содержимого.
        """
        pass

    @abstractmethod
    def update(self):
        """
        Абстрактный метод для обновления содержимого.
        """
        pass
