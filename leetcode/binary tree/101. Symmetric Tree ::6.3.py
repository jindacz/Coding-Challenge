101. Symmetric Tree
Easy

8270

203

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    	if not root:
    		return True
    	else:
    		return self.symmetricTree(root.left,root.right) #递归左右子

    def symmetricTree(self,lNode,rNode): 
    #重新定义被递归的函数。理由是确定一棵树是否对称需要输入两个参数，需要左右两个子节点，原本函数只限定了一个函数
    	if not lNode and not rNode:
    		return True
    	elif lNode and rNode and lNode.val==rNode.val: #判断是否相等
    		return self.symmetricTree(lNode.right,rNode.left) and self.symmetricTree(lNode.left,rNode.right)
    	else:
    		return False