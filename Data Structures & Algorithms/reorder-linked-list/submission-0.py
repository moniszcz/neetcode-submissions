# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []
        node = head 
        while node:
            temp.append(node)
            node = node.next
        
        left = 1
        right = len(temp) - 1
        output = temp[0]
        while left < right:
            output.next = temp[right]
            output = output.next
            right -= 1
            output.next = temp[left]
            output = output.next            
            left += 1
            
        if left == right:        # even length: attach the remaining middle node
            output.next = temp[left]
            output = output.next
        output.next = None


        