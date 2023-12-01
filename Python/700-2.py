# Search in a Binary Search Tree
# Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
    if not root: return None
    if root.val == val:
        return root

    l = searchBST(root.left,  val)
    r = searchBST(root.right, val)
    
    return l if l is not None else r
    
    