from menu.menu import Menu, MenuItem

main_menu  =  Menu()

main_menu.add_item(MenuItem("Играть", action=None))
main_menu.add_item(MenuItem("Выход", action=exit))

main_menu.show()