class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a+b
        return b
    def climbStairs123(self, n):
        if n < 1:
            return 0
        if n <= 2:
            return n
        a, b, c, d = 1, 1, 2, 0
        for i in range(3, n+1):
            d = a+b+c
            a, b, c = b, c, d
        return d
