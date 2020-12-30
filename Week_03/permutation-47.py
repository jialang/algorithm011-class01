from itertools import permutations
class Solution:
    def permuteUnique(self, nums):
        res, n = set(), len(nums)
        for x in permutations(nums, n):
            res.add(x)
        return res
