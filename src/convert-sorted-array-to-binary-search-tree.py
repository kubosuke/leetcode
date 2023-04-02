# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        im = len(nums) // 2
        return TreeNode(nums[im], self.sortedArrayToBST(nums[:im]), self.sortedArrayToBST(nums[im+1:]))
    
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))