# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_diff = 1
        self.flag = True 
        def dfs(node):
            if not node:
                return [True, 0]

            diff_value = abs(dfs(node.right)[1] - dfs(node.left)[1])
            if diff_value > max_diff:
                self.flag = False
                return [False, -1]
            
            if self.flag:
                return [True, max(dfs(node.right)[1], dfs(node.left)[1]) + 1]
            else:
                return [False, -1]


        answer = dfs(root)

        return answer[0]


        