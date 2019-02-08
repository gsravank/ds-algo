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
    def num_digits(self, n):
        num_dig = 0
        while n > 0:
            num_dig += 1
            n = int(n / 10)

        return num_dig

    def kth_digit_from_right(self, n, k):
        all_digits = list()

        while n > 0:
            all_digits.append(n % 10)
            n = int (n / 10)

        # all_digits = all_digits[::-1]
        return all_digits[k-1]

    def get_n_ones(self, n):
        final = 0
        for i in range(n):
            final += (10 ** i)

        return final

    def get_num_nums(self, A, num_digits_A):
        num_of_nums = [0] * 10
        first_digit_A = self.kth_digit_from_right(A, num_digits_A)
        print(A, num_digits_A)
        print(first_digit_A)

        id = -1
        for idx in range(len(num_of_nums)):
            if idx == 0 and (self.num_digits(A) == num_digits_A):
                pass
            elif idx + 1 < first_digit_A:
                num_of_nums[idx] = self.get_n_ones(num_digits_A)
            elif idx + 1 == first_digit_A:
                id = idx
                num_of_nums[idx] = self.get_n_ones(num_digits_A - 1)
            else:
                num_of_nums[idx] = self.get_n_ones(num_digits_A - 1)

        print(num_of_nums)
        if id > -1:
            num_of_nums[id] += (A + 1 - (first_digit_A * (10 ** (num_digits_A - 1))))
        else:
            num_of_nums[0] += ()
        # print(num_of_nums)

        return num_of_nums

    def find_kth_num(self, k, A, digs):
        # print(k, A, digs)
        print('\n\nStart of find-kth-num call..')
        print(k, A, digs)
        print(self.num_digits(A) - len(digs))
        num_of_nums = self.get_num_nums(A, self.num_digits(A) - len(digs))
        print(num_of_nums)

        sum_till_idx = [0] * len(num_of_nums)
        curr_sum = 0
        for idx, num_of_num in enumerate(num_of_nums):
            curr_sum += num_of_num
            sum_till_idx[idx] = curr_sum
        print(sum_till_idx)

        for idx, num_of_num in enumerate(num_of_nums):
            if sum_till_idx[idx] >= k:
                print(idx)
                digs.append(idx - 1)
                print(digs)

                # Remaining to find recursively in the tree
                if idx == 0:
                    remaining_sum = k
                else:
                    remaining_sum = (k - sum_till_idx[idx - 1])

                print(remaining_sum)

                self.find_kth_num(remaining_sum, A, digs)
                break

        return digs

    def solve(self, A, B):
        final_list = list()
        for k in B:
            digits = list()
            final_digits = self.find_kth_num(k, A, digits)
            num_of_digits = len(final_digits)
            kth_num = 0

            for idx, digit in enumerate(final_digits):
                kth_num += (digit * (10 ** (num_of_digits - 1 - idx)))
            final_list.append(kth_num)

        return final_list


s = Solution()
print(s.solve(3000, [1112]))