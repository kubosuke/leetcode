from typing import List


class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		ans = []

		def backtrace(i: int, cur: List[int]):
			print(cur)
			if sum(cur) == target:
				ans.append(cur.copy())
				return
			elif sum(cur) > target or i >= len(candidates):
				return
			cur.append(candidates[i])
			backtrace(i, cur)
			cur.pop()
			backtrace(i + 1, cur)

		backtrace(0, [])
		return ans


print(Solution().combinationSum([2, 3, 5], 8))
