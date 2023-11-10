# Maximum Depth of Binary Tree
# Easy

from collections import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1