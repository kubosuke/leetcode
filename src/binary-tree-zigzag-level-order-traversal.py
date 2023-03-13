# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dq = deque()
        ans = []
        dq.append((root, 0))

        cur_level = -1
        tmp = [root.val]
        while dq:
            v, level = dq.popleft()
            if level > cur_level:
                tmp.reverse() if level % 2 == 1 else ()
                ans.append(tmp)
                tmp = []
                cur_level = level
            if (left := v.left) is not None:
                tmp.append(left.val)
                dq.append((left, level + 1))
            if (right := v.right) is not None:
                tmp.append(right.val)
                dq.append((right, level + 1))
        return ans
