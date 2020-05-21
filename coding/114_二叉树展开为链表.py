'''
题目描述:
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

解题思路：
递归法：先排好左右子树，再链接左右子树
方法一：每次遍历都find子树的终端节点（while循环）
方法二：保存链表化后子树的终端节点，不用每次使用时都find （递归函数每次多返回一个子树终端节点）

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #递归版-v1 每次遍历都find子树的终端节点（为什么该方法使用时间更少？？？）
        lastnode=None
        def fun(root):
            if root is None:
                return None
            #最开始的状态
            #左边操作  
            leftnode=fun(root.left)
            rightnode=fun(root.right)
            if leftnode:      
                #左子树的最右结点
                tmpright=leftnode
                while tmpright.right is not None:
                    tmpright=tmpright.right       
                if rightnode:
                    tmpright.right=root.right
                    root.right=leftnode        
                else:
                    root.right=leftnode
                root.left=None
            #else:
            #    if rightnode:
            return root
        fun(root)
        return  root

        #保存链表化后子树的终端节点，不用每次使用时都find
        def main(root):
            if not root:return None,None
            left_node,endl=main(root.left)
            right_node,endr=main(root.right)
            if not left_node:
                if not right_node:
                    return root,root
                else:
                    return root,endr
            else:
                if not right_node:
                    root.right=left_node
                    root.left=None
                    return root,endl
                else:
                    tmpr=root.right
                    root.right=left_node
                    root.left=None
                    endl.right=right_node
                    endl.left=None
                    return root,endr
        return main(root)

        
                
