from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		idx =  self.find_min_idx(nums)
		print(idx)
		i1 = self.bs(nums, target, 0, idx)
		i2 = self.bs(nums, target, idx, len(nums) - 1)
		return max(i1, i2)

	def find_min_idx(self, nums: List[int]) -> int:
		left = 0
		right = len(nums) - 1

		if len(nums) == 1:
			return 0

		if nums[left] < nums[right]:
			return 0

		while left < right:
			mid = (left + right) // 2
			if nums[right] < nums[mid]:
				left = mid + 1
			else:
				right = mid
		return left

	def bs(self, nums: List[int], target: int, left: int, right: int) -> int:
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return -1


print([4, 5, 6, 7, 0, 1, 2])
print(Solution().search([8, 9, 0, 1, 2, 3, 4, 5, 6], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([1], 0))
print(Solution().search([1], 1))
print(Solution().search([1], 2))
print(Solution().search([1, 3], 2))
print(Solution().search([1, 3, 5], 3))
print(Solution().search([1,3], 3))