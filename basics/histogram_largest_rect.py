class Solution:
    def get_max_widths(self, heights):
        max_widths = [1 for _ in range(len(heights))]

        stack = list()
        max_area = 0

        for idx, hi in enumerate(heights):
            if len(stack) == 0:
                stack.append((hi, idx))
            else:
                temp_idx = stack[-1][1]

                while len(stack) and stack[-1][0] > hi:
                    top = stack.pop()

                    top_hi = top[0]
                    top_idx = top[1]

                    max_widths[top_idx] = (temp_idx - top_idx + 1)
                    # max_area = max(max_area, top_hi * (temp_idx - top_idx + 1))

                stack.append((hi, idx))

        if len(stack):
            temp_idx = stack[-1][1]

        while len(stack):
            top = stack.pop()

            top_hi = top[0]
            top_idx = top[1]

            # print(temp_idx, top_hi, top_idx, top_hi * (temp_idx - top_idx + 1))
            max_widths[top_idx] = (temp_idx - top_idx + 1)
            # max_area = max(max_area, top_hi * (temp_idx - top_idx + 1))

        return max_widths


    def largestRectangleArea(self, heights):# List[int]) -> int:
        # stack = list()
        # max_area = 0
        #
        # for idx, hi in enumerate(heights):
        #     # print(max_area)
        #     if len(stack) == 0:
        #         stack.append((hi, idx))
        #     else:
        #         temp_idx = stack[-1][1]
        #
        #         while len(stack) and stack[-1][0] > hi:
        #             top = stack.pop()
        #
        #             top_hi = top[0]
        #             top_idx = top[1]
        #
        #             # print(temp_idx, top_hi, top_idx, top_hi * (temp_idx - top_idx + 1))
        #             max_area = max(max_area, top_hi * (temp_idx - top_idx + 1))
        #
        #         stack.append((hi, idx))
        #
        # if len(stack):
        #     temp_idx = stack[-1][1]
        #
        # while len(stack):
        #     top = stack.pop()
        #
        #     top_hi = top[0]
        #     top_idx = top[1]
        #
        #     # print(temp_idx, top_hi, top_idx, top_hi * (temp_idx - top_idx + 1))
        #     max_area = max(max_area, top_hi * (temp_idx - top_idx + 1))
        # print(heights)
        max_right_widths = self.get_max_widths(heights)
        max_left_widths = self.get_max_widths(heights[::-1])[::-1]
        # print(max_right_widths)
        # print(max_left_widths)

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, (max_left_widths[i] + max_right_widths[i] - 1) * heights[i])

        return max_area


heights = [2, 1, 5, 6, 2, 3]
sol = Solution()
print(sol.largestRectangleArea(heights))