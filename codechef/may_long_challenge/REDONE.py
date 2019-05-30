MOD = 10**9 + 7

fact = dict()
fact[1] = 2
for n in range(2, 10**6 + 1):
    fact[n] = ( (n+1) * fact[n-1] ) % MOD

for _ in range(int(input())):
    n = int(input())

    print((fact[n] - 1) % MOD)



"""
2
1
2

"""