class Solution:
    def dfs(self, s, res, l, r, n):
        if l == n and r == n:
            res.append(s)
            return
        if l < n:
            self.dfs(s+'(', res, l+1, r, n)
        if r < l:
            self.dfs(s+')', res, l, r+1, n)

    def generateParenthesis(self, n: int):
        res = []
        s = ''
        level = 0
        self.dfs(s, res, 0, 0, n)
        return res
