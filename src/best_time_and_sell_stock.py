from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = None

        for p in prices:
            if l is None:
                l = p
            elif l < p:
                ans += p - l
                l = p
            else:
                l = p
        return ans


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
