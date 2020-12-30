# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        ltree = inorder[:idx]
        rtree = inorder[idx+1:]
        root.left  = self.buildTree(preorder, ltree)
        root.right = self.buildTree(preorder, rtree)

        return root
