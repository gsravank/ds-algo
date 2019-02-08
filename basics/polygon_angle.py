"""
https://codeforces.com/contest/1096/problem/C
"""
from fractions import Fraction


n = int(input())

for _ in range(n):
    angle = int(input())
    f = Fraction(180, angle)
    if f.denominator <= f.numerator - 2:
        print(f.numerator)
    else:
        print(2 * f.numerator)
