
from random_word import RandomWords

if __name__ == '__main__':
    rw = RandomWords()
    word = rw.get_random_word()

    print('Can you find the chosen word?')
    print('_' * len(word))
    print('The chosen word was:', word)
