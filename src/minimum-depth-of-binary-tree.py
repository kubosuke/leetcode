# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append((root, 0))

        ans = 1000000
        while dq:
            v, d = dq.popleft()
            if v.left:
                dq.append((v.left, d + 1))     
            if v.right:
                dq.append((v.right, d + 1))
            if not v.left and not v.right:
                ans = min(ans, d+1)
        return ans