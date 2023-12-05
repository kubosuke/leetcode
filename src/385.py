from collections import defaultdict


class Solution:
    def check1(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(lambda: 0)
        for m in magazine:
            d[m] += 1
        for r in ransomNote:
            v = d.get(r)
            if not v or v == 0:
                return False
            d[r] -= 1
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return self.check1(ransomNote=ransomNote, magazine=magazine)
