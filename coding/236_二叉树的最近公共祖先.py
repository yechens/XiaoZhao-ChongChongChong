"""
题目描述：
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例：
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

解题思路：
一个节点如果刚好是p,q的最近公共祖先的话，要么它本身为p 或者 q,要么它的左右子树分别包含p , q中的一个，因此可以使用递归f(x)判断节点x是否包含p或者q中的一个，当满足上述条件时，即可找到最深的最近公公祖先。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root
        self.helper(root, p, q)
        return self.ans

    
    def helper(self, root, p, q):
        if not root:
            return False
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if (left and right) or ((root.val==p.val or root.val==q.val) and (left or right)):
            self.ans = root
        return left or right or (root.val==p.val or root.val==q.val)
