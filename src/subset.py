from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for bit in range(1 << n):
            v = []
            for j in range(n):
                if bit & (1 << j) != 0:
                    v.append(nums[j])
            ans.append(v)
        return ans
                
res = Solution().subsets([9,0,3,5,7])
print(res)
res = Solution().subsets([7])
print(res)
res = Solution().subsets([9,0])
print(res)