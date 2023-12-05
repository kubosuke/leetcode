class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = 0
                while True:
                    try:
                        ans += s[i + j * (numRows + 1)]
                        j += 1
                    except IndexError:
                        break
