# Search in a Binary Search Tree
# Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(node: Optional[TreeNode]):
        
        if not node: return None
        if node.val == val:
            return node

        l = dfs(node.left )
        r = dfs(node.right)
        
        return l if l is not None else r
    
    return dfs(root)