class Solution:
    def numSquares(self, n: int) -> int:
        candidates = []
        for i in range(1, n+1):
            if i*i == n:
                return 1
            elif i*i < n:
                candidates.append(i*i)
            else:
                break
        a = [float('inf')] * (n+1)
        a[0] = 0
        for i in range(1, n+1):
            for k in candidates:
                if i<k:
                    break
                else:
                    a[i] = min(a[i], a[i-k]+1)
        return a[-1]
