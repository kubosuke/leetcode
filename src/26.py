from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        i = 1
        d = defaultdict(lambda: False)
        while True:
            if i >= len(nums):
                break
            if prev == nums[i]:
                if not d[prev]:
                    d[prev] = True
                    i += 1
                else:
                    nums.pop(i)
            else:
                prev = nums[i]
                i += 1
        return len(nums)


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
