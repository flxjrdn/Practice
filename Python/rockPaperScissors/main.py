
import random


def get_user_choice():
    while True:
        choice = ask_user()
        if choice in RPS:
            return choice
        else:
            print('Invalid input. Valid inputs are \'rock\', \'paper\', \'scissors\'.')


def ask_user():
    return input('choose one: [rock], [paper], [scissors]?')


def compare():
    # order is: rock, paper, scissors
    diff = (RPS.index(choice_user) - RPS.index(choice_comp)) % 3
    if diff == 1:    # 1 ; -2
        return WIN
    elif diff == 2:  # -1; 2
        return LOSS
    elif diff == 0:  # 0
        return DRAW


def print_result():
    print('Your choice:       ', choice_user)
    print('Computer\'s choice: ', choice_comp)
    if result == WIN:
        print('YOU WIN!')
    elif result == LOSS:
        print('YOU LOSE!')
    elif result == DRAW:
        print('Draw... Go again.')


if __name__ == '__main__':
    RPS = ['rock', 'paper', 'scissors']
    WIN = 0
    LOSS = 1
    DRAW = 2

    while True:
        choice_comp = RPS[random.randint(0, 2)]
        choice_user = get_user_choice()
        result = compare()
        print_result()
        if result != DRAW:
            break




