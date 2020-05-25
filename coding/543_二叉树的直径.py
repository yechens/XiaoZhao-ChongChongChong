"""
题目描述：
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。

解题思路：
采用递归函数f(x)代表节点x的左孩子和右孩子的最大深度的列表，维护一个self.ans存储全局最大的直径，最后返回self.ans即可，可以避免通过根的直径小于不通过根的直径的bad case。
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            #左右孩子都没有
            if not root.left and not root.right:
                tmp = [0, 0]
            #只有左孩子
            elif not root.right:
                tmp = [max(helper(root.left)) +1, 0]
            #只有右孩子
            elif not root.left:
                tmp = [0, max(helper(root.right))+1]
            #左右孩子均存在
            else:
                tmp = [max(helper(root.left)) +1, max(helper(root.right)) + 1]
            self.ans = max(self.ans, sum(tmp))
            return tmp

        self.ans = 0
        if root:
            helper(root)
        return self.ans
            
