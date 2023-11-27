# Odd Even Linked List
# Medium

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head or not head.next: return head

    oddhead = head
    bp = evenhead = head.next

    turn = 3
    node = evenhead.next
    while node:
        if turn % 2 != 0:
            oddhead.next = node
            oddhead = node
        else:
            evenhead.next = node
            evenhead = node
        node = node.next
        turn += 1

    oddhead.next = bp
    evenhead.next = None
    return head