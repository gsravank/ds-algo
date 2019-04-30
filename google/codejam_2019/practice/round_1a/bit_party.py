def get_min_time(R, B, C, M, S, P):
    return


for ti in range(int(input())):
    R, B, C = list(map(int, input().strip().split()))

    M = list()
    S = list()
    P = list()

    for _ in range(C):
        mi, si, pi = list(map(int, input().strip().split()))

        M.append(mi)
        S.append(si)
        P.append(pi)

    print("Case #{}: {}".format(ti + 1, get_min_time(R, B, C, M, S, P)))



