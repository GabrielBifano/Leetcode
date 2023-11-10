# Leaf-Similar Trees
# 

from collections import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def runner(root: Optional[TreeNode], arr: 'list[int]'):
        if not root: return
        if not root.left and not root.right:
            arr.append(root.val)
        else:
            runner(root.left, arr)
            runner(root.right, arr)
    arr1 = []
    arr2 = []
    runner(root1, arr1)
    runner(root2, arr2)
    return arr1 == arr2