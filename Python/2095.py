# Delete the Middle Node of a Linked List
# Medium

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head or not head.next: return None

    length = idx = 1
    node = middle = head
    while node:
        node = node.next
        length += 1

        if length / 2 > idx:
            middle = middle.next
            idx += 1
    
    node = head
    while node.next != middle:
        node = node.next

    node.next = middle.next
    return head