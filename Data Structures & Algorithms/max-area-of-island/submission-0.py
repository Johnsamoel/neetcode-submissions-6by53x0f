class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0, -1]
        ]

        seen = set()
        maxIsland = 0

        def dfs(r, c) -> int:
            count = 1
            seen.add((r, c))

            for row, col in directions:
                nr , nc = r + row, c + col

                if (
                    nr < 0 
                    or nr == len(grid)
                    or nc < 0
                    or nc == len(grid[0])
                    or grid[nr][nc] != 1
                    or (nr, nc) in seen
                    ):
                    continue
                count += dfs(nr, nc)

            return count 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    maxIsland = max(dfs(row, col), maxIsland)

        return maxIsland
