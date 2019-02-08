"""
https://codeforces.com/contest/1096/problem/B
"""
P = 998244353

_ = input()
s = input()

num_first_chars = 0
num_last_chars = 0


for idx in range(len(s)):
    if s[idx] != s[0]:
        break
num_first_chars = idx


for idx in range(len(s)-1, -1 , -1):
    if s[idx] != s[-1]:
        break
num_last_chars = len(s) - 1 - idx
# print(num_first_chars)
# print(num_last_chars)

num_total_ways = 0

if s[0] != s[-1]:
    num_total_ways += (1 + num_first_chars + num_last_chars)
else:
    num_total_ways += (1 + num_first_chars + num_last_chars + (num_first_chars * num_last_chars))

print(num_total_ways % P)