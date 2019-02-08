"""
Dr. Dhruv is a superb professor of Mathematics. He is so lenient that he doesn’t even take attendance. But his students are not so cooperative.
Frustrating of all aspects is that students have stopped attending classes of Dr. Dhruv. Dr. Dhruv is really disappointed and he has decided to start taking attendance. There are A students in his class. Ordinary professors take a roll call as [1, 2, 3, …, A] but Dr. Dhruv is no ordinary man. He has come up with a different method of taking roll call. His method is as follows:

He has a list B of K random integers which means that he will call out only K students. He will first treat the numbers [1, 2, 3, .., A] as strings
[“1”, “2”, “3”, .., “A”]. Then he will sort this vector of strings in lexicographic order (see example below). Now, Dr. Dhruv will call the numbers
which are at B[i]-th (0 <= i < K) position in the sorted order (see example below).

Simply putting, if the sorted order is S, then he will call students in the order { S[B[0] - 1], S[B[1] - 1], …, S[B[K-1] - 1] }. You need to output the numbers in the sequence that Dr. Dhruv will call.

Note: Dr. Dhruv needs this task to finish quickly and hence expected time complexity O(K*log(A))
"""

class Solution:
    def get_biggest_ones(self, n):
        prev_biggest_ones = 1
        curr_biggest_ones = 11

        while curr_biggest_ones <= n:
            prev_biggest_ones = curr_biggest_ones
            curr_biggest_ones = ((curr_biggest_ones * 10) + 1)

        return prev_biggest_ones

    def get_kth_number(self, k, A):
        biggest_ones = self.get_biggest_ones(A)
        digits = list()

        first = 1

        print('A = {}, k = {}, biggest_ones={}\n\n'.format(A, k, biggest_ones))
        while k != 0:
            print('k={}'.format(k))
            quotient = int(k/biggest_ones)
            print('quotient = {}'.format(quotient))

            remainder = k % biggest_ones
            # if remainder == 0:
            #     remainder = biggest_ones

            print('remainder = {}'.format(remainder))

            if first:
                if remainder == 0:
                    digit = quotient
                else:
                    digit = quotient + 1
            else:
                if remainder == 0:
                    digit = quotient - 1
                else:
                    digit = quotient
            digits.append(digit)
            print('digit added = {}'.format(digit))

            if quotient == 0:
                remainder -= 1

            first = 0
            k = remainder
            print('new k = {}'.format(k))
            biggest_ones = int(biggest_ones / 10)
            print('new biggest_ones = {}'.format(biggest_ones))
            print('\n\n')

        final_number = 0
        for idx, digit in enumerate(digits):
            final_number += (digit * (10 ** (len(digits) - idx - 1)))

        return final_number

    def solve(self, A, B):
        final_list = list()
        for b in B:
            final_list.append(self.get_kth_number(b, A))

        return final_list



sol = Solution()
# print(sol.get_biggest_ones(2000))
print(sol.solve(999, [112]))