t = int(input())


def best_defence(a, d, n):
    max_def = -1

    for i in range(n):
        if d[i] > (a[i-1] + a[(i+1) % n]):
            if d[i] > max_def:
                max_def = d[i]

    return max_def


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))

    print(best_defence(a, d, n))