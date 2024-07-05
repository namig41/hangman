from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def check(self, user_input):
        pass