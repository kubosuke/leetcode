from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue
            if nums[i - 1] != s:
                ans.append(f"{s}->{nums[i-1]}")
            else:
                ans.append(str(s))
            s = nums[i]
        if nums[-1] > s:
            ans.append(f"{s}->{nums[-1]}")
        else:
            ans.append(str(s))
        return ans
