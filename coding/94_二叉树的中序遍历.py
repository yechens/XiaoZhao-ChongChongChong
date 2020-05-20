"""
题目描述：
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

解题思路：
递归遍历很简单；非递归解法用一个栈（数组）来保存遍历过程中的节点，且优先考虑左节点
中序遍历顺序：左 -> 根 -> 右
时间复杂度：O(n)
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        # 1.非递归遍历
        result = []
        stack = [root]
        node = root
        while stack:
            while node and node.left:
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
                node = node.right
            else:
                node = None # 右节点不存在时要置空，否则会重复遍历

        return result

        # 递归遍历        
        def inOrder(root, res):
            if not root:
                return
            inOrder(root.left, res)
            res.append(root.val)
            inOrder(root.right, res)
            return res

        return inOrder(root, [])
