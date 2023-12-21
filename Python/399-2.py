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
        
        def dfs(q, target, s):
            nonlocal visited, big
            if q not in adj or target not in adj: return -1.0
            if q == target: return s
            visited.add(q)
            for n, w in adj[q]:
                if n in visited: continue
                val = dfs(n, target, s * w)
                if big < val: big = val
            return big

        answers = []
        for q0, q1 in queries:
            big = -1.0
            visited = set()
            answers.append(dfs(q0, q1, 1))

        return answers