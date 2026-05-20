class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addNei(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append([r,c])

        # fill the queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])

        dist = 0
        while q:
            size = len(q)

            for _ in range(size):
                r, c = q.popleft()
                grid[r][c] = dist

                addNei(r + 1, c)
                addNei(r, c + 1)
                addNei(r - 1, c)
                addNei(r, c - 1)
            dist += 1

