from core.listener import Listener


class MenuListener(Listener):
    """
    Читает ввод пользователя для выбора пункта меню.
    :return: Введенное пользователем значение.
    """

    def read(self):
        num_menu = input("Выберите пункт меню: ")
        return num_menu

    """
    Проверяет валидность ввода пользователя.
    :param user_input: Введенное пользователем значение.
    :return: True, если ввод валиден, иначе False.
    """

    def is_valid(self, user_input) -> bool:

        # NOTE: Проверка будет не корректна в случае, если есть больше 9 пунктов меню
        # Проверка, что ввод состоит из одного символа
        if len(user_input) != 1:
            return False

        # Проверка, что ввод является числом
        if not user_input.isdigit():
            return False

        return True
