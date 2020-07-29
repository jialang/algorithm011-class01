class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a+b
        return b
