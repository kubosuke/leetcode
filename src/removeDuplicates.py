from functools import cache
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


print(Solution().removeDuplicates([0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5]))
