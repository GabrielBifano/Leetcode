# Reorder Routes to Make All Paths Lead to the City Zero
# Medium

class Solution:
    def minReorder(self, n: int, connections: 'list[list[int]]') -> int:
        
        def dfs(node):
            nonlocal E, N, visited, changes
            for n in N[node]: # for each neighbour
                if n in visited: continue
                if ( n, node ) not in E:
                    changes += 1
                visited.add(n)
                dfs(n)

        E = { (x, y) for x, y in connections } # edge set
        N = { city:[] for city in range(n) }   # neighbours set
        visited = set()
        visited.add(0)
        changes = 0

        for x, y in connections:
            N[x].append(y)
            N[y].append(x)
        
        dfs(0)
        return changes