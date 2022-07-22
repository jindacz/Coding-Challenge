# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val: # if both are greater, go to right subtree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: # if both are less, go to right subtree
                cur = cur.left
            else: # if split occurs, or one of them are equal to cur, LCA is found
                return cur
            
"""
if one of p, q are root, no decendents, return root
start with root 
7, 9 are both right subtree, go to right subtree
since 7, 9 are at different subtree, the split occurs
return 8 as LCA
        
time - o(logn) only visit one node for every single level, is the height of the tree
space - o(1)
"""