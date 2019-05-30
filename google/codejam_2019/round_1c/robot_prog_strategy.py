from collections import defaultdict

win_move = dict()
win_move['R'] = 'P'
win_move['P'] = 'S'
win_move['S'] = 'R'

lose_move = dict()
lose_move['P'] = 'R'
lose_move['S'] = 'P'
lose_move['R'] = 'S'


def get_strategy(A, C):
    player_alive = defaultdict(lambda: True)
    curr_idx = [0 for _ in range(A)]

    done = False
    found = False
    strategy_moves = list()
    while not done:
        curr_moves = list()
        for idx in range(A):
            if player_alive[idx]:
                curr_moves.append(C[idx][curr_idx[idx]])
                curr_idx[idx] = (curr_idx[idx] + 1) % len(C[idx])

        unique_curr_moves = set(curr_moves)
        if len(unique_curr_moves) == 3:
            done = True
        elif len(unique_curr_moves) == 1:
            strategy_moves.append(win_move[list(unique_curr_moves)[0]])
            done = True
            found = True
        else:
            if 'P' not in unique_curr_moves:
                strategy_moves.append('R')
                curr_win_move = 'R'
            elif 'R' not in unique_curr_moves:
                strategy_moves.append('S')
                curr_win_move = 'S'
            else:
                strategy_moves.append('P')
                curr_win_move = 'P'

            curr_lose_move = lose_move[curr_win_move]
            for idx in range(A):
                if C[idx][(curr_idx[idx] - 1) % len(C[idx])] == curr_lose_move:
                    player_alive[idx] = False

    if found:
        return ''.join(strategy_moves)
    else:
        return 'IMPOSSIBLE'


for ti in range(int(input())):
    A = int(input())
    C = list()
    for _ in range(A):
        C.append(input())

    print("Case #{}: {}".format(ti + 1, get_strategy(A, C)))


"""
3
1
RS
3
R
P
S
7
RS
RS
RS
RS
RS
RS
RS

"""