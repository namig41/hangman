from core.listener import Listener

class GameListener(Listener):
    def read(self):
        letter = int(input("Буква: "))
        return letter
    
    def check(self, user_input):
        pass