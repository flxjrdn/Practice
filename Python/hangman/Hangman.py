from random_word import RandomWords


class Hangman:
    __MAX_NUM_FAILED = 12

    def __init__(self):
        self.word = ''
        self.known_letters = ''
        self.num_failed = 0
        self.guess = ''
        self.prev_guesses = []

    def print_word(self):
        print(self.word)

    def initialize_known_letters(self):
        self.known_letters = ''.join(['_' for c in self.word])

    def choose_word(self):
        rw = RandomWords()
        self.word = rw.get_random_word()
        self.word = self.word.lower()

    def guess_letter(self):
        while True:
            guess = input('Choose a letter:').lower()
            if guess.isalpha() & (len(guess) == 1):
                if guess not in self.prev_guesses:
                    self.guess = guess
                    break
                else:
                    print('This letter has already been guessed. All previously guessed letters are:',
                          self.prev_guesses)
            else:
                print('Invalid input. Choose a single letter.')

    def find_matches(self):
        return [i for i, letter in enumerate(self.word) if letter == self.guess]

    def update_known_letters(self, matches):
        kl = [letter for letter in self.known_letters]
        for i in matches:
            kl[i] = self.word[i]
        self.known_letters = ''.join(kl)

    def check_guess(self):
        matches = self.find_matches()
        if len(matches) == 0:
            self.num_failed += 1
            print('The chosen letter does not occur in the word. Error count:',
                  self.num_failed, '/', self.__MAX_NUM_FAILED)
        else:
            self.update_known_letters(matches)
            print('Nice.')
            print(self.known_letters)

    def play(self):
        self.choose_word()
        self.initialize_known_letters()
        print('Can you find the chosen word?')
        print(self.known_letters)
        print(self.word)

        self.guess_letter()
        self.check_guess()
