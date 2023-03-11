from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], gt: int = -2 << 32, lt: int = 2 << 32) -> bool:
        if root is None:
            return True
        left, right = root.left, root.right
        if left is not None:
            if left.val >= root.val or not gt < left.val < lt:
                return False
        if right is not None:
            if right.val <= root.val or not gt < right.val < lt:
                return False
        return self.isValidBST(left, gt, root.val) and self.isValidBST(right, root.val, lt)
