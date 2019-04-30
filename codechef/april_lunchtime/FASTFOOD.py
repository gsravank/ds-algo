for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a_contr = 0
    b_contr = sum(b)
    max_sum = b_contr

    for i in range(n):
        a_contr += a[i]
        b_contr -= b[i]

        max_sum = max(max_sum, a_contr + b_contr)

    print(max_sum)


"""
3
3
2 3 2
10 3 4
4
7 5 3 4
2 3 1 3
2
10 1
1 10

"""