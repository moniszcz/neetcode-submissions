# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        
        output = ListNode()
        dummy = output

        while l1 or l2:
            if l1 and l2:
                if l1.val >= l2.val:
                    output.next = l2
                    l2 = l2.next
                else:
                    output.next = l1
                    l1 = l1.next
            elif l1 and not l2:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
        
        return dummy.next
        