'''
题目描述：
给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。


解题思路：
递归遍历左右子树的最大路径
举例：
当前最大值==max(左子树的右子树的最大路径,右子树的左子树的最大路径）


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.global_max=0
        #方法一
        #手动模拟一下
        def get_zz(root):
             #返回值：左右子树两边的合理路径上的节点数！
             #后序遍历
             
            if not root:return (0,0)
            left_condi=get_zz(root.left)
            right_condi=get_zz(root.right)

            #计算左右两边的数量
            if max(left_condi[1]+1,right_condi[0]+1)>self.global_max:
                    self.global_max=max(left_condi[1]+1,right_condi[0]+1)

            return(left_condi[1]+1,right_condi[0]+1)
        get_zz(root)
         #节点数-1等于路径数
        return self.global_max-1
        
        #方法2
        def get_zz(root,direc):#自己都搞不明白。。。
        #返回值：路径上节点的数量
            if not root:return 0
            if direc=='left':
                #左右两边
                tmp_max_left=get_zz(root.left,'left')
                tmp_max_right=get_zz(root.left,'right')
                #当前是从左边过来的，左边不能+1，
                if tmp_max_left>self.global_max:
                    self.global_max=tmp_max_left
                if tmp_max_right+1>self.global_max:
                    self.global_max=tmp_max_right+1
                #只往上传递右边符合条件的节点数
                return tmp_max_right+1
               
            if direc=='right':
                #左右两边
                tmp_max_left=get_zz(root.right,'left')
                tmp_max_right=get_zz(root.right,'right')
                
                #当前是从右边过来的，右边不能+1，
                ##只往上传递左边符合条件的节点数
                if tmp_max_left+1>self.global_max:
                    self.global_max=tmp_max_left+1
                if tmp_max_right>self.global_max:
                    self.global_max=tmp_max_right
                return tmp_max_left+1   
        get_zz(root,'left')
        get_zz(root,'right')
        #节点数-1等于路径数
        return self.global_max-1
