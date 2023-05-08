from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        while r - l > 1:
            mid = (r + l) // 2
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
        return nums[0] if r == len(nums) else nums[r]


v = [3, 4, 5, 1, 2]
res = Solution().findMin(v)
print(res)

v = [4, 5, 6, 7, 0, 1, 2]
res = Solution().findMin(v)
print(res)

v = [11, 13, 15, 17]
res = Solution().findMin(v)
print(res)
