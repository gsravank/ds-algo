t = int(input())


def get_gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        f = x % y
        x = y
        y = f

    return x


def get_lcm(x, y):
    return x*y/get_gcd(x, y)


for _ in range(t):
    n, a, b, k = list(map(int, input().split()))

    fa = int(n / a)
    fb = int(n / b)
    fab = int(n / get_lcm(a, b))
    f = fa + fb - (2 * fab)

    # print(fa, fb, fab, f)

    if f >= k:
        print("Win")
    else:
        print("Lose")
