class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[0] * (n+1) for _ in range(m+1)]
        d[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m][n]
