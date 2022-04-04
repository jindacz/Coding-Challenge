98. Validate Binary Search Tree
Medium

8384

813

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1


7.2验证二叉搜索树
7.2.1算法要求
给定一棵二叉树，判断其是否是一棵有效的二叉搜树
假设一棵二叉搜索树具有如下特征：
·左边小于当前
·右边大于当前
·左子树和右子树都是二叉搜索树

eg1:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

7.2.2解题思路
这一题还是用递归。需要解决，按照题目的定义，rott的值必须大于左边所有节点的值，小于右边所有节点的值。那么可以预测，左边节点的值，深度越深就越小，左边最深节点的left是最小的；右边最深节点的right的值是最大的。那么这个最大值和最小值是多少呢？
在python3定义了最大值，max=sys.maxsize。一天你次这里也可以推算出min=sys.maxsize*（-1）。max和min有了，就可以得出一条结论。在root节点中，所有左边节点的值大于min，右边节点的值小于max。否则root节点必定不是二叉搜索树。以root=【5，1，4，None，None，3，6】为例。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import sys
        min=sys.maxsize*(-1)
        max=sys.maxsize
        return self.validBST(root,min,max)

    def validBST(self,root,min,max):
    	if root==None:
    		return True
    	if root.val<=min or root.val>=max:
    		return False
    	return self.validBST(root.left,min,root.val) and self.validBST(root.right,root.val,max) #左边小于当前,右边大于当前

这一道题重新定义了一个validBST函数用于递归，避免了干扰。