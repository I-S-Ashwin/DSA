class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        
        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        
        dp[n-1][n-1] = (0, 1)
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X':
                    continue
                
                if i == n-1 and j == n-1:
                    continue
                
                maxScore, numPaths = -1, 0
                
                for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if x < n and y < n and dp[x][y][0] != -1:
                        score, paths = dp[x][y]
                        if score > maxScore:
                            maxScore = score
                            numPaths = paths
                        elif score == maxScore:
                            numPaths = (numPaths + paths) % MOD
                
                if maxScore == -1:
                    continue
                
                if board[i][j].isdigit():
                    maxScore += int(board[i][j])
                
                dp[i][j] = (maxScore, numPaths % MOD)
        
        return [max(dp[0][0][0], 0), dp[0][0][1]]
