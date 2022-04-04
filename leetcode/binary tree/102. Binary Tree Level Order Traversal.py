102. Binary Tree Level Order Traversal
Medium

6850

138

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
Accepted
1,084,265
Submissions
1,812,571


7.4二叉树的层次遍历
7.4.1算法要求
给定一棵二叉树，返回其按层次遍历的节点值（逐层地，从左到右访问所有节点）。

例如：
给定二叉树【3，9，20，null，null，15，7】
返回层次遍历结果：【【3】，【9，20】，【15，7】】

7.4.2解题思路
这一道题和其他题目有点不一样。其他的题是以节点为单位操作的，而这一道题是以层为单位操作的，树的层数越多，节点就越多，而且对节点值还有顺序的要求。因此，这一道题对节点的递归效果可能没有那么好。换个思路，对层进行迭代。给定二叉树【3，9，20，null，null，15，7】，如图7-10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    	if not root:
    		return []
    	ans,level=[],[root]

    	while level:
    		ans.append([node.val for node in level])
    		temp=[]

    		for node in level:
    			temp.extend([node.left,node.right])
    		level=[leaf for leaf in temp if leaf]
    	return ans