
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# recursion
class Solution:
    def preorder(self, root):
        if not root:
            return 
        res = []
        self.traverseP(root, res)
        return res
    def traverseP(self, root, res):
        if not root:
            return res
        res.append(root.val)
        for x in root.children:
            self.traverseP(x, res)
# iteration
class Solution:
    def preorder(self, root):
        if not root: 
            return []
        s, res = [root], []
        while s:
            tmp = s.pop()
            res.append(tmp.val)
            if tmp.children:
                s.extend(tmp.children[::-1])
        return res
