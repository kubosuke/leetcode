from collections import deque
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cs = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            cs[i + 1] = cs[i] + nums[i]
        ans = len(nums)
        for i in range(1, len(nums)):
            if cs[i + 1] < target:
                continue
            l = 0
            r = i
            while r - l > 1:
                m = (r + l) // 2
                if cs[i] - cs[m] < target:
                    r = m
                else:
                    l = m
            if cs[i] - cs[l] >= target:
                ans = min(ans, i - l - 1)
        return 0 if ans == len(nums) and cs[-1] < target else ans

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cs = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            cs[i + 1] = cs[i] + nums[i]
        l = 0
        r = 0
        ans = len(nums)
        while True:
            if cs[r] - cs[l] >= target:
                while cs[r] - cs[l + 1] >= target:
                    l += 1
            if cs[r] - cs[l] >= target:
                ans = min(ans, r - l)
            if r == len(nums):
                break
            r += 1
        return 0 if ans == len(nums) and cs[r] - cs[l] < target else ans

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        dq = deque()
        ans = len(nums)
        for n in nums:
            dq.append(n)
            while True:
                if sum(dq) - dq[0] >= target:
                    dq.popleft()
                else:
                    break
            if sum(dq) >= target:
                ans = min(ans, len(dq))
        return 0 if ans == len(nums) and sum(dq) < target else ans


# print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(4, [1, 4, 4]))
# print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
# print(Solution().minSubArrayLen(15, [1, 2, 3, 4, 5]))
