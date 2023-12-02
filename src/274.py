from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        for i in range(0, len(citations) + 2):
            if len(list(filter(lambda x: x >= i, citations))) < i:
                break
        return max(i - 1, 0)


print(Solution().hIndex([1]))
