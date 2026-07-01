class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        dist = [[-1] * n for _ in range(n)]
        queue = []
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        head = 0
        while head < len(queue):
            r, c = queue[head]
            head += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        def isValidPath(min_safeness: int) -> bool:
            if dist[0][0] < min_safeness:
                return False
                
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            path_q = [(0, 0)]
            
            p_head = 0
            while p_head < len(path_q):
                r, c = path_q[p_head]
                p_head += 1
                
                if r == n - 1 and c == n - 1:
                    return True
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if dist[nr][nc] >= min_safeness:
                            visited[nr][nc] = True
                            path_q.append((nr, nc))
            return False

        low, high = 0, 2 * n
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if isValidPath(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans