import os

from menu.menu_listener import MenuListener
from core.render import Render


class MenuItem:
    """
    Инициализация пункта меню.
    :param name: Название пункта меню.
    :param action: Действие, выполняемое при выборе пункта меню.
    """

    def __init__(self, name, action=None):

        self.name = name
        self.action = action
        self.submenu = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_submenu(self, submenu_item):
        """
        Добавление подпункта меню.
        :param submenu_item: Подпункт меню.
        """
        self.submenu.append(submenu_item)


class Menu(Render):
    def __init__(self):
        self.items = []

        self.title = """
 _   _                                         
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/  
        """

        self.menu_listener = MenuListener()

    def add_item(self, item):
        """
        Добавление пункта в меню.
        :param item: Пункт меню.
        """
        self.items.append(item)

    def clear(self):
        """
        Очистка экрана.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def show(self):
        """
        Отображение меню и обработка выбора пользователя.
        """

        while True:
            # Очистка и вывод заголовка
            self.clear()
            print(self.title)

            # Вывод пунктов меню
            for idx, item in enumerate(self.items):
                print(f"{idx + 1}. {item}")

            # Чтение ввода данных пользователя и проверка на правильность
            choice = self.menu_listener.read()
            if not self.menu_listener.is_valid(choice):
                print("Неправильный ввод")
                continue

            # DOTO: Необходимо вынести дополнительную проверку
            # в метод is_valid класса MenuListener
            # Дополнильная проверка на правильность выбора пункта меню
            choice = int(choice)
            if 0 < choice <= len(self.items):
                item = self.items[choice - 1]
                if item.action:
                    # Запуск выбранного меню
                    item.action.run()
                else:
                    continue
            else:
                print("Неправильный ввод")

    def update(self):
        """
        Обновление меню.
        """
        self.clear()
        self.show()
