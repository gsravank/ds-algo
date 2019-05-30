for _ in range(int(input())):
    n, m = list(map(int, input().strip().split()))

    max_moves_seq = list()
    done = False
    while not done:
        if n % m == 0 or m % n == 0:
            max_moves_seq.append(1)
            done = True
        else:
            if n < m:
                n, m = m, n

            max_moves_seq.append(int(n / m))
            n = n % m

    curr_winner = "Rich"
    curr_loser = "Ari"

    for max_move in max_moves_seq[::-1]:
        if max_move == 1:
            curr_winner, curr_loser = curr_loser, curr_winner
        else:
            if curr_winner == 'Ari':
                pass
            else:
                curr_winner, curr_loser = curr_loser, curr_winner

    print(curr_winner)


"""
5
1 1
2 2
1 3
155 47
6 4

"""