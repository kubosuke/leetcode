from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = 0
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                cur += 1
            else:
                ans = max(cur, ans)
                cur = 0
        return max(cur, ans) + 1


# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(Solution().longestConsecutive([1, 2, 0, 1]))
