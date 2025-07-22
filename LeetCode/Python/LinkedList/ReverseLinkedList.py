def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        nextN = current.next
        current.next = prev
        prev = current
        current = nextN

    return prev
pri