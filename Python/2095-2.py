# Delete the Middle Node of a Linked List
# Medium

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head or not head.next: return None

    length = idx = 0
    node = head
    while node:
        node = node.next
        length += 1
        idx = int(length / 2)

    node = head
    for i in range(idx):
        node = node.next        
        if i == idx - 1:
            node.next = node.next.next
            
    return head