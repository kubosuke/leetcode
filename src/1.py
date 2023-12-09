from itertools import combinations
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]
