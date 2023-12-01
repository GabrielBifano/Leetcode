# Search in a Binary Search Tree
# Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The quickest
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    if root != None:    
        if root.val == val: return root
        if val < root.val:
            return searchBST(root.left,  val)
        else:
            return searchBST(root.right, val)

    return None



    