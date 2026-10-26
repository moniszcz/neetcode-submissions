# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return True
            visited_nodes.add(node)
            node = node.next

        return False
        