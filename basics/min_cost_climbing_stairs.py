class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp = [0] * (len(cost) + 1)
        if len(cost) <= 1:
            return 0

        dp0 = 0
        dp1 = 0
        for i in range(2, len(cost) + 1, 1):
            new = min(cost[i - 2] + dp0, cost[i - 1] + dp1)
            dp0 = dp1
            dp1 = new
            # dp[i] = min(cost[i - 2] + dp[i - 2], cost[i - 1] + dp[i - 1])

        return dp1

sol = Solution()
print(sol.minCostClimbingStairs([10]))