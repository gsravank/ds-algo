from collections import defaultdict


def is_even_power_of_two(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            count += 1
            n = int(n/2)
        else:
            return False

    return count % 2 == 0

def is_odd_power_of_two(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            count += 1
            n = int(n / 2)
        else:
            return False

    return count % 2 == 1


def f(n, parity, game_dict):
    if parity == 0:
        if is_even_power_of_two(n):
            game_dict[n][parity] = False
            return False
        elif is_odd_power_of_two(n):
            game_dict[n][parity] = True
            return True
    else:
        if is_even_power_of_two(n-1):
            game_dict[n][parity] = True

    print(n, parity)
    if n in game_dict:
        if parity in game_dict[n]:
            return game_dict[n][parity]

    if n == 1 and parity == 0:
        game_dict[n][parity] = True
        # print(n, parity, True)
        return True
    elif n == 1 and parity == 1:
        game_dict[n][parity] = False
        # print(n, parity, False)
        return False
    else:
        if n % 2 == 0:
            answer = f(int(n/2), 1-parity, game_dict)
        else:
            x1 = f(n+1, 1-parity, game_dict)
            x2 = f(n-1, 1-parity, game_dict)
            answer = x1 or x2
        game_dict[n][parity] = answer
        return answer

#
# game_dict = defaultdict(lambda: dict())
# print(f(6, 0, game_dict))
#
# print(game_dict)

print(is_even_power_of_two(2))