"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        s = [root]
        res = []
        while s:
            cur = []
            nex = []
            for x in s:
                cur.append(x.val)
                if x.children:
                    nex.extend(x.children)
            res.append(cur)
            s = nex
        return res
