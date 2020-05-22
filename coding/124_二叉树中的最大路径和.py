"""
题目描述：
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3
输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

解题思路：
递归遍历当前节点的左右孩子节点，并更新全局最大路径和
详见代码注释！
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.mmax = 0 # 存放全局最大路径和
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            # 更新遍历到当前节点可以访问到的最大值
            self.mmax = max(
                self.mmax,
                left + root.val + right,
                root.val,
                root.val + left,
                root.val + right
            )
            # 对于当前结点而言，只能返回 左+根、根、右+根、0（不选） 组合的最大值
            # 不能返回 左+根+右，因为该组合之前的节点不能够选取
            # 左+根+右 只能在判断全局的最大路径和时考虑进去
            return max(left + root.val, right + root.val, root.val, 0)
        
        helper(root)
        return self.mmax
