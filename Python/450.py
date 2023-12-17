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
        
    def get_node(node, key, parent=None) -> Optional[tuple]:
        if not node: return None
        elif key < node.val: get_node(node.left,  key, node)
        elif key > node.val: get_node(node.right, key, node)
        else: return (node, parent)
    
    def del_node(node, parent) -> None:
        if parent.left == node:
            if node.right is not None:
                parent.left = node.right
            else: parent.left = node.left
        else: 
            if node.right is not None:
                parent.right = node.right
            else: parent.right = node.left

    def del_twin_child_node(node) -> None:
        sparent = None
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
    remove_me.val = 100
    
    # elif remove_me.left is None and remove_me.right is None:
    #     del_node(remove_me, parent)
    # elif remove_me.left is not None and remove_me.right is not None:
    #     del_twin_child_node(remove_me)
    # else:
    #     del_node(remove_me, parent)

    return root











def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    self.actual_node_found = None
    
    def find_val(node, key):
        if node == None:
            return node

        if node.val == key:
            if node.right and node.left:
                self.actual_node_found = node
            if node.right:
                return node.right
            else:
                return node.left
            return None
        
        node.left = find_val(node.left, key)
        node.right = find_val(node.right, key)

        return node

    root = find_val(root, key)
    
    if self.actual_node_found is None or \
    self.actual_node_found.left is None:
        return root

    #now the problem becomes of attaching left subtree of found val to this right child of the found val

    #how to do this 

    right = self.actual_node_found.right
    left = self.actual_node_found.left

    while True:
        prev = right
        if right.val > left.val:
            right = right.left
        else:
            right = right.right

        if right == None:
            break
    
    if prev.val > left.val:
        prev.left = left
    else:
        prev.right = left

    return root
