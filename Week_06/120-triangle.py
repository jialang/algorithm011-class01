class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        res = triangle[-1]
        for i in range(l-2, -1,-1):
            for j in range(len(triangle[i])):
                res[j] = triangle[i][j] + min(res[j+1], res[j])
        return res[0]
