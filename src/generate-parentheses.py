from itertools import product
from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         candinate = [''.join(x) for x in product('()', repeat=2*n)]
#         return [c for c in candinate if (self.ok(c))]

#     def ok(self, s: str) -> bool:
#         l = 0
#         for ss in s:
#             if l < 0:
#                 return False
#             match ss:
#                 case "(":
#                     l += 1
#                 case ")":
#                     l -= 1
#         return l == 0

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

print(Solution().generateParenthesis(int(input())))
