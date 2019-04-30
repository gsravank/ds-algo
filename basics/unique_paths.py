from pprint import pprint

class Solution:
    def get_comb(self, n, r, dp):
        if r == 0:
            dp[n][r] = 1
        elif n == r:
            dp[n][r] = 1
        elif n < r:
            dp[n][r] = 0
        else:
            if not dp[n][r]:
                dp[n][r] = self.get_comb(n - 1, r - 1, dp) + self.get_comb(n - 1, r, dp)

        return dp[n][r]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n + 1)] for _ in range(m + n + 1)]
        a = self.get_comb(m+n, n, dp)

        for x in dp:
            pprint(x)

        return a

sol = Solution()
sol.uniquePaths(5, 5)