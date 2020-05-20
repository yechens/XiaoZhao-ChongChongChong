"""
题目描述：
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

解题思路：
前序遍历可以知道每个子树的根节点，中序遍历可以通过得到的根节点划分为左右2个子树部分，类似于分治思想
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        self.i = 1
        root.left = self.helper(0, index-1, preorder, inorder)
        root.right = self.helper(index+1, len(preorder)-1, preorder, inorder)
        return root

        
    def helper(self, s, e, preorder, inorder):
        if not s <= e:
            return None
        node = TreeNode(preorder[self.i])
        self.i += 1
        index = inorder.index(node.val)
        node.left = self.helper(s, index-1, preorder, inorder)
        node.right = self.helper(index+1, e, preorder, inorder)
        return node
