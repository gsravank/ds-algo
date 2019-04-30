for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    pos_size = 0
    neg_size = 0

    for elem in a:
        if elem > 0:
            pos_size += 1
        else:
            neg_size += 1

    if pos_size == 0 or neg_size == 0:
        print("{} {}".format(n, n))
    else:
        print("{} {}".format(max(pos_size, neg_size), min(pos_size, neg_size)))
