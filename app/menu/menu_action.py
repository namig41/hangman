from abc import ABC, abstractmethod


class MenuAction(ABC):

    @abstractmethod
    def run():
        pass
