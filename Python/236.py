# Lowest Common Ancestor of a Binary Tree
# Medium

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    def DFS(node: 'TreeNode', target: 'TreeNode', stack: list):
        
        if not node: return None
        if node == target: return stack + [node]
        
        left  = DFS(node.left,  target, stack + [node])
        right = DFS(node.right, target, stack + [node])
        
        if left is not None: return left
        else: return right

    pstack = DFS(root, p, [])
    qstack = DFS(root, q, [])

    ancestor = 0
    for i in range(min(len(pstack), len(qstack))):
        if pstack[i] == qstack[i]:
            ancestor = pstack[i]

    return ancestor