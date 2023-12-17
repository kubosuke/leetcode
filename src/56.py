from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        ans = []
        i = 0
        l = intervals[0][0]
        r = intervals[0][1]
        while i < len(intervals):
            j = i + 1
            for j in range(i + 1, len(intervals)):
                if r < intervals[j][0]:
                    ans.append([l, r])
                    i = j
                    l = intervals[i][0]
                    r = intervals[i][1]
                    break
                l = min(l, intervals[j][0])
                r = max(r, intervals[j][1])
            if len(intervals) - 1 <= j:
                ans.append([l, r])
                break
        return ans


# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(Solution().merge([[1, 4], [4, 5]]))
# print(Solution().merge([[1, 4], [2, 3]]))
# print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
# print(Solution().merge([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))
print(Solution().merge([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]]))
