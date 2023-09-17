# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ListNode()
        h = ptr
        s = 0
        c = 0
        
        while l1 or l2 or c:
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
                
            s += c
            p = s % 10
            c = s // 10
            
            nwnode = ListNode(p)
            ptr.next = nwnode
            ptr = ptr.next
            
            s = 0  
        
        return h.next
