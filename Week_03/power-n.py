class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.mypow(1/x, -n)
        else:
            return self.mypow(x, n)
        
    def mypow(self, x, n):
        if n == 0:
            return 1
        subresult = self.myPow(x, n//2)
        if n % 2 == 0:
            return subresult * subresult
        else:
            return x * subresult * subresult
