class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char for char in s if char.isalpha() or char.isdigit()).lower()
        for i in range(len(res)):
            if res[i] != res[len(res) - i - 1]:
                return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("0P"))
