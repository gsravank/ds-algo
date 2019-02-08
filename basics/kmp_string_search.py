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

    def search(self, text, pattern):
        lps = self.compute_lps(pattern)
        i = 0 # text pointer
        j = 0 # pattern pointer

        indices = list()

        while i < len(text):
            print(i, j)
            if pattern[j] == text[i]:
                i += 1
                j += 1

                if j == len(pattern):
                    indices.append(i - len(pattern))
                    j = lps[j-1]
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

        return indices


sol = Solution()
# print(sol.compute_lps('abcdabcy'))
# print(sol.search('abcdabcxabxabcdabcdabcyabcdabcy', 'abcdabcy'))

print(sol.compute_lps('abcdabcd'))
print(sol.search('abcdabcxabxabcdabcdabcdabcyabcy', 'abcdabcd'))