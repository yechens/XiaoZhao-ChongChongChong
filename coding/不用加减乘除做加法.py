'''
题目描述:
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2

解题思路：
确定 0 0 /0 1 /1 1 /1 0的加和位及进位的关系


'''

class Solution:
    def add(self, a: int, b: int) -> int:
        #位运算 进位和不进位的结论！！！
        max_pos=0xffffffff
        a=a & max_pos
        b=b & max_pos
        while b!=0:
            a,b=a^b,(a&b)<<1 & max_pos
        return  a if a<=0x7fffffff else ~(a^max_pos)
