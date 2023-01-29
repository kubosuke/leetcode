from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		ans = []
		def perms(cur: List[int], used: dict):
			if len(cur) == len(nums):
				ans.append(cur.copy())
				return
			for num in nums:
				if not used.get(num):
					used[num] = True
					cur.append(num)
					perms(cur, used)
					used[num] = False
					cur.pop()
		perms([], {})
		return ans


print(Solution().permute([2, 3, 5]))
