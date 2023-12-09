from functools import reduce
from typing import Set


class Solution:
    s: Set[int]

    def __init__(self) -> None:
        self.s = set()

    def isHappy(self, n: int) -> bool:
        digits = list(map(int, list(str(n))))
        d = sum(dd * dd for dd in digits)
        if d == 1:
            return True
        if d in self.s:
            return False
        self.s.add(d)
        return self.isHappy(sum(dd * dd for dd in digits))


print(Solution().isHappy(17))
