class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        # print(A)
        # print('\n')
        if len(A) <= 1:
            return len(A)

        from collections import defaultdict
        l = list()
        for _ in range(len(A)):
            l.append(defaultdict(lambda : 1))

        possible_diffs = dict()
        for i in range(1, len(A), 1):
            possible_diffs[i] = list()
            for j in range(0, i, 1):
                possible_diffs[i].append(A[i] - A[j])
        # print(possible_diffs)

        nearest_diff_elem = dict()
        for i in range(1, len(A), 1):
            nearest_diff_elem[i] = dict()
            for j in range(i-1, -1, -1):
                curr_diff = A[i] - A[j]
                if curr_diff not in nearest_diff_elem[i]:
                    nearest_diff_elem[i][curr_diff] = j

        uber_max = 1
        for i in range(1, len(A), 1):
            for diff in possible_diffs[i]:
                max_len = 1
                if diff in nearest_diff_elem[i]:
                    k = nearest_diff_elem[i][diff]
                    curr_len = l[k][diff] + 1

                    if curr_len > max_len:
                        max_len = curr_len

                l[i][diff] = max_len

                if max_len > uber_max:
                    uber_max = max_len

        # print(l)

        return uber_max


sol = Solution()
a = [9, 4, 7, 2, 10]
# a = [3, 6, 9, 12, 15, 19, 18, 21]
# a = [8, 5, 2, -1]
a = [2, 4, 5, 3, 8]
# a = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
print(sol.solve(a))


