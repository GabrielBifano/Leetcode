from typing import Optional

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def flip(old, new):
    
    if new == None:
        return old

    if new.next == None:
        new.next = old
        return new

    old_right = new.next
    new.next = old
    return flip(new, old_right)


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    if head == None: return None
    new_head = flip(head, head.next)
    head.next = None
    return new_head