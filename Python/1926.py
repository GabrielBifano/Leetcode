# Nearest Exit from Entrance in Maze
# Medium
# 678 ms => Faster than 100% on 21/12/2023 (very ugly, I know)

from collections import deque

class Solution:
    def nearestExit(self, maze: 'list[list[str]]', entrance: 'list[int]') -> int:
        
        m = len(maze)
        n = len(maze[0])
        visited = set()
        x, y = entrance
        visited.add((x, y))

        steps = 0
        queue = deque()
        queue.extend([
            ((x-1,y), 1),
            ((x+1,y), 1),
            ((x,y-1), 1),
            ((x,y+1), 1),
        ])

        while len(queue) != 0:
        
            coords, steps = queue.popleft()
            x, y = coords
            if x < 0 or x >= m: continue
            if y < 0 or y >= n: continue
            if maze[x][y] == '+': continue
            if (x, y) in visited: continue
            if x == 0 or x == m - 1: return steps
            if y == 0 or y == n - 1: return steps
        
            visited.add((x, y))
            queue.extend([
                ((x-1,y), steps+1),
                ((x+1,y), steps+1),
                ((x,y-1), steps+1),
                ((x,y+1), steps+1),
            ])
        
        return -1