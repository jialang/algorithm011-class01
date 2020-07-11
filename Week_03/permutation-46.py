class Solution:
    def findp(self, level, nums, n, res):
        if level == n:
            res.append(nums[:])
            return
        for i in range(level, n):
            if i != level and nums[i] == nums[level]:
                continue
            nums[level], nums[i] = nums[i], nums[level]
            self.findp(level + 1, nums, n, res)
            nums[level], nums[i] = nums[i], nums[level]

    def p(self, nums):
        n = len(nums)
        res = []
        self.findp(0, nums, n, res)
        return res
