# Count Good Nodes in Binary Tree
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int: # TODO may underestimate by one the counter
    
    def traverse(root: TreeNode, maxNode: int) -> int:
        
        bigger = maxNode <= root.val
        noleft  = root.left  == None
        noright = root.right == None

        if noleft and noright:
            return 1 if bigger else 0
        
        else:
            left  = 0
            right = 0
            if not noleft:  left  = traverse(root.left, root.val if bigger else maxNode)
            if not noright: right = traverse(root.right, root.val if bigger else maxNode)
            
            return left + right + 1 * (bigger)
    
    return traverse(root=root, maxNode=root.val)