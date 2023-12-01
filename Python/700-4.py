# Search in a Binary Search Tree
# Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    stack = [root]
    while len(stack) > 0:

        node = stack.pop()
        if not node: break
        if node.val == val: return node 
        
        if val < node.val: stack.append(node.left )
        else: stack.append(node.right)      

    return None   


    