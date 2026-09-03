# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            stack = [[node, 1]]

            max_len = 1
            while stack:
                curr_node, _len = stack.pop(-1)
                if not curr_node.right and not curr_node.left:
                    max_len = max(max_len, _len)
                if curr_node.right:
                    stack.append([curr_node.right, _len + 1])
                if curr_node.left:
                    stack.append([curr_node.left, _len + 1])
            
            return max_len
        
        if not root:
            return 0

        return dfs(root)

        