from random_word import RandomWords


class Hangman:
    __MAX_NUM_FAILED = 10

    def __init__(self):
        self.word = ''
        self.known_letters = ''
        self.num_failed = 0
        self.guess = ''
        self.prev_guesses = []

    def init_known_letters_as_underscores(self):
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
                    self.prev_guesses.append(guess)
                    self.guess = guess
                    break
                else:
                    print('This letter has already been guessed. Go again.')
            else:
                print('Invalid input. Choose a single letter.')

    def update_known_letters(self, matches):
        kl = [letter for letter in self.known_letters]
        for i in matches:
            kl[i] = self.word[i]
        self.known_letters = ''.join(kl)

    def check_guess(self):
        matches = [i for i, letter in enumerate(self.word) if letter == self.guess]
        if len(matches) == 0:
            self.num_failed += 1
            print('No match.')
            print('Error count:',
                  self.num_failed, '/', self.__MAX_NUM_FAILED)
        else:
            self.update_known_letters(matches)
            print('Nice.')

    def play(self):
        self.choose_word()
        self.init_known_letters_as_underscores()
        print('Can you find the chosen word?')
        print(self.known_letters)

        while True:
            self.guess_letter()
            self.check_guess()
            print(self.known_letters)
            if self.num_failed == self.__MAX_NUM_FAILED:
                print('You lost this time.')
                print('The word was:', self.word)
                break
            elif self.known_letters == self.word:
                print('You win!')
                break
            print('Previous guesses:', ', '.join(self.prev_guesses))
