# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
题目描述:
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
解题思路：
    找到中间位置
双指针：起始slow位置和fast位置不同,或者说从-1位置开始
1.举例子🌰：
偶数 ：
     1 2 3 4
slow |
fast   | 
     1 2 3 4
slow   |(m)
fast       | 
奇数：
     1 2 3 4 5 (6)
slow |
fast   | 
     1 2 3 4 5 (6)
slow   |
fast       |
     1 2 3 4 5 (6)
slow     |(m)
fast            |

2.mid_head=slow.next
3.翻转mid_head开始的后半部分链表
4.懒猴从head和mid_head遍历看val是不是相等
注意点⚠️：
双指针的判断条件为：
while fast and fast.next 


'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #链表翻转
        def reverse_list(head):
            pre=None
            current=head
            while current:
                curr_copy=current.next
                current.next=pre
                pre=current
                current=curr_copy
            return pre
        #找到中间位置
        count_num=0
        thead=head
        while thead:
            count_num+=1
            thead=thead.next
        mid=count_num//2
        mid_head=None
        count_num=0
        thead=head
        while thead:
            if count_num==mid:
                mid_head=thead
                break
            count_num+=1
            
            thead=thead.next

        #双指针找中间位置
        slow=head
        fast=None
        if not head:return True
        if not head.next: return True
        else:fast=head.next
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        mid_head=slow.next

        
        #翻转
        mid_head=reverse_list(mid_head)
        while mid_head and head:
            if mid_head.val!=head.val:
                return False
            mid_head=mid_head.next
            head=head.next
        return True
