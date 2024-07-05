import random

class GameState:

    def __init__(self):
        self.game_running = True
        self.score = 0
        self.letters = []
        self.current_word = ""
        self.word_length =  0
        self.max_number_mistakes = 10
        self.current_number_mistakes = 0
        self.word_database = []


    def load_word_database(self):
        with open('data/nouns.txt', 'r') as file:
            for line in file:
                self.word_database.append(line.strip())


    def get_random_word(self):
        return random.choice(self.word_database)


    def check_word(self, word):
        if word in self.word_database:
            return True
        else:
            return False


    def check_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            return False
        
    def init_word(self):
        self.current_word = self.get_random_word()
        self.word_length = len(self.current_word)
        self.letters = []
        self.current_number_mistakes = 0
        self.score = 0


    def update_score(self):
        self.score += 1


    def update_mistakes(self):
        self.current_number_mistakes += 1


    def check_game_over(self):
        self.game_running = self.current_number_mistakes >= self.max_number_mistakes

    def reset(self):
        self.game_running = True
        self.letters = []
        self.current_word = ""
        self.word_length =  0
        self.max_number_mistakes = 10
        self.current_number_mistakes = 0
        self.word_database = []





































































