# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        # helper function: compare two trees is same tree
        def sameTree(s, t):
            # base cases for recursion
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            
            return sameTree(s.left, t.left) and sameTree(s.right, t.right)
        
        # base cases for recursion
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        # if not same tree of left subtree and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
            
        