class Solution:
    LETTERS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans, level, s = [], 0, ''
        self.findCombinations(level, ans, digits, s)
        return ans
    
    def findCombinations(self, level, ans, digits, s):
        if level == len(digits):
            ans.append(s)
            return
        for l in self.LETTERS[digits[level]]:
            self.findCombinations(level+1, ans, digits, s+l)
