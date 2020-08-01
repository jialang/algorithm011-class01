class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [float('inf')] * (amount+1)
        a[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    a[i] = min(a[i], a[i-j]+1)
        if a[amount] == float('inf'):
            return -1
        else:
            return a[amount]
