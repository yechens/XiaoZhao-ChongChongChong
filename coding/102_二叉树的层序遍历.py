'''
题目描述：
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
解题思路：
设置两个数组，一个存储每层节点，一个存储每层节点对应的value


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
        #保存每层节点
        queue=[root]
        #保存每层节点对应的value
        queue_val=[[root.val]]
        while queue:
            tmpl=len(queue)
            new_level_val=[]
            for i in range(tmpl):
                tmpnode=queue.pop(0)
                if tmpnode.left:
                    new_level_val.append(tmpnode.left.val)
                    queue.append(tmpnode.left)
                if tmpnode.right:
                    new_level_val.append(tmpnode.right.val)
                    queue.append(tmpnode.right)
            if  new_level_val:queue_val.append(new_level_val[:])
        return queue_val
                
                

        
