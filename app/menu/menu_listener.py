from core.listener import Listener

class MenuListener(Listener):
    def read(self):
        num_menu = int(input("Выберите пункт меню: "))
        return num_menu
    
    def check(self, user_input) -> bool:
        pass