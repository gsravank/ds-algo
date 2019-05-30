"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


class Solution:
    def find_end_idx(self, s, start_idx):
        count = 0
        curr_idx = start_idx
        while True:
            if s[curr_idx] == '[':
                count += 1
                curr_idx += 1
            elif s[curr_idx] == ']':
                count -= 1
                if count == 0:
                    return curr_idx
                curr_idx += 1
            else:
                curr_idx += 1

    def helper(self, s, start_idx, end_idx, char_list):
        curr_idx = start_idx
        while curr_idx <= end_idx:
            if s[curr_idx].isnumeric():
                rep = int(s[curr_idx])
                curr_char_list = list()
                self.helper(s, curr_idx + 2, self.find_end_idx(s, curr_idx + 1) - 1, curr_char_list)
                char_list.extend(curr_char_list * rep)
            else:
                char_list.append(s[curr_idx])
                curr_idx += 1
        return char_list

    def decodeString(self, s: str) -> str:
        char_list = list()
        self.helper(s, 0, len(s) - 1, char_list)

        return ''.join(char_list)


sol = Solution()