class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t = TreeNode()
t.val = 2

t.right = TreeNode(val=2, left=TreeNode(val=1))

print(hash(t))