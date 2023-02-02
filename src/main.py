class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return (m+n)**(m+n) - (m**m) - (n**n)

print(Solution().uniquePaths(3,7))
