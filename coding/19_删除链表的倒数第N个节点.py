"""
题目描述：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

解题思路：采用双指针方法，首先要区分n是否等于链表的长度，如果等于的话，相当于删除第一个节点，直接得到head.next；不等于的话，q指向头节点，p指向头节点的后面第n个节点，然后p,q同步遍历，直到p指向最后一个节点，然后删除q后面的一个节点
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p,q = head, head
        for i in range(n):
            p = p.next
        if not p:
            return head.next
        else:
            while p.next:
                p = p.next
                q = q.next
            q.next = q.next.next
            return head
