'''
题目描述：
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6

解题思路：
按数字 23--3---4的左右拆分算组合数

'''

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n==0:return 0
        n=str(n)
        nlen=len(n)
        res=0
        index=1
        for i in range(nlen):
            if n[nlen-1-i]=='0':
                #借位
                prenum=(int(n)//(10**index))
                lastnum=10**(index-1)
                res+=(1 if prenum==0 else prenum)*lastnum
            elif n[nlen-1-i]=='1':
                #难点
                prenum=(int(n)//(10**index))
                new_add=(int(n)%(10**(index-1))+1)
                print('new_add:',new_add)
                lastnum=10**(index-1)
                #左边没了的话，那只有右边的new_add
                res+=(new_add if prenum==0 else prenum*lastnum+new_add)
            else:
                prenum=(int(n)//(10**index)+1)
                lastnum=10**(index-1)
                res+=(1 if prenum==0 else prenum)*lastnum
            index+=1
            print(res)
        return res
