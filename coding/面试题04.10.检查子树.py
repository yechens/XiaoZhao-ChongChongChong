'''
题目描述：
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。

解题思路：
方法一：递归判断是否为子树
方法二：中序遍历判断----->bug

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        #递归判断
        def issame(root1,root2):
            if not root1 or not root2:return root1==root2
            if root1.val!=root2.val:return False
            return issame(root1.left,root2.left) and issame(root1.right,root2.right) 
        def midtraverse(root):
            if not root:return issame(root,t2)
            res1=midtraverse(root.left)
            if issame(root,t2):return True
            res2=midtraverse(root.right)
            return res1 or res2
        return midtraverse(t1)


        #中序遍历==bug
        def midtraverse(root,travelist):
            if not root:return
            midtraverse(root.left,travelist)
            travelist.append(str(root.val))
            midtraverse(root.right,travelist)
        self.tree1trave=[]
        self.tree2trave=[]
        midtraverse(t1,self.tree1trave )       
        midtraverse(t2,self.tree2trave )  
        return   ''.join(self.tree2trave) in  ''.join(self.tree1trave)  
