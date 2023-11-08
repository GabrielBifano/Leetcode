# Reverse Linked List
# Easy

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    curr = head
    newl = None

    while curr:
        next        = curr.next
        curr.next   = newl
        newl        = curr 
        curr        = next

    return newl