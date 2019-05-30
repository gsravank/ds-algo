"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


class Solution:
    def dailyTemperatures(self, T): #List[int]) -> List[int]:
        stack = list()
        wait_days = [0 for _ in range(len(T))]

        for idx, ti in enumerate(T):
            if len(stack) == 0:
                stack.append((idx, ti))
            else:
                while len(stack) and stack[-1][1] < ti:
                    top = stack.pop()
                    wait_days[top[0]] = idx - top[0]

                stack.append((idx, ti))

        return wait_days

T =  [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.dailyTemperatures(T))