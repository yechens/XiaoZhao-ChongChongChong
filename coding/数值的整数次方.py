'''
题目描述：
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
解题思路：
O(logN)
通过把数字转化为二进制，通过二进制的位数来判断是否有效

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #二分法
        if n==0:return 1
        res=1
        org=x
        if n<0:x,n=1/x,-n
        #转为2进制
        binn=''
        while n>=2:
            binn+=str(n%2)
            n=n//2
        binn+='1'
        res=1
        pre=x
        #根据二进制的数位判断要不要✖️
        for index,i in enumerate(binn):
            if index==0:
                if i=='0':
                    pass
                else:
                    res*=pre
            else:
                pre*=pre
                if i=='0':
                    pass
                else:
                    res*=pre
        return res
