class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer

    def power(self, x, y):
        print(y)
        if (y == 0): return 1
        temp = self.power(x, int(y / 2))

        if (y % 2 == 0):
            return temp * temp
        else:
            if (y > 0):
                return x * temp * temp
            else:
                return (temp * temp) / x

    def pow(self, x, n, d):
        return self.power(x, n) % d



sol = Solution()
print(sol.pow(71045970, 41535484, 64735492))