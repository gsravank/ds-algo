class Solution:
    def findLongestChain(self, pairs):  #List[List[int]]) -> int:
        if len(pairs) == 0:
            return 0

        pairs = sorted(pairs, key=lambda x: x[0])
        print(pairs)
        pairs = sorted(pairs, key=lambda x: x[1])
        print(pairs)

        max_len = 1
        prev_start = pairs[0][0]
        prev_end = pairs[0][1]
        for pair in pairs[1:]:
            curr_start = pair[0]
            curr_end = pair[1]

            if curr_start == prev_start:
                pass
            elif curr_start > prev_end:
                max_len += 1
                prev_start = curr_start
                prev_end = curr_end
            else:
                pass

        return max_len


p = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]

sol = Solution()
print(sol.findLongestChain(p))