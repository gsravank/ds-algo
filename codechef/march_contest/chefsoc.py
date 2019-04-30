MOD = (10 ** 9) + 7

"""
DP(last_used, mask):
     ret=0
     for all i unmarked in mask:
          //we try to place number i at current position
          if abs(i-last_used) <= K:
          //last_used is now i
          //we pass new mask by setting i’th bit in it
          ret += DP(i, mask|(1<<i))
     return ret
"""



def dp(last_used, mask):
    ret = 0


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))