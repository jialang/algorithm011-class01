class Solution:
    def canJump(self, nums):
        reachable = 0
        for idx, val in enumerate(nums):
            if idx > reachable:
                return False
            reachable = max(reachable, idx + nums[idx])
        return True
s = Solution()
print(s.canJump([3,2,1,0,4]))
