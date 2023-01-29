from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        s = i + 1
        t = n - 1
        while s < t:
            nums[s], nums[t] = nums[t], nums[s]
            s += 1
            t -= 1


v = [1, 2, 3]
print(v)
Solution().nextPermutation(v)
print(v)
assert v == [1, 3, 2]

v = [3, 2, 1]
print(v)
Solution().nextPermutation(v)
print(v)
assert v == [1, 2, 3]

v = [1, 1, 5]
print(v)
Solution().nextPermutation(v)
print(v)
assert v == [1, 5, 1]

v = [1, 2]
print(v)
Solution().nextPermutation(v)
print(v)
assert v == [2, 1]

v = [1, 3, 2]
print(v)
Solution().nextPermutation(v)
print(v)
assert v == [2, 1, 3]
