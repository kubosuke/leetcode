from typing import List


class Solution:
    def check(self, s: List[str], i: int) -> bool:
        try:
            t = s[0][i]
            for ss in s:
                if ss[i] != t:
                    return False
        except IndexError:
            return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            if self.check(strs, i):
                i += 1
            else:
                break
        return strs[0][:i] if strs[0] != "" else ""
