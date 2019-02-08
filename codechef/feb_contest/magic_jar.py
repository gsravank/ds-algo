t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    for elem in a:
        s += (elem - 1)
    s += 1

    print(s)
