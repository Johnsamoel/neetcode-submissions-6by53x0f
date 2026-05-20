class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addNeigbour(r, c):
            if (r < 0 
            or r == ROWS 
            or c < 0 
            or c == COLS
            or (r, c) in visit
            or grid[r][c] == 0
            ):
                return

            q.append([r,c])
            visit.add((r,c))
            grid[r][c] = 2 # mark adj nei as rotten

        # fill the queue with possible sources
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        minutes = 0
        # BFS
        while q:
            size = len(q)

            for _ in range(size):
               r, c = q.popleft()
               if grid[r][c] == 2:
                    addNeigbour(r + 1, c)
                    addNeigbour(r - 1, c)
                    addNeigbour(r, c + 1)
                    addNeigbour(r, c - 1)
            if q:
                minutes += 1

        # second check if all are rotten
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes

            

