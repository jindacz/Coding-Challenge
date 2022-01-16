104. Maximum Depth of Binary Tree
Easy

5593

115

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

第七章 tree
前面一章说的是数据结构中比较简单的链表，这一张即将了解tree。tree分为很多种，通常数据结构说的是二叉树，二叉树像链表的变种，只是链表只有一个指针域，二叉树有两个而已。
7.1二叉树的最大深度
7.1.1算法要求
给定一个二叉树，找出其最大深度
二叉树的深度为根节点到最远也子节点最长路径上的节点树
说明：也子节点是指没有子节点的节点。

eg：给定二叉树【3，9，20，null，null，15，7】
返回它的最大深度3

7.1.2解题思路
一般来说，做有关二叉树的题都是使用递归的。因为递归很容易理解。也不需要取关二叉树的父子孙节点的关系。因此这里只需要理清root节点的关系。至于其他的节点，使用递归。以二叉树root=【3，9，20，None，None，15，7】为例。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
        	return 0
        else:
        	return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))
