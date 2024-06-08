class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        if head.next.next is None:
            return head
        
        first_odd = head
        first_even = head.next

        last_even = None
        while True:
            print(head.val)
            if last_even is not None:
                last_even.next = head.next
            last_even = head.next

            if head.next is None:
                head.next = first_even
                break
            if head.next.next is None:
                last_even.next = None
                head.next = first_even
                break

            head.next = head.next.next
            head = head.next

        return first_odd