# Definition for a binary tree node.
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        l = self.hasPathSum(root.left, targetSum-root.val) if root.left else False
        r = self.hasPathSum(root.right, targetSum-root.val) if root.right else False
        return l or r
