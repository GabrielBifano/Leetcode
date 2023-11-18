# Binary Tree Right Side View
# Medium

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> 'list[int]':

    side_view = []
    def traverse(node: TreeNode, depth: int) -> None:
        
        if not node: return
        
        if depth == len(side_view):
            side_view.append(node.val)
        
        traverse(node.right, depth + 1)
        traverse(node.left,  depth + 1)
    
    traverse(root, 0)
    return side_view
