'''
题目描述：
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？


解题思路：
迭代：使用层序遍历解决
递归：只考虑当前节点，及其子节点是否对称，即roo1和root2、root1.left和root2.right、root1.right和
root2.left

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #迭代法
        queue=[root]
        #判断数组是否镜像
        def issymlist(queue):
            val_list=[]
            #偶数个
            if len(queue)%2!=0:
                return False
            #获取节点的值
            for iq in queue:
                val_list.append(iq.val)
            for i in range(len(val_list)//2):
                if val_list[i]!=val_list[len(val_list)-1-i]:
                    return False
            return True

        while queue:
            tmpl=len(queue)
            for i in range(tmpl):
                tmpnode=queue.pop(i)
                if tmpnode.left:
                    queue.append(tmpnode.left)
                if tmpnode.right:
                    queue.append(tmpnode.right)
            #判断是否镜像
            if not issymlist(queue):return False
        return True


            


    #递归法
    def isSymmetric(self, root: TreeNode) -> bool:
        def issym(left,right):
            #无子节点
            #if not root:return True
            #子节点可能为空
            if not left:return left==right
            #子节点不为空但不相等
            if left.val!=right.val:
                return False
            #子节点不为空但相等
            #易错点：只考虑两层即可
            return issym(left.left,right,right)and issym(left.right,right.left)
        return issym(root.left.root.right)
