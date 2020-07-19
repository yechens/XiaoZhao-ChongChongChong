'''
题目描述：
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

解题思路：
BFS

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        queue=[root]
        res=[]
        listdir=0
        while queue:
            tmpl=len(queue)
            tmprow=[]
            for i in range(tmpl):
                tmpnode=queue.pop(0)
                tmprow.append(tmpnode.val)
                if tmpnode.left:
                    queue.append(tmpnode.left)
                if tmpnode.right:
                    queue.append(tmpnode.right)
            if listdir==1:
                tmprow.reverse()
            res.append(tmprow)
            listdir=1 if listdir==0 else 0
        return res
