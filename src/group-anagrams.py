from typing import List
from collections import defaultdict

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		ans = []
		d = defaultdict(list)
		for i in range(len(strs)):
			s = "".join(sorted(strs[i]))
			d[s].append(i)
		for idxs in d.values():
			tmp = []
			for idx in idxs:
				tmp.append(strs[idx])		
			ans.append(tmp)
		return ans

res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)