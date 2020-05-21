"""
题目描述：
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

解题思路：
BST的中序遍历是升序，从小到大
按先右后左的顺序遍历，就是从大到小了; 然后累加 num 即可
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        global num # 存放全局的累加值，用来更新当前遍历的节点
        num = 0
        def helper(root):
            global num
            if not root:
                return
            # 先右后左的顺序遍历
            helper(root.right)
            root.val += num
            num = root.val # 用当前节点的 val 更新 num
            helper(root.left)

        helper(root)
        return root
