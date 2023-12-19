# Reorder Routes to Make All Paths Lead to the City Zero
# Medium

# This algorithm works, but exceeds time

class Solution:
    def minReorder(self, n: int, connections: 'list[list[int]]') -> int:
        
        self.flips = 0
        
        def dfs(city: int, visited):
            
            neighbours = [vertex for vertex in connections if city in vertex]
            for nei in neighbours:
                
                if tuple(nei) in visited: continue
                start, finish = nei[0], nei[1]

                if finish == city:
                    visited.add(tuple(nei))
                    dfs(start, visited)
                
                elif start == city:
                    self.flips += 1
                    visited.add(tuple(nei))
                    dfs(finish, visited)

        
        dfs(0, set())
        return self.flips
