class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        start = 0
        end = len(A) - 1

        while start <= end:
            print(start, end)
            print('Comparing "{}" and "{}"'.format(A[start], A[end]))
            print('\n')
            if A[start].isalnum() and A[end].isalnum():
                if A[start].lower() != A[end].lower():
                    return 0
                else:
                    start += 1
                    end -= 1
            else:
                if not A[start].isalnum():
                    start += 1
                if not A[end].isalnum():
                    end -= 1

        return 1


sol = Solution()
print(sol.isPalindrome('A man, a plan, a canal: Panama'))