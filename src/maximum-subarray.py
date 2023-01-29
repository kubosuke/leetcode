from typing import List


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		cur = 0
		ans = -1000000000
		for i in range(len(nums)):
			if cur < 0 and cur < nums[i]:
				cur = nums[i]
			else:
				cur += nums[i]
			ans = max(ans, cur)
		return ans


v = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(v)
print(Solution().maxSubArray(v))

v = [1]
print(v)
print(Solution().maxSubArray(v))

v = [5, 4, -1, 7, 8]
print(v)
print(Solution().maxSubArray(v))
