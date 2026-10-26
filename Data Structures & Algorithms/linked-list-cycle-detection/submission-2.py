# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = {}
        node = head
        while node:
            if not node.next:
                return False
            if node.val in visited_nodes and visited_nodes[node.val] == node.next.val:
                return True
            visited_nodes[node.val] = node.next.val
            node = node.next

        return False
        