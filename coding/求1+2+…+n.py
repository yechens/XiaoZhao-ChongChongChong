'''
题目描述:
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

解题思路：
递归
'''

class Solution:
    def sumNums(self, n: int) -> int:
        #递归
        self.res=0
        def sum(n):
            n>1 and self.sumNums(n-1)
            self.res+=n
        sum(n)
        return self.res
    
        #不可用
        for i in range(1,n+1):
            res+=i
        return res
