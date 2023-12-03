from functools import reduce
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = 0
        for i in range(len(gas)):
            gas[i] -= cost[i]
            s += gas[i]
        if s < 0:
            return -1
        g = 0
        ans = 0
        for i in range(len(gas)):
            g += gas[i]
            if g < 0:
                g = 0
                ans = i + 1
        return ans


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
