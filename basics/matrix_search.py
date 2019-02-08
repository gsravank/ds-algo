class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def get_row(self, A, B):
        low = 0
        high = len(A) - 1
        result = -1

        # print(low, high, result)
        # input('Hey..')

        while low <= high:
            mid = int((low + high) / 2)
            # print(low, mid, high)
            # input('Hey..')

            if A[mid][0] == B:
                return mid
            elif A[mid][0] > B:
                high = mid - 1
            else:
                result = mid
                low = mid + 1

        return result

    def binary_search(self, items, elem):
        low = 0
        high = len(items) - 1

        while low <= high:
            mid = int((low + high) / 2)

            if items[mid] == elem:
                return True
            elif items[mid] < elem:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix(self, A, B):
        print('Given matrix: ')
        print(A)
        print('\n\n')

        row_number = self.get_row(A, B)

        print('\nFound correct row..\n')
        print('Row number: {}'.format(row_number))
        row = A[row_number]
        print('Row: {}'.format(row))
        print('\nFinding if number is in that row..\n')
        return self.binary_search(row, B)

sol = Solution()
a = sol.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50],
  [53, 58, 59, 60]
], 20)
print(a)