'''
题目描述:
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null

解题思路：
中序遍历


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        
        #中序遍历
        self.res=[]
        self.final_res=None
        def traverse(root):
            if not root :return None       
            traverse(root.left)
            if self.res and self.res[-1]==p:
                self.final_res=root
            self.res.append(root)
            traverse(root.right)
        traverse(root)
        return self.final_res

            
            
