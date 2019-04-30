# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        level_order = list()

        curr_level = [A]

        while len(curr_level):
            curr_level_items = [x.val for x in curr_level]
            level_order.append(curr_level_items)

            next_level = list()
            for x in curr_level:
                if x.left is not None:
                    next_level.append(x.left)
                if x.right is not None:
                    next_level.append(x.right)

            curr_level = next_level

        return level_order

nodes = list()

for i in range(1, 8):
    nodes.append(TreeNode(i))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]

nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]

nodes[4].right = nodes[6]

sol = Solution()
print(sol.levelOrder(nodes[0]))