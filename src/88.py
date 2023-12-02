class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        w = 0
        i = 0
        j = 0
        nums = nums1[:m].copy()
        print(nums)

        for _ in range(m + n):
            if (j >= n) or (i < m and nums[i] < nums2[j]):
                nums1[w] = nums[i]
                i += 1
            else:
                nums1[w] = nums2[j]
                j += 1
            w += 1
