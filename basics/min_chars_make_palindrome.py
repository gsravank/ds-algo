class Solution:
    # @param A : string
    # @return an integer
    def compute_lps(self, A):
        lps = [0] * len(A)

        j = 0
        i = 1

        while i < len(A):
            if A[i] == A[j]:
                lps[i] = j+1
                i += 1
                j += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]

        return lps

    def solve(self, A):
        new_string = A.lower() + '#' + A[::-1].lower()
        # print(new_string)
        lps = self.compute_lps(new_string)
        # print(lps)
        num_chars_to_add = len(A) - lps[-1]

        return num_chars_to_add


sol = Solution()
# print(sol.compute_lps('ababababca'))
print(sol.solve('AACECAAAA'))