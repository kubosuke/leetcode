from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #
        if endWord not in wordList:
            return 0

        #
        d = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                d[w[:i] + "*" + w[i + 1 :]].append(w)

        #
        visited = defaultdict(lambda: False)
        visited[beginWord] = True
        dq = deque([(beginWord, 1)])
        while dq:
            v, cnt = dq.popleft()
            if v == endWord:
                return cnt

            next = [v[:i] + "*" + v[i + 1 :] for i in range(len(v))]
            for n in next:
                for dd in d[n]:
                    if not visited[dd]:
                        dq.append((dd, cnt + 1))
                        visited[dd] = True
        return 0

    def is_ladderable(self, a: str, b: str):
        if len(a) != len(b):
            return False

        cnt = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                cnt += 1
            if cnt > 1:
                return False
        return cnt == 1


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
