# Path Sum III
# Medium

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    
    stack = []

    def checksum():
        cumsum = 0
        check = 0
        for element in reversed(stack):
            cumsum += element
            if cumsum == targetSum: check += 1
        return check

    def traverse(node: Optional[TreeNode]) -> int:

        if not node:
            return 0

        stack.append(node.val)
        check = checksum()
        result =  check + traverse(node.left) + traverse(node.right)
        
        stack.pop()
        return result
    
    return traverse(root)

n8 = TreeNode(val=1,left=None, right=None)
n7 = TreeNode(val=-2,left=None, right=None)
n6 = TreeNode(val=3,left=None, right=None)
n5 = TreeNode(val=11,left=None, right=None)
n4 = TreeNode(val=2,left=None, right=n8)
n3 = TreeNode(val=3,left=n6, right=n7)
n2 = TreeNode(val=-3,left=None, right=n5)
n1 = TreeNode(val=5,left=n3, right=n4)
root = TreeNode(val=10,left=n1, right=n2)

pathSum(root, 8)