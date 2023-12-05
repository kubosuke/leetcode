from typing import List


class Solution:
    def is_appendable(self, words: List[str], w: str, maxWidth: int) -> bool:
        return len(" ".join(words)) + len(w) <= maxWidth

    def padding(self, words: List[str], maxWidth: int) -> str:
        if len(words) == 1:
            return words[0].ljust(maxWidth)
        if " ".join(words) == maxWidth:
            return " ".join(words)
        words = list(map(lambda e: e + " ", words))
        words[-1] = words[-1].rstrip()
        i = 1
        while True:
            print(len(words))
            if i == len(words) - 1:
                i += 1
                continue
            i %= len(words)
            if len("".join(words)) >= maxWidth:
                return "".join(words)
            words[i] += " "
            i += 1

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur = []
        idx = 0
        while True:
            if idx == len(words):
                if cur:
                    ans.append(self.padding(cur, maxWidth))
                break
            if self.is_appendable(cur, words[idx], maxWidth):
                cur.append(words[idx])
                idx += 1
            else:
                ans.append(self.padding(cur, maxWidth))
                cur = []
        return ans
