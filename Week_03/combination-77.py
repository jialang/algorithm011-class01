class Solution:
    def combine(self, n, k):
        res = []
        self.findC(1, [], res, n, k)
        return res
    def findC(self, level, tmp, res, n, k):
        if len(tmp) == k:
            res.append(tmp[:])
            return
        for i in range(level, n+1):
            self.findC(i+1, [i]+tmp, res, n, k)
