# Delete Node in a BST
# Medium

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
    def del_node(node: Optional[TreeNode], key):

        if not node: return None
        if node.val == key:
            return node.left

        if key < node.val:
            node.left = del_node(node.left, key)
        else:
            node.right = del_node(node.right, key)
        return node

    del_node(root, key)
    return root