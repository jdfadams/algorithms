import random


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
        ret = best_outcome(coins)
        other_taken, taken = ret
        return taken + [coin], other_taken

    if len(coins) == 1:
        return coins, []

    if len(coins) == 2:
        left, right = coins
        return ([left], [right]) if left >= right else ([right], [left])

    outcomes = [compute_taken(m, coins) for m in MOVES]
    return max(outcomes, key=lambda pair: sum(pair[0]))


def main():
    coins = random.choices([1, 5, 10, 25], k=10)
    print('Coins:', coins)
    taken, other_taken = best_outcome(coins)
    print('Taken:', taken, 'Total:', sum(taken))
    print('Other:', other_taken, 'Total:', sum(other_taken))


if __name__ == '__main__':
    main()
