from collections import deque

class Solution:

    def orangesRotting(self, grid: 'list[list[int]]') -> int:
        
        # helper variables
        m, n = range(len(grid)), range(len(grid[0]))
        mask = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # get all initialy rotten oranges
        rotten = [(i, j) for i,_ in enumerate(grid) for j, _ in enumerate(grid[i]) if grid[i][j] == 2]

        # BFS
        steps = -1
        q = deque()
        q.extend(rotten)
        while q:
            for _ in range(len(q)):
                rot = q.popleft()
                for dx, dy in mask:
                    x, y = rot[0] + dx, rot[1] + dy
                    if x in m and y in n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
            steps += 1
        
        if any(1 in row for row in grid): return -1
        if steps == -1: return 0
        return steps
        
