from functools import cache
from typing import List


class Solution:
    nums = []

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self._rob(len(nums) - 1)

    @cache
    def _rob(self, i: int) -> int:
        if i == 0:
            return self.nums[0]
        if i == 1:
            return max(self.nums[0], self.nums[1])
        return max((self._rob(i - 2) + self.nums[i]), self._rob(i - 1))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
    nums = [
        104,
        209,
        137,
        52,
        158,
        67,
        213,
        86,
        141,
        110,
        151,
        127,
        238,
        147,
        169,
        138,
        240,
        185,
        246,
        225,
        147,
        203,
        83,
        83,
        131,
        227,
        54,
        78,
        165,
        180,
        214,
        151,
        111,
        161,
        233,
        147,
        124,
        143,
    ]
    print(Solution().rob(nums))
