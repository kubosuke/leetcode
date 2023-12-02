class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        for i in range(1, len(nums)):
            if cur == 0:
                return False
            cur -= 1
            cur = max(cur, nums[i])
        return True
