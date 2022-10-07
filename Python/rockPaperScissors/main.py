
import random


if __name__ == '__main__':
    rps = ['rock', 'paper', 'scissors']

    choice_comp = rps[random.randint(0, 2)]

    choice_user = input('choose one: [rock], [paper], [scissors]?')
    while choice_user not in rps:
        print('Invalid input. Valid inputs are \'rock\', \'paper\', \'scissors\'.')
        choice_user = input('[rock], [paper], [scissors]?')
