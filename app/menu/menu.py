class MenuItem:
    def __init__(self, name, action=None):

        self.name = name
        self.action = action
        self.submenu = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_submenu(self, submenu_item):
        self.submenu.append(submenu_item)


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show(self):
        while True:
            for idx, item in enumerate(self.items):
                print(f"{idx + 1}. {item}")

            try:
                choice = int(input("Введите номер: "))
                if 0 < choice <= len(self.items):
                    item = self.items[choice - 1]
                    if item.action:
                        item.action.run()
                    else:
                        continue
                else:
                    print("Неправильный ввод")
            except ValueError:
                print("Неправильный ввод")
