'''
题目描述：
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

解题思路：
每次合并两个链表，最后合并完所有的链表。（也可用分治的方法，每次合并，两两配对，直到只剩一个链表）
有以下易错点和注意点：
易错点：
    单独变量存头节点
    每次需更新合并链表为最后一个节点
注意点：
    考虑输入链表有空的情况（链表的list为空，或者list中的链表元素为空）

待优化：
不过虽好理解，但代码略冗余，后续再改进！



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge_twolists(alist,blist):
            root=None
            #易错点：单独变量存头节点
            final_root=None
            while alist and blist:
                if alist.val>blist.val:
                    if not root:
                        root=blist
                        final_root=blist
                        blist=blist.next
                        root.next=None
                    else:
                        root.next=blist
                        blist=blist.next
                        root.next.next=None
                        #易错：root也需要指向新的节点
                        root=root.next       
                else:
                    if not root:
                        root=alist
                        final_root=alist
                        alist=alist.next
                        root.next=None
                    else:
                        root.next=alist
                        alist=alist.next
                        root.next.next=None
                        #易错：root也需要指向新的节点
                        root=root.next
                    
            if alist:
                #考虑输入链表有空的情况
                if not final_root:
                    final_root=alist
                else:
                    root.next=alist
            if blist:
                #考虑输入链表有空的情况
                if not final_root:
                    final_root=blist
                else:
                    root.next=blist
            return final_root
        while len(lists)>1:
            alist=lists.pop(0)
            blist=lists.pop(0)
            new_list=merge_twolists(alist,blist)
            #print(new_list)
            lists.append(new_list)
        if not lists:return None
        return lists[0]


# 分治清爽解法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 分治
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        # 合并2个有序链表
        def fuge_list(l1, l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            p, q = l1, l2
            pre_head = ListNode(0)
            z = pre_head
            while p and q:
                if p.val <= q.val:
                    z.next = p
                    p = p.next
                else:
                    z.next = q
                    q = q.next
                z = z.next
            if p:
                z.next = p
            if q:
                z.next = q
            return pre_head.next
        # 分治函数
        def divide_conquer(lists):
            if len(lists) == 1:
                return lists[0]
            elif len(lists) == 2:
                return fuge_list(lists[0], lists[1])
            else:
                return fuge_list(divide_conquer(lists[:len(lists)//2]), divide_conquer(lists[len(lists)//2:]))
        return divide_conquer(lists)
    
                
