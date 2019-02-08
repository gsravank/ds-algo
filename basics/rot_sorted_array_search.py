class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def find_pivot(self, A):
        n = len(A)
        low = 0
        high = len(A) - 1

        while low <= high:
            mid = int((low + high) / 2)
            next = (mid + 1) % n
            prev = (mid - 1) % n
            if A[low] <= A[high]:
                return low
            elif A[mid] <= A[next] and A[mid] <= A[prev]:
                return mid
            elif A[mid] <= A[high]:
                high = mid - 1
            else:
                low = mid + 1

    def modified_binary(self, A, pivot, elem):
        n = len(A)
        low = pivot
        high = (pivot - 1) % n

        found = 1
        if low < high:
            found = 0

        while found or (low <= high):
            dist = (high - low) % n
            mid = (low + int(dist / 2)) % n
            # mid = int((low + high) / 2) % n
            print('low: {}, dist: {}, mid: {}, high: {}, found: {}'.format(low, dist, mid, high, found))
            if A[mid] == elem:
                return mid
            elif A[mid] < elem:
                low = (mid + 1) % n
            else:
                high = (mid - 1) % n

            if low <= high:
                found = 0

        return -1

    def search(self, A, B):
        pivot = self.find_pivot(A)
        print(pivot)
        return self.modified_binary(A, pivot, B)

# [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
s = Solution()
a = s.search([204, 205, 206, 2,3,4,5, 10 , 100 , 202], 206)
print(a)