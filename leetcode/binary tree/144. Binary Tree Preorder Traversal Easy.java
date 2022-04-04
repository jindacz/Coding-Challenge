144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?


/*definition for a binary tree node
public class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(){}
	TreeNode(int val) {this.val=val;}
	TreeNode(int val,TreeNode left,TreeNode right){
		this.val=val;
		this.left=left;
		this.right=right;
	}
}
*/

方法一：递归
思路与算法

首先我们需要了解什么是二叉树的前序遍历：按照访问根节点——左子树——右子树的方式遍历这棵树，而在访问左子树或者右子树的时候，我们按照同样的方式遍历，直到遍历完整棵树。因此整个遍历过程天然具有递归的性质，我们可以直接用递归函数来模拟这一过程。

定义 preorder(root) 表示当前遍历到 root 节点的答案。按照定义，我们只要首先将 root 节点的值加入答案，然后递归调用 preorder(root.left) 来遍历 root 节点的左子树，最后递归调用 preorder(root.right) 来遍历 root 节点的右子树即可，递归终止的条件为碰到空节点。


class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
    	List<Integer> res=new ArrayList<Integer>(); //build-up a result List
    	preorder(root,res);
    	return res;
    }

    public void preorder(TreeNode root,List<Integer> res){
    	if(root==null){
    		return;
    	}
    	res.add(root.val);
    	preorder(root.left,res);
    	preorder(root.right,res);
    }
}

//
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。每一个节点恰好被遍历一次。

空间复杂度：O(n)O(n)，为递归过程中栈的开销，平均情况下为 O(\log n)O(logn)，最坏情况下树呈现链状，为 O(n)O(n)。

方法二：迭代
思路与算法

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) {
            return res;
        }

        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                res.add(node.val);
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            node = node.right;
        }
        return res;
    }
}


方法三：Morris 遍历
思路与算法

有一种巧妙的方法可以在线性时间内，只占用常数空间来实现前序遍历。这种方法由 J. H. Morris 在 1979 年的论文「Traversing Binary Trees Simply and Cheaply」中首次提出，因此被称为 Morris 遍历。

Morris 遍历的核心思想是利用树的大量空闲指针，实现空间开销的极限缩减。其前序遍历规则总结如下：

新建临时节点，令该节点为 root；

如果当前节点的左子节点为空，将当前节点加入答案，并遍历当前节点的右子节点；

如果当前节点的左子节点不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点：

如果前驱节点的右子节点为空，将前驱节点的右子节点设置为当前节点。然后将当前节点加入答案，并将前驱节点的右子节点更新为当前节点。当前节点更新为当前节点的左子节点。

如果前驱节点的右子节点为当前节点，将它的右子节点重新设为空。当前节点更新为当前节点的右子节点。

重复步骤 2 和步骤 3，直到遍历结束。

这样我们利用 Morris 遍历的方法，前序遍历该二叉树，即可实现线性时间与常数空间的遍历。

//use stack keep pushing&poping to come BACK

//https://www.youtube.com/watch?v=wGXB9OWhPTg&t=327s&ab_channel=TusharRoy-CodingMadeSimple

Algorithm: pre-order
current=root
while current is not null
    if there does not exist current.left
        visit(current)
        current=current.right
    else 
        predecssor=findpredessor(current)
        if not exists predessor.right
            predessor.right=current
            visit(current)
            current=current.right
        else
            predessor.right=null;
            current=current.right;

Algo: in-order
current=root
while current is not null
    if there does not exist current.left
        visit(current)
        current=current.right
    else 
        predecssor=findpredessor(current)
        if not exists predessor.right
            predessor.right=current
            current=current.right
        else
            predessor.right=null;
            visit(current)
            current=current.right;





class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res=new ArrayList<Integer>();
        TreeNode predecessor=null;

        while(root!=null){  
             
            if(root.left!=null){ 
                //find predecessor : right-most
                predecessor=root.left;
                while(predecessor.right!=null&&predecessor.right!=root){ 
                    predecessor=predecessor.right;  
                }

                //let predecessor.right=root, 继续遍历左子树
                if(predecessor.right==null){  
                    res.add(root.val);  //preorder就先保存节点
                    predecessor.right=root; 
                    root=root.left; 
                    continue;
                }

                //左子树访问完毕，断开链接
                else{
                    predecessor.right=null;
                    root=root.right; 
                }
            }
            //如果没有左孩子，则直接访问右孩子
            else{ 
                res.add(root.val); 
                root=root.right;
            }
            
        }
        return res;
    }
}





