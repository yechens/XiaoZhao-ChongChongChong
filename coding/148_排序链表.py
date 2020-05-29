"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5


解题思路：
使用归并排序，递归切分直到链表中只剩一个节点
依次两两合并两段有序的小数组
归并排序速度仅次于快速排序，是一种稳定的排序算法
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序，时间复杂度: O(nlogn)
        # 1.递归切分，直到剩下一个结点
        # 2.依次合并
        if not head or not head.next:
            return head
        
        # 1.快慢指针找到中点 mid 进行递归切分
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid, slow.next = slow.next, None
        left = self.sortList(head)
        right = self.sortList(mid)

        # 2.合并两段有序的小数组
        newh = ListNode(-1) # 新建一个头指针
        node = newh
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        node.next = left if left else right
        return newh.next
