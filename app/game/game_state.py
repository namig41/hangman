import random
from enum import Enum


class State(Enum):
    PLAYING = 1,
    LOSE = 2,
    WIN = 3,


class GameState:
    """
    Инициализация состояния игры.
    """

    def __init__(self):

        # Текущее состояние игры
        self.game_state = State.PLAYING
        # Очки игрока
        self.score = 0
        # Количество побед
        self.win_score = 0
        # Количество поражений
        self.lose_score = 0
        # Список букв в текущем слове
        self.letters = []
        # Текущее загаданное слово
        self.current_word = ""
        # Длина текущего слова
        self.word_length = 0
        # Максимальное количество ошибок
        self.max_number_mistakes = 10
        # Текущее количество ошибок
        self.current_number_mistakes = 0
        # База слов
        self.word_database = []
        # Множество использованных букв
        self.used_letters = set()

    def load_word_database(self, path='app/data/nouns.txt'):
        """
        Загрузка базы слов из файла 'app/data/nouns.txt'.
        """
        with open(path, 'r') as file:
            for line in file:
                self.word_database.append(line.strip())

    def get_random_word(self):
        """
        Получение случайного слова из базы слов.
        :return: Случайное слово.
        """
        return random.choice(self.word_database)

    def check_letter(self, letter):
        """
        Проверка, содержится ли данная буква в текущем слове.
        :param letter: Проверяемая буква.
        :return: True, если буква присутствует в слове, иначе False.
        """

        # Добавление букву в список использованных
        self.used_letters.add(letter)
        return letter in self.current_word

    def find_letter(self, letter):
        """
        Найти индекс первого вхождения буквы в текущем слове.
        :param letter: Искомая буква.
        :return: Индекс буквы в слове.
        """
        index = self.letters.index(letter)
        return index

    def init_word(self):
        """
        Инициализация нового слова для игры.
        """
        # Выбираем случайное слово
        self.current_word = self.get_random_word()
        # Определяем его длину
        self.word_length = len(self.current_word)
        # Создаем список пустых мест для букв
        self.letters = ['_'] * self.word_length
        # Сбрасываем количество ошибок
        self.current_number_mistakes = 0
        # Сбрасываем счет
        self.score = 0

    def update_score(self):
        """
        Обновление счета (количество отгаданных букв).
        """
        self.score += 1

    def update_mistakes(self):
        """
        Увеличение количества ошибок на 1.
        """
        self.current_number_mistakes += 1

    def check_game_over(self):
        """
        Проверка условий завершения игры: достигнуто максимальное количество ошибок или отгаданы все буквы.
        """
        if self.current_number_mistakes >= self.max_number_mistakes:
            self.game_state = State.LOSE
            self.lose_score += 1
        elif self.score == self.word_length:
            self.game_state = State.WIN
            self.win_score += 1

    def reset(self):
        """
        Сброс состояния игры.
        """
        # Сброс текущего состояния игры
        self.game_state = State.PLAYING
        # Очистка списка букв
        self.letters = []
        # Очистка текущего слова
        self.current_word = ""
        # Сброс длины слова
        self.word_length = 0
        # Сброс текущего числа ошибок
        self.current_number_mistakes = 0
        # Очистка базы слов
        self.word_database = []
        # Очистка использованных букв
        self.used_letters = set()

    def add_letter(self, letter):
        """
        Добавление угаданной буквы в список отгаданных.
        :param letter: Угаданная буква.
        """

        for index, character in enumerate(self.current_word):
            if letter == character and self.letters[index] == '_':
                self.letters[index] = letter
                self.update_score()

    def get_used_letters(self):
        """
        Получение строки с использованными буквами.
        :return: Строка с использованными буквами, разделенными запятой.
        """
        return ", ".join(self.used_letters)

    def get_letters(self):
        """
        Получение строки с текущим состоянием отгаданных букв.
        :return: Строка, где пустые места обозначены символом '_'.
        """
        return " ".join(self.letters)
