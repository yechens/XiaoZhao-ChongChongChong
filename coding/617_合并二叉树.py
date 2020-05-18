"""
题目描述：
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例：
输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

题解思路：
目前能想到的是以空间换时间，新建一个root树，同步递归遍历t1和t2，判断递归中左右节点是否存在，更新root树的节点
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            root = TreeNode(t1.val + t2.val)
            self.helper(t1, t2, root)
            return root


    def helper(self, t1, t2, root):
        if t1.left and t2.left:
            root.left = TreeNode(t1.left.val + t2.left.val)
            self.helper(t1.left, t2.left, root.left)
        elif t1.left:
            root.left = t1.left
        elif t2.left:
            root.left = t2.left
        if t1.right and t2.right:
            root.right = TreeNode(t1.right.val + t2.right.val)
            self.helper(t1.right, t2.right, root.right)
        elif t1.right:
            root.right = t1.right
        elif t2.right:
            root.right = t2.right
