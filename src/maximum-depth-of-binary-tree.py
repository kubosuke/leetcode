# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        dq = deque()
        ans = 1
        dq.append((root, 1))
        while dq:
            v, l = dq.popleft()
            if (left := v.left) is not None:
                ans = max(ans, l + 1)
                dq.append((left, l+1))
            if (right := v.right) is not None:
                ans = max(ans, l + 1)
                dq.append((right, l + 1))
        return ans
