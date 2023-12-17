from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(lambda: [])

        for i, v in enumerate(nums):
            d[v].append(i)
        for l in d.values():
            for i in range(len(l) - 1):
                if l[i + 1] - l[i] <= k:
                    return True
        return False


print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
