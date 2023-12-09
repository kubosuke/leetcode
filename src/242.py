from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(lambda: 0)
        dt = defaultdict(lambda: 0)
        for ss in s:
            ds[ss] += 1
        for tt in t:
            dt[tt] += 1
        return ds == dt
