# Maximum Level Sum of a Binary Tree
# Medium

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: Optional[TreeNode]) -> int:

    level_sum = {}

    def traverse(node: TreeNode, depth: int) -> None:
    
        if not node: return
        
        cumsum = level_sum.get(depth, 0)
        level_sum[depth] = cumsum + node.val

        traverse(node.right, depth + 1)
        traverse(node.left,  depth + 1)
    
    traverse(root, 1)
        
    return max(level_sum, key= lambda x: level_sum[x])