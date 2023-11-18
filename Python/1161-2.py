# Maximum Level Sum of a Binary Tree
# Medium

from collections import deque
from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: Optional[TreeNode]) -> int:

    maxsum = -10e10
    depth = maxdepth = 0
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        
        depth += 1
        val = sum([x.val for x in queue])
        if val > maxsum: 
            maxsum = val
            maxdepth = depth
        
        n = len(queue)
        while(n > 0):
            node = queue.popleft()
            if node.left:   queue.append(node.left)
            if node.right:  queue.append(node.right)
            n -= 1
    
    return maxdepth
        
maxLevelSum()