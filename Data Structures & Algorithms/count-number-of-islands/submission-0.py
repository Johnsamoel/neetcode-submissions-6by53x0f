class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [1,0], 
            [-1,0], 
            [0,1], 
            [0,-1]
            ]
        rows, cols = len(grid), len(grid[0])
        seen = set()
        numOfIslands = 0

        def dfs(r, c):
            seen.add((r,c))
            
            for row, col in directions:
                nr, nc = r + row, c + col

                if (nr < 0
                    or nr >= len(grid)
                    or nc < 0
                    or nc >= len(grid[0])
                    or grid[nr][nc] != "1"
                    or (nr, nc) in seen
                    ):
                    continue

                dfs(nr, nc)

            return 
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    numOfIslands += 1

        
        return numOfIslands

            
                