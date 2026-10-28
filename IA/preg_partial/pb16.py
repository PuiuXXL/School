class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_same(p, q):
    if p is None and q is None:
        return True
    if p.val != q.val:
        return False
    stanga = is_same(p.left,q.left)
    dreapta = is_same(p.right,q.right)

    return stanga and dreapta

p = TreeNode(1,TreeNode(2),TreeNode(3))
q = TreeNode(1,TreeNode(2),TreeNode(3))

print(is_same(p,q))