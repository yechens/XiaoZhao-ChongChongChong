'''
题目描述:
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

解题思路:
根据后序遍历安的性质 左子树 右子树 根 + root节点

'''



class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        #判断左右子树是否都是满足搜索树的条件
        def recursive(i,j):
            if i>=j:return True
            #找到左右子树的边界
            p=i
            q=j
            while postorder[p]<postorder[q]:p+=1
            left_tree=postorder[i:p]
            right_tree=postorder[p:q]
            if len(left_tree)>0 and max(left_tree)>postorder[q]:return False
            if len(right_tree)>0 and min(right_tree)<postorder[q]:return False
            if not recursive(i,p-1):return False
            if not recursive(p,q-1):return  False
            return True
        return recursive(0,len(postorder)-1)






        #先序 后序 重构二叉树 +搜索性质
        def recursive(prelist,postlist,isleft,preroot):
            if len(prelist)!=len(postlist):return False
            if len(prelist)==0:return len(postlist)==0
            if len(postlist)==0:return False
            root=postlist[-1]
            try:
                index_pre=prelist.index(root)
            except:
                return False
            if index_pre==-1:return False
            #左子树
            left_list=prelist[:index_pre]
            post_left_list=postlist[:len(left_list)]
            #右子树
            right_list=prelist[index_pre+1:]
            post_right_list=postlist[len(left_list):-1]
            #保证大小
            dis_tri=True
            if False:
                if isleft:
                    if len(right_list)>0 and  max(right_list)>preroot:return False
                else:
                    if len(left_list)>0 and  min(left_list)<preroot:return False
            #左子树都要小于root
            if len(left_list)>0 and max(left_list)>root:return False
            #右子树都要大于root
            if len(right_list)>0 and min(right_list)<root:return False
            left_res=recursive(left_list,post_left_list,True,root)
            if not left_res:return False
            if not recursive(right_list,post_right_list,False,root):return False
            return True
        return recursive(sorted(postorder),postorder,None,None)