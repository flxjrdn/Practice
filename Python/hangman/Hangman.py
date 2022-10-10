from random_word import RandomWords


class Hangman:

    def __init__(self):
        self.word = ''
        self.known_letters = ''
        self.num_failed = 0
        self.guess = ''

    def print_word(self):
        print(self.word)

    def print_known_letters(self):
        print(self.known_letters)

    def choose_word(self):
        rw = RandomWords()
        self.word = rw.get_random_word()
        self.word = self.word.lower()

    def get_input_letter(self):
        while True:
            self.guess = input('Choose a letter:')
            if self.guess.isalpha() & len(self.guess) == 1:
                break
            else:
                print('Invalid input. Choose a single letter:')

    def play(self):
        self.choose_word()
        print('Can you find the chosen word?')

        self.print_known_letters()
        self.get_input_letter()
