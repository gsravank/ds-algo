t = int(input())
c = 10**9

def print_query(x, y):
    print('Q {} {}'.format(x, y), flush=True)


def print_answer(xl, yl, xu, yu):
    print('A {} {} {} {}'.format(xl, yl, xu, yu), flush=True)


for _ in range(t):
    print_query(0, 0)
    a1 = int(input())
    print_query(0, c)
    a2 = int(input())
    print_query(c, c)
    a3 = int(input())
    print_query(c, 0)
    a4 = int(input())

    xmid = int((a2 - a3 + c) / 2)
    # print('xmid: {}'.format(xmid), flush=True)
    print_query(xmid, 0)

    yl = int(input())
    xl = a1 - yl
    yu = xl - a2 + c
    xu = (2*c) - a3 - yu
    print_answer(xl, yl, xu, yu)

    verdict = int(input())

"""
1
Q 0 0
3
Q 0 1000000000
999999997
Q 1000000000 1000000000
1999999993
Q 1000000000 0
999999999
xmid: 2
Q 2 0
2
A 1 2 3 4
"""


