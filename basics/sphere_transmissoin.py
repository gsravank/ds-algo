from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


n = int(input().strip())
fvs = list()
print(factors(n))

for al in factors(n):
    fvs.append((n / al) + ((n / 2) * ((n / al) - 1)))


for x in sorted(fvs):
    print('{}'.format(int(x)), end=' ')

# print(factors(36))