"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/

Key fact to note is Fermat's Little Theorem:

if P is prime

A^P = A mod P

so

A^-1 mod P = A^P-2 mod P


"""


import math


MOD = (10 ** 9) + 7
t = int(input())


# def mod_inverse(a, m):
#     m0 = m
#     y = 0
#     x = 1
#
#     if (m == 1):
#         return 0
#
#     while (a > 1):
#         # q is quotient
#         q = a // m
#
#         t = m
#
#         # m is remainder now, process
#         # same as Euclid's algo
#         m = a % m
#         a = t
#         t = y
#
#         # Update x and y
#         y = x - q * y
#         x = t
#
#         # Make x positive
#     if (x < 0):
#         x = x + m0
#
#     return x


# Iterative Function to calculate
# (x^y)%p in O(log y)

def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    while y > 0:

        # If y is odd, multiply
        # x with result
        if (y & 1) == 1:
            res = (res * x) % p

            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def mod_inverse(a, m):
    return power(a, m - 2, m)


for _ in range(t):
    n, k, m = list(map(int, input().strip().split()))
    if n == 1:
        p = 1
        q = 1
        print((p * mod_inverse(q, MOD)) % MOD)
    else:
        x = int(math.ceil(float(m + 1) / 2.0))
        if m % 2 == 1:
            n_x = power(n, x, MOD)
            n_1_x = power(n-1, x, MOD)
            den_inv = power(n, x*(MOD-2), MOD)

            answer = (((n_x - n_1_x) % MOD) * den_inv) % MOD
        else:
            den_1 = power(n, (x-1)*(MOD-2), MOD)
            den_2 = power(n+k, MOD-2, MOD)
            den_inv = (den_1 * den_2) % MOD

            n_x_1 = power(n, x-1, MOD)
            n_1_x_1 = power(n - 1, x - 1, MOD)

            num = ( (n_x_1 * (n+k)) - ((n+k) * n_1_x_1) + n_1_x_1 ) % MOD
            answer = (num * den_inv) % MOD
        print(answer)
