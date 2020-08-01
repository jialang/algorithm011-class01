class Solution:
    def helper(self, nums):
        n = len(nums)
        a = [[-1] * 2 for _ in range(n)]
        a[0][0] = 0
        a[0][1] = nums[0]
        for i in range(1, n):
            a[i][0] = max(a[i-1][1], a[i-1][0])
            a[i][1] = a[i-1][0]+ nums[i]
        return max(a[n-1][0], a[n-1][1])

    def rob(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        res1 = self.helper(nums[1:])
        res2 = self.helper(nums[:-1])
        return max(res1, res2)
