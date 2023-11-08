# Reverse Linked List
# Easy

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def change_values(head, cum: 'list[int]'):
    
    cum.append(head.val)
    if head.next == None:
        head.val = cum[0]
        return (head, 1)
    else:
        _, i = change_values(head.next, cum)
        head.val = cum[i]
        return (head, i + 1)

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    if head == None: return None
    else: 
        h, _ = change_values(head, [])
        return h