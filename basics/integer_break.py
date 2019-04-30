class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(2, n + 1):
            dp[i][i] = 1

        for i in range(2, n + 1):
            dp[i][1] = i

        for i in range(3, n + 1):
            for j in range(2, i):
                for k in range(1, i):
                    dp[i][j] = max(dp[i][j], k * dp[i - k][j - 1])

        for x in dp:
            print(x)

        return max(dp[n][2:])

sol = Solution()
print(sol.integerBreak(10))