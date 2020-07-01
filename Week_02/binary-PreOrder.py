def preOrder(root):
    if not root:
        return []
    res, s = [], []
    tmp = root
    while tmp or s:
        if tmp:
            res.append(tmp.val)
            while tmp.left:
                tmp = tmp.left
                s.append(tmp)
        tmp = s.pop()
        res.append(tmp.val)
        tmp = tmp.right
    return res
    
#recursion
def preOrder(root):
    if not root:
        return
    if root:
        print(root.val)
    preOrder(root.left)
    preOrder(root.right)
