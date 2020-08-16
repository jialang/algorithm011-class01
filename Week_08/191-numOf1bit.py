class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        # while n > 0:
        #     if n & 1 == 1:
        #         cnt +=1
        #     n = n >> 1
        # return cnt
        while n > 0:
            cnt += 1
            n = n & (n-1)
        return cnt
