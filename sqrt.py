class Solution:
    # @param A : integer
    # @return an integer
    def integers(self, idx):
        return idx + 1

    def sqrt(self, A):
        if A == 0:
            return 0

        # integers = list(range(1, A + 1, 1))
        # print(integers)

        low = 0
        high = A
        result = -1

        while low <= high:
            mid = int((low + high) / 2)
            # print(low, mid, high)

            if self.integers(mid) ** 2 == A:
                return self.integers(mid)
            elif self.integers(mid) ** 2 > A:
                high = mid - 1
            else:
                result = mid
                low = mid + 1

        return self.integers(result)


sol = Solution()
print(sol.sqrt(9))