class Solution:
    def __init__(self):
        self.status = True
        self.MIN = -float('inf')
        self.MAX = float('inf')

    def isValidBST(self, root):
        return self.valid( root, self.MIN, self.MAX)

    def valid(self, root, minV, maxV):
        if not root:
            return self.status
        if root:
            if not (root.val > minV and root.val < maxV):
                self.status = False
        if root.left:
            if root.left.val < root.val:
                self.valid(root.left, minV, root.val)
            else:
                self.status = False
                return
        if root.right:
            if root.right.val > root.val:
                self.valid(root.right, root.val, maxV)
            else:
                self.status = False
                return

        return self.status

s = Solution()
print(s.isValidBST(n10))
