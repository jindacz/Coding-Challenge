# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        # look at root node
        root.left, root.right = root.right, root.left
        # recursive run function on left subTree and right subTree use DFS
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


s = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(s.invertTree(root))