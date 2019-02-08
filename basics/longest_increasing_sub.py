class Solution:
    def LIS(self, A):
        lis = [0] * len(A)

        for i in range(len(A)):
            max_lis = 1
            for j in range(i):
                if A[j] < A[i]:
                    curr_lis = lis[j] + 1

                    if curr_lis > max_lis:
                        max_lis = curr_lis
            lis[i] = max_lis

        return lis

    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        if len(A) == 0:
            return 0
        # print(A)
        # print('\n')

        lis_array = self.LIS(A)
        # print(lis_array)
        # print('\n')

        lis_rev_array = self.LIS(A[::-1])[::-1]
        # print(lis_rev_array)
        # print('\n')

        max_len = 0
        for i in range(len(A)):
            curr_len = lis_array[i] + lis_rev_array[i] - 1
            if curr_len > max_len:
                max_len = curr_len
            # print(i, max_len)

        return max_len


sol = Solution()

# a = [1, 11, 2, 10, 4, 5, 2, 1]
# a = [1, 2]
a = [ 1, 1, 1, 1, 1]
print(sol.longestSubsequenceLength(a))