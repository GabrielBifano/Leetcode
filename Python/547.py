# Number of Provinces
# Medium

class Solution:        

    def dfs(self, node, isConnected, visited):
        visited.add(node)
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and i not in visited:
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected: 'list[list[int]]') -> int:

        p = 0
        width = len(isConnected)
        visited = set()

        while len(visited) != width:
            node = 0
            for i in range(width):
                if i not in visited:
                    node = i
            self.dfs(node, isConnected, visited)                        
            p += 1        
        return p
                