'''
题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 



 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 



 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

解题思路：
1.首先找到二叉树的最左节点，即head,并保存
2.非递归中序遍历
    2.1每次pop时，调整指向=====>变成双向链表
    2.2易忘点：非递归的两个条件




'''




"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return None
        #找到头节点
        head=None
        tmp_root=root
        while tmp_root.left:
            tmp_root=tmp_root.left
        head=tmp_root
        #非递归遍历
        stack=[]
        tmp_root=root
        previous=None
        #易忘点：非递归的两个条件
        while  stack or  tmp_root:
            if tmp_root:
                stack.append(tmp_root)
                tmp_root=tmp_root.left
            else:
                tmp_root=stack.pop()
                if not previous:previous=tmp_root
                else:
                    #双向
                    previous.right=tmp_root
                    tmp_root.left=previous
                    previous=tmp_root
                tmp_root=tmp_root.right
        previous.right=head
        head.left=previous
        return head
            
            




            
        
        
            
