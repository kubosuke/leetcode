from collections import deque
from typing import List

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		dq = deque()
		i = 0
		dq.append(candidates[i])
		while dq:
