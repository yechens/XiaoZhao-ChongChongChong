"""
题目描述：
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1 (图片详见leetcode页面：https://leetcode-cn.com/problems/linked-list-cycle-ii/)
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

解题思路：
1.使用哈希表存放已经遍历过的节点
2.双指针（快慢指针）
慢指针一次走1步，快指针一次走2步
（1）快指针走过链表末端，一定没有环
（2）若有环，快慢指针一定会相遇
- 快慢指针第一次相遇时，快指针走过了 2nb 步，慢指针走过了 nb 步，其中 b 表示链表环节点个数
- 设链表头部到环入口节点个数为 a （不包括环入口节点），将快指针重新设置为头节点，和慢指针一起向前走 a 步后停下，两者将在入口节点重合
方法2时间复杂度：O(n), 空间复杂度：O(1)

add-lyf:
解题思路：
快慢指针：
    关键点-slow从index0开始，fast从index1开始（即假设两者都从-1位置开始）
    易错点：fast走两步时，需要判断fast.next是不是None



"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head: return None # 无环

        # 1.hashmap
        from collections import OrderedDict
        myhash = OrderedDict() # 顺序字典
        while head and head.next:
            if head not in myhash:
                myhash[head] = 1
                head = head.next
            else:
                return head
        return None

        # 2.双指针（快慢指针）
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 快慢指针相遇
                break
        if not fast or not fast.next:
            return None
        # 快慢指针第一次相遇，分别走了 2nb、nb 步，其中 b 表示环的大小，a表示链表头部到环节点入口的距离（不包含环节点入口）
        fast = head # fast 重头开始
        while fast != slow:
            fast = fast.next
            slow = slow.next
        # 快慢指针第二次一定在环入口相遇
        return slow
