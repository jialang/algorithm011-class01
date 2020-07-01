# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s, res = [], []
        tmp = root
        while tmp or s:
            if tmp:
                s.append(tmp)
                while tmp.left:
                    s.append(tmp.left)
                    tmp = tmp.left
            tmp = s.pop()
            res.append(tmp.val)
            tmp = tmp.right
                
        return res
