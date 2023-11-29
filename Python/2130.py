# Maximum Twin Sum of a Linked List
# Medium

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head: Optional[ListNode]) -> int:

    l = []
    len = 0
    node = head
    while node:
        len += 1
        l.append(node.val)
        node = node.next
    
    for i in range(int(len/2)):
        l[i] += l[-i - 1]
    
    return max(l)