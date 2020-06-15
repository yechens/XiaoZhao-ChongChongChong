'''
问题描述：
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

解题思路：
二进制表示
举例：
10//3=3----(2**0+2**1)
7//3=2-----(2**1)

举个例子：11 除以 3 。
首先11比3大，结果至少是1， 然后我让3翻倍，就是6，发现11比3翻倍后还要大，那么结果就至少是2了，那我让这个6再翻倍，得12，11不比12大，吓死我了，差点让就让刚才的最小解2也翻倍得到4了。但是我知道最终结果肯定在2和4之间。也就是说2再加上某个数，这个数是多少呢？我让11减去刚才最后一次的结果6，剩下5，我们计算5是3的几倍，也就是除法




TODO：
3进制怎么做？？

'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if -2**31>dividend or dividend>2**31-1 or -2**31>divisor or divisor>2**31-1 :
            return 2**31-1
        if abs(dividend)<abs(divisor):return 0
        ten_list=[0]*15
        tag=1
        if divisor<0:
            tag=-1
            divisor=abs(divisor)
        tag2=1
        if dividend<0:
            tag2=-1
            dividend=abs(dividend)

        def div_(a,b):
            if a<b:return 0
            count=1#至少是1
            tmp=b
            while(tmp+tmp<=a):
                count=count+count#count*2
                tmp=tmp+tmp#tmp*2
            return count+div(a-tmp,b)
        res=tag*tag2*div(dividend,divisor)
        if -2**31>res or res>2**31-1 :
            return 2**31-1
        return res
