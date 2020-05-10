import random
import sys


COIN_CHOICES = [1, 5, 10, 25]


def take_left(coins):
    coin, *coins = coins
    return coin, coins


def take_right(coins):
    *coins, coin = coins
    return coin, coins


MOVES = [take_left, take_right]


def best_outcome(coins):

    def compute_taken(move, coins):
        coin, coins = move(coins)
        __, other_taken, taken = best_outcome(coins)
        return move, taken + [coin], other_taken

    if len(coins) == 1:
        return take_left, coins, []

    if len(coins) == 2:
        left, right = coins
        return (take_left, [left], [right]) if left >= right else (take_right, [right], [left])

    outcomes = [compute_taken(m, coins) for m in MOVES]
    return max(outcomes, key=lambda outcome: sum(outcome[1]))


def main():

    def print_state():
        total_machine = sum(taken_machine)
        total_user = sum(taken_user)
        print(f'User: {total_user} Machine: {total_machine}')
        if coins:
            print(' '.join(str(coin) for coin in coins))
        else:
            print('User wins.' if total_user > total_machine else 'Machine wins.')

    def play_machine(coins):
        moves = {
                take_left: 'left',
                take_right: 'right',
        }
        move, taken, __ = best_outcome(coins)
        print_state()
        print(f"Machine takes {moves[move]}.")
        return move(coins)

    def play_user(coins):
        moves = {
                'L': lambda: take_left(coins),
                'R': lambda: take_right(coins),
                'Q': lambda: sys.exit()
        }
        while True:
            print_state()
            choice = input('Choose left (L) or right (R).')
            choice = choice.strip().upper()
            move = moves.get(choice)
            if move:
                break
        return move()

    n = 6
    coins = random.choices(COIN_CHOICES, k=2 * n)
    coins = list(coins)
    taken_machine = []
    taken_user = []
    while coins:
        coin, coins = play_user(coins)
        taken_user += [coin]
        coin, coins = play_machine(coins)
        taken_machine += [coin]
        print('-' * 20)
    print_state()


if __name__ == '__main__':
    main()
