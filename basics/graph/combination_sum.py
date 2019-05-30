class Solution:
    def helper(self, candidates, l, n, target, curr_sum, curr_comb, all_comb):
        if curr_sum == target:
            all_comb.append(curr_comb[:])

        if l == n:
            return

        if candidates[l] > (target - curr_sum):
            return

        curr_cand = candidates[l]
        total_mult = int(target / curr_cand)
        for num_times in range(total_mult + 1):
            self.helper(candidates, l + 1, n,
                        target, curr_sum + (num_times * curr_cand),
                        curr_comb, all_comb)
            curr_comb.append(curr_cand)

        for _ in range(total_mult + 1):
            curr_comb.pop()

        return

    def combinationSum(self, candidates, target):# List[int], target: int) -> List[List[int]]:
        curr_comb = list()
        all_comb = list()

        candidates = sorted(candidates)
        n = len(candidates)

        self.helper(candidates, 0, n, target, 0, curr_comb, all_comb)
        return all_comb


c = [2,3,5]
t = 8

sol = Solution()
print(sol.combinationSum(c, t))