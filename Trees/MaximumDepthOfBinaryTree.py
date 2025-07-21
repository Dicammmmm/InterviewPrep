from collections import deque
from logging import _Level
from typing import Optional

# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(node, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return result

class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        
        return level
