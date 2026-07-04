class Solution:
    def minScore(self, n, roads):
        graph = [[] for _ in range(n+1)]
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = [False] * (n+1)
        ans = 10**9
        q = [1]
        visited[1] = True
        
        while q:
            u = q.pop(0)
            for v, w in graph[u]:
                if w < ans:
                    ans = w
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return ans
