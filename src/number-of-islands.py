from collections import deque
from typing import List


class Solution:
    grid = [[]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.grid = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == "1":
                    self.bfs(i, j)
                    cnt += 1
        return cnt

    def bfs(self, x: int, y: int):
        dq = deque()
        dq.append((x, y))
        while dq:
            v = dq.popleft()
            a, b = v[0], v[1]
            for dxx, dyy in zip(self.dx, self.dy):
                nx = a + dxx
                ny = b + dyy
                if nx < 0 or nx > len(self.grid) - 1 or ny < 0 or ny > len(self.grid[0]) - 1:
                    continue
                if self.grid[nx][ny] == "1":
                    dq.append((nx, ny))
                    self.grid[nx][ny] = "0"


if __name__ == "__main__":
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(grid))
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(grid))
