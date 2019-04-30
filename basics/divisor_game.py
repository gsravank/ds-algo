from collections import defaultdict
import math


class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 0:
            return False

        dp = [[i for i in range(2)] for _ in range(N + 1)]
        dp[1][0] = 0
        dp[1][1] = 1

        for i in range(2, N + 1):
            print("n = {}".format(i))
            sqrt_i = int(math.sqrt(i))

            for f1 in range(1, sqrt_i + 1):
                if i % f1 == 0:
                    if dp[i - f1][1]:
                        print("f1 = {}".format(f1))
                        dp[i][0] = 1
                        dp[i][1] = 0
                        break

                    f2 = int(i / f1)
                    if f2 < i and dp[i - f2][1]:
                        print("f2 = {}".format(f2))
                        dp[i][0] = 1
                        dp[i][1] = 0
                        break
            print('\n')

        for x in dp:
            print(x)

        return bool(dp[N][0])


sol = Solution()
sol.divisorGame(5)