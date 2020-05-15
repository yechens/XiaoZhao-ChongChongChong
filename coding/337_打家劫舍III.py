"""
题目描述：
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例：
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

解题思路：
采用动态规划加递归方法，对于每个节点，其最大收益为 max(当前节点选择偷+2个子节点选择不偷的收益, 当前节点不偷+2个节点偷或者不偷的最大收益）
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.helper(root)
        return max(result)
    
    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res0 = max(left) + max(right)
        res1 = root.val + left[0] + right[0]
        return [res0, res1]
