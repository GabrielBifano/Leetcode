# Evaluate Division
# Medium

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: 'list[list[str]]', values: 'list[float]', queries: 'list[list[str]]') -> 'list[float]':
        adj = defaultdict(list)
        for eq, val in zip(equations, values):
            s1, s2 = eq
            adj[s1].append((s2, val))
            adj[s2].append((s1, 1/val))
        
        def dfs(q, target, s, visited, big):
            if q not in adj or target not in adj: return -1.0
            if q == target: return s
            visited.add(q)
            for n, w in adj[q]:
                if n in visited: continue
                val = dfs(n, target, s * w, visited, big)
                if big < val: big = val
            return big

        answers = [dfs(q0, q1, 1, set(), -1.0) for q0, q1 in queries]
        return answers