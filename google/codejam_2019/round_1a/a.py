def get_answer(R, C):

    return 1


for ti in range(int(input())):
    R, C = list(map(int, input().strip().split()))
    answer = get_answer(R, C)
    print("Case #{}: {}".format(ti + 1, answer))
