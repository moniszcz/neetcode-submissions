# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #solution 1
        # def dfs(node):
        #     stack = [[node, 1]]

        #     max_len = 1
        #     while stack:
        #         curr_node, _len = stack.pop(-1)
        #         if not curr_node.right and not curr_node.left:
        #             max_len = max(max_len, _len)
        #         if curr_node.right:
        #             stack.append([curr_node.right, _len + 1])
        #         if curr_node.left:
        #             stack.append([curr_node.left, _len + 1])
            
        #     return max_len
        
        # if not root:
        #     return 0

        # return dfs(root)

        #solution 2:
        # def dfs(node):
        #     if not node:
        #         return 0
        #     return 1 + max(dfs(node.right), dfs(node.left))

        # return dfs(root)


        #solution 3:

        def bfs(node):
            _len = 1
            queue = [[node, _len]]

            while queue:
                curr_node, _len = queue.pop(0)
                print(curr_node.val, _len)

                if curr_node.left:
                    queue.append([curr_node.left, _len + 1])
                if curr_node.right:
                    queue.append([curr_node.right, _len + 1])

            
            return _len
            
        if not root:
            return 0
            
        return bfs(root)

        