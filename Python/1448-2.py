# Count Good Nodes in Binary Tree
# Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    
    def traverse(node: TreeNode, maxNode: int) -> int:
        
        if not node: return 0
        elif node.val >= maxNode:
            return 1 + traverse(node.left, node.val) + traverse(node.right, node.val)
        else:
            return traverse(node.left, maxNode) + traverse(node.right, maxNode)
    
    return traverse(node=root, maxNode=root.val)