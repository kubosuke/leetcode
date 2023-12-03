class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = d[s[-1]]
        now = s[-1]
        for i in reversed(range(0, len(s) - 1)):
            if d[now] > d[s[i]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
            now = s[i]
        return ans


s = "LVIII"
print(Solution().romanToInt(s))
