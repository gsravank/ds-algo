t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    a = list()
    b = list()
    s = list()

    for _ in range(n):
        ai, bi, si = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)
        s.append(si)

    c = list()
    d = list()
    r = list()
    for _ in range(m):
        ci, di, ri = list(map(int, input().split()))
        c.append(ci)
        d.append(di)
        r.append(ri)



