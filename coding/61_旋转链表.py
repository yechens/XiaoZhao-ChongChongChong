'''
题目描述：
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

解题思路：
O(n)
先计算链表的长度n,同时把环串成循环链表，计算从最开始移动的step=n-k%n
找到新链表的起始位置start,上一个位置即为end位置

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #存储长度
        if not head:return None
        list_len=0
        tmp_head=head
        #计算长度并串环,变成循环链表
        while tmp_head:
            list_len+=1
            if not tmp_head.next:
                tmp_head.next=head
                break 
            tmp_head=tmp_head.next
        move_step=list_len-k%list_len
        count=0
        start=head
        end=None
        #移动
        for i in range(move_step):
            end=start
            start=start.next
        end.next=None
        return start
        



