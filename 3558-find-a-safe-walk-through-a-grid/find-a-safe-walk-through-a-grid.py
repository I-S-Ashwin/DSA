class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        q = [(0, 0, health - grid[0][0])]
        
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = health - grid[0][0]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y, h = q.pop(0)
            
            if (x, y) == (m-1, n-1) and h >= 1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > 0 and nh > visited[nx][ny]:
                        visited[nx][ny] = nh
                        q.append((nx, ny, nh))
        
        return False
