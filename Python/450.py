# Delete Node in a BST
# Medium

# This still doesnt work

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
    def get_node(node, key, parent=None):
        if node == None: return None
        elif key < node.val: return get_node(node.left,  key, node)
        elif key > node.val: return get_node(node.right, key, node)
        else: return (node, parent)
        
    def del_node(node, parent) -> None:
        if parent is None:
            node = None
            return 
        if parent.left == node:
            if node.right is not None:
                parent.left = node.right
            else: parent.left = node.left
        else: 
            if node.right is not None:
                parent.right = node.right
            else: parent.right = node.left

    def del_twin_child_node(node) -> None:
        sparent = node
        succ = node.right
        while True:
            if succ.left is not None:
                sparent = succ
                succ = succ.left
            else: break
        del_node(succ, sparent)
        node.val = succ.val

    t = get_node(root, key)
    if t is None: return root
    
    remove_me, parent = t
    if   remove_me.left is None and remove_me.right is None:
        del_node(remove_me, parent)
    elif remove_me.left is not None and remove_me.right is not None:
        del_twin_child_node(remove_me)
    else:
        del_node(remove_me, parent)

    return root