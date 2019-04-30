from collections import defaultdict


def f(n, parity, game_dict):
    if n in game_dict:
        if parity in game_dict[parity]:
            return game_dict[n][parity]

    if n == 1 and parity == 0:
        game_dict[n][parity] = True
        return True
    elif n == 1 and parity == 1:
        game_dict[n][parity] = False
        return False
    else:
        if n % 2 == 0:
            answer = f(int(n/2), 1-parity, game_dict)
        else:
            answer = f(n+1, 1-parity, game_dict) or f(n-1, 1-parity, game_dict)
        game_dict[n][parity] = answer
        return answer


def play_game(n):
    game_dict = defaultdict(lambda: dict())

    if f(n, 0, game_dict):
        print(game_dict)
        print("Win", flush=True)

        parity = 0
        while n:
            if parity == 0:
                # A's move
                if n % 2 == 0:
                    n /= 2
                    print("/2", flush=True)
                else:
                    if n == 1:
                        print("-1", flush=True)
                        n -= 1
                    else:
                        if game_dict[n-1][1]:
                            n -= 1
                            print("-1", flush=True)
                        else:
                            n += 1
                            print("+1", flush=True)
                parity = 1
            else:
                # B's move
                b_s_move = input()

                if b_s_move == '/2':
                    n /= 2
                elif b_s_move == '+1':
                    n += 1
                else:
                    n -= 1
                parity = 0

        input()

    else:
        print("Lose", flush=True)
        response = input()

        return


for _ in range(int(input())):
    N = int(input())
    play_game(N)
