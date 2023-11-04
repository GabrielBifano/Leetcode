# Equal Row and Column Pairs
# Medium

from collections import defaultdict

def equalPairs(grid: 'list[list[int]]') -> int:
        
        rows    = defaultdict(int)
        columns = defaultdict(int)

        for row in grid:
            l = [str(x) for x in row]
            s = "*".join(l)
            rows[s] += 1

        for column in zip(*grid):
            l = [str(x) for x in column]
            s = "*".join(l)
            columns[s] += 1

        count = 0
        for k in rows.keys():
            if columns[k] > 0:
                count += columns[k] * rows[k]

        return count