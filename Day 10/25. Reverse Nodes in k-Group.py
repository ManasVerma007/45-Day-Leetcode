class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_group(head, k):
            prev = None
            curr = head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, head

        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1

        if count == k:
            new_head, new_tail = reverse_group(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return new_head

        return head
