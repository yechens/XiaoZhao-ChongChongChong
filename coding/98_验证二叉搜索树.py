"""
题目描述：
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

解题思路：
（1）递归判断；除了当前节点本身，需要不断保存、更新到当前节点的最大值与最小值
（2）非递归：利用栈来模拟中序遍历，“BST树的中序遍历一定是升序”！
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # 1.递归判断,保存遍历到当前节点的最大值mmax和最小值mmin
        def helper(root, mmin=float('-inf'), mmax=float('inf')):
            if not root:
                return True
            if mmin < root.val < mmax:
                return helper(root.left, mmin, root.val) and \
                    helper(root.right, root.val, mmax)
            return False
        
        return helper(root)

        # 2.非递归中序遍历
        stack = []
        p = root
        mid = -1e20
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            val = p.val
            print(val)
            if val <= mid: # 一旦发现非升序，直接返回 False
                return False
            mid = val
            if p.right:
                p = p.right
            else:
                p = None
        return True
