'''
题目描述：
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

 

示例 1：



输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
示例 2：



输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
示例 3：

输入：root = [2,3,9,10,7,8,6,5,4,11,1]
输出：1025
示例 4：

输入：root = [1,1]
输出：1
 

提示：

每棵树最多有 50000 个节点，且至少有 2 个节点。
每个节点的值在 [1, 10000] 之间。

解题思路：
递归计算每次删除左、右子树，以及以当前节点为根节点的乘积，同时保存最大值。


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        #后序遍历获取总和
        self.pre_traverse_val=[]
        def pre_traverse_get_val(root):
            if not root :return None
            pre_traverse_get_val(root.left)
            
            pre_traverse_get_val(root.right)
            self.pre_traverse_val.append(root.val)
        pre_traverse_get_val(root)
        sum_val=sum(self.pre_traverse_val)
        #后序遍历
        self.max_res=0
        def pre_traverse(root):
            if not root :return 0
            tmp_sum_left=pre_traverse(root.left) 
            #去掉左节点
            left_max_res=tmp_sum_left*(sum_val-tmp_sum_left)
            if left_max_res>self.max_res:
                self.max_res=left_max_res
            tmp_sum_right=pre_traverse(root.right)
            #去掉右节点
            right_max_res=tmp_sum_right*(sum_val-tmp_sum_right)
            if right_max_res>self.max_res:
                self.max_res=right_max_res
            #去掉根节点及子树
            root_max_res=(root.val+tmp_sum_right+tmp_sum_left)*(sum_val-root.val-tmp_sum_right-tmp_sum_left)
            if root_max_res >self.max_res:
                self.max_res=root_max_res
            #返回当前子树的和
            return root.val+tmp_sum_right+tmp_sum_left
        pre_traverse(root)
        return self.max_res%(10**9+7)


            


