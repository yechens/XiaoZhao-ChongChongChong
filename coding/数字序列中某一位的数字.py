'''
题目描述：

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0



解题思路：
数学
找到第n位所在的数字，找到在该数字中的位置
link:https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/zhe-shi-yi-dao-shu-xue-ti-ge-zhao-gui-lu-by-z1m/

'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        #难样例 10
        if n<=9:return n
        digit=-1
        index=0
        #找到数位的第几个

        while n-9*10**(digit)*index>0:
            n=n-9*10**(digit)*index
            digit+=1
            index+=1
        #找到对应number
        #问题难点<=====
        #(n-1)//index) 而不是n//index
        number=str(int(10**(index-1)+(n-1)//index))
        print(number)
        #找到number对应的数字
        rem=int(list(number)[int((n)%index)-1])
        return rem
