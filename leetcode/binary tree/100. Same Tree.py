class Solution(object):
    def isSameTree(self, p, q):
        # if both empty trees
        if not p and not q:
            return True
        # only one of them are empty, or both not empty but does not have same value
        if not p or not q or p.val != q.val:
            return False
        # check left subtrees, right subtrees
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # T: o(p+q), iterate through all node