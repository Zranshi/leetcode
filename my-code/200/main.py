from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        marks = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or marks[i][j] == 1:
                    continue
                res += 1
                queue = deque([(i, j)])
                while len(queue) != 0:
                    idx = queue.popleft()
                    for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        _x, _y = idx[0] + x, idx[1] + y
                        if (
                            0 <= _x < len(grid)
                            and 0 <= _y < len(grid[0])
                            and grid[_x][_y] == "1"
                            and marks[_x][_y] == 0
                        ):
                            marks[_x][_y] = 1
                            queue.append((_x, _y))

        return res


print(
    Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
