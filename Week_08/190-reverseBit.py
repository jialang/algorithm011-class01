class Solution:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31
        while n > 0:
            ans += (n&1) << power
            power -= 1
            n = n >> 1
        return ans
