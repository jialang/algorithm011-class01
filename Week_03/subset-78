class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        ans, l = [], []
        self.subresults(nums, l, ans, 0)
        return ans
    
    def subresults(self, nums, l, ans, level):
        if level == len(nums):
            ans.append(l)
            return
        self.subresults(nums, l.copy(), ans, level+1)
        l.append(nums[level])
        self. subresults(nums, l.copy(), ans, level+1)
