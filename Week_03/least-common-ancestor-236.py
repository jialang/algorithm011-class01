class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = s.pop()
            if node.left:
                parent[node.left] = node
                s.append(node.left)
            if node.right:
                parent[node.right] = node
                s.append(node.right)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q
        
