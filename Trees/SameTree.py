from typing import Optional

# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # If both p and q are emtpy return True
            return True
        
        if not p or not q or p.val != q.val:    # If p is empty or q is empty or p value is not equal to the q value return False
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))  # Recusively check for the values