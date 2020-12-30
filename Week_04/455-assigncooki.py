class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        cnt, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1
        return cnt
