import random
from enum import Enum


class State(Enum):
    PLAYING = 1,
    LOSE = 2,
    WIN = 3,


class GameState:

    def __init__(self):
        self.game_state = State.PLAYING
        self.score = 0
        self.win_score = 0
        self.lose_score = 0
        self.letters = []
        self.current_word = ""
        self.word_length = 0
        self.max_number_mistakes = 10
        self.current_number_mistakes = 0
        self.word_database = []

    def load_word_database(self):
        with open('app/data/nouns.txt', 'r') as file:
            for line in file:
                self.word_database.append(line.strip())

    def get_random_word(self):
        return random.choice(self.word_database)

    def check_letter(self, letter):
        return letter in self.current_word

    def find_letter(self, letter):
        index = self.letters.index(letter)
        return index

    def init_word(self):
        self.current_word = self.get_random_word()
        self.word_length = len(self.current_word)
        self.letters = ['_'] * self.word_length
        self.current_number_mistakes = 0
        self.score = 0

    def update_score(self):
        self.score += 1

    def update_mistakes(self):
        self.current_number_mistakes += 1

    def check_game_over(self):
        if self.current_number_mistakes >= self.max_number_mistakes:
            self.game_state = State.LOST
            self.lose_score += 1
        elif self.score == self.word_length:
            self.game_state = State.WIN
            self.win_score += 1

    def reset(self):
        self.game_state = State.PLAYING
        self.letters = []
        self.current_word = ""
        self.word_length = 0
        self.max_number_mistakes = 10
        self.current_number_mistakes = 0
        self.word_database = []

    def add_letter(self, letter):
        for index, character in enumerate(self.current_word):
            if letter == character and self.letters[index] == '_':
                self.letters[index] = letter
                self.update_score()
