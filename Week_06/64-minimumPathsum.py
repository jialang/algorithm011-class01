class Solution:
    def minPathSum(self, grid):
        r = len(grid)
        c = len(grid[0])
        d = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    d[i][j] = grid[i][j]
                elif i == 0:
                    d[i][j] = d[i][j-1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i-1][j] + grid[i][j]
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1]) + grid[i][j]
        return d[-1][-1]  
