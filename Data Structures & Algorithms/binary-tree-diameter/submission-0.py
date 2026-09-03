# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0
        def dfs(node):
            if not node:
                return 0
            
            self.max_path = max(self.max_path, dfs(node.right) + dfs(node.left))
            return 1 + max(dfs(node.right), dfs(node.left))
        
        dfs(root)
        return self.max_path

            
        