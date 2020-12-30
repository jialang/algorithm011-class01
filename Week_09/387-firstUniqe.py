from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s):
        d = OrderedDict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = (1, i)
            else:
                d[s[i]] = (2, i)
        for k in d:
            if d[k][0] == 1:
                return d[k][1]
        return -1
