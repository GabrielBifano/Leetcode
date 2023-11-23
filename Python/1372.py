# Longest ZigZag Path in a Binary Tree
# Medium

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(root: Optional[TreeNode]) -> int:
    def traverse(node: Optional[TreeNode], len, right:bool, maxlen):

        if not node:
            return maxlen

        if len > maxlen:
            maxlen = len
        
        if right: # grow right
            l= traverse(node.left,  1,       True,  maxlen)
            r= traverse(node.right, len + 1, False, maxlen)
            return max(l, r)
        else: # grow left
            l= traverse(node.left,  len + 1, True,  maxlen)
            r= traverse(node.right, 1,       False, maxlen)
            return max(l, r)

    return traverse(root, 0, False, 0)