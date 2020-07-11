from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = set(), len(nums)
        for x in permutations(nums, n):
            res.add(x)
        return res
