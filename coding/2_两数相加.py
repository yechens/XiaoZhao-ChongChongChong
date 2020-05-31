"""
题目描述：
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

解题思路：
为了节省空间，直接在l1上操作，循环遍历一次即可，时间复杂度为O(m+n)。每次循环将l2的节点加到l1上，需要注意进位是否为0
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        tmp = 0
        while p and q:
            p.val = p.val + q.val + tmp
            tmp = 0
            if p.val > 9:
                p.val -= 10
                tmp += 1
            if not p.next:
                z = p
            p = p.next
            q = q.next
        while p:
            p.val += tmp
            tmp = 0
            if p.val > 9:
                p.val -= 10
                tmp += 1
            if not p.next:
                z = p
            p = p.next
        if q:
            z.next = q
        while q:
            q.val += tmp
            tmp = 0
            if q.val > 9:
                q.val -= 10
                tmp += 1
            if not q.next:
                z = q
            q = q.next
        if tmp:
            node = ListNode(tmp)
            z.next = node
        return l1
