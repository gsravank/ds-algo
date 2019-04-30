n, q = list(map(int, input().split()))
f = list(map(int, input().split()))

cum_f = list()
curr = 0
cum_f.append(curr)
for fi in f:
    curr = curr ^ fi
    cum_f.append(curr)

for _ in range(q):
    k = int(input())
    print(cum_f[k % (n+1)])

"""
3 4
0 1 2
7
2
5
1000000000

"""