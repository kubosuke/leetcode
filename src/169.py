from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
            if d[n] > l // 2:
                return n


print(Solution().majorityElement([8, 9, 8, 9, 8]))
