import heapq as hp
import math


for _ in range(int(input())):
    N, A, B, X, Y, Z = list(map(int, input().strip().split()))
    C = list(map(int, input().strip().split()))
    C = [-x for x in C]
    hp.heapify(C)

    done = False
    sum_till_now = 0
    num_conts = 0
    found = False
    # print("Z = {}, A = {}, B = {}".format(Z, A, B))

    t1 = int(math.ceil((Z - sum_till_now - A) / X))
    h_t1 = B + (t1 * Y)
    if h_t1 < Z:
        found = True
        done = True

    while not done:
        # print('\n')
        # print(C)
        top = (-1 * C[0])

        if top == 0:
            done = True
        else:
            half_of_top = -1 * int(top / 2)
            hp.heapreplace(C, half_of_top)

            sum_till_now += top
            num_conts += 1
            t1 = int(math.ceil((Z - sum_till_now - A) / X))
            # print(sum_till_now, A)
            # print(Z - sum_till_now - A, X)
            h_t1 = B + (t1 * Y)
            # print(t1, h_t1)
            if h_t1 < Z:
                found = True
                done = True

    if found:
        print(num_conts)
    else:
        print("RIP")
    # print('\n========\n')

"""
3
3 10 15 5 10 100
12 15 18
3 10 15 5 10 100
5 5 10
4 40 80 30 30 100
100 100 100 100

"""