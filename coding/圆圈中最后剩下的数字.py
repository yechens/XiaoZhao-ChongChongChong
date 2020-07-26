'''
题目描述：
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

解题思路：
每次mod，找到pop的index,更新原有数组

'''


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        #取mod
        num_list=list(range(n))
        index=0
        pre_index=0
        while len(num_list)>1:
            index_offset=m
            final_index=(pre_index+index_offset-1)%(len(num_list))
            pre_index=final_index
            num_list.pop(pre_index)
        return num_list[0]
