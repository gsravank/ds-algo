n, m = list(map(int, input().strip().split()))
MOD = (10**9) + 7

l = [1] * (m-1)
l += [2]
# print(l)

for i in range(m, n):
    # print(l)

    mi = i % m
    mi1 = (i-1) % m

    l[mi] += l[mi1]
    l[mi] = l[mi] % MOD

print(l[(n-1) % m])