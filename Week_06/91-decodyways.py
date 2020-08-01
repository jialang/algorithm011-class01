class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s) < 1:
            return 0
        elif s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        else:
            d = [0] * (len(s)+1)
            d[0], d[1] = 1, 1
            for i in range(2, len(s)+1):
                last = int(s[i-1])
                seclast = int(s[i-2:i])
                if last > 0 and last <= 9:
                    d[i] += d[i-1]
                if seclast >= 10 and seclast <=26:
                    d[i] += d[i-2]
            return d[-1]
