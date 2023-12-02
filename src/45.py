from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = nums[0]
        cnt = 0
        for i in range(len(nums)):
            if cur == 0:
                break
            cur -= 1
            if cur < nums[i]:
                cur = nums[i]
                cnt += 1
            if cur == len(nums) - 1:
                break
        return max(cnt - 1, 0)


print(Solution().jump([2, 3, 1, 1, 4]))
