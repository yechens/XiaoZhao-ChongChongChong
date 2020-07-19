'''
题目描述：
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

解题思路：
dp[i] 表示使用0-i的字符，共有多少种翻译方法
关键点：dp[i-1]，dp[i-2],dp[i]的关系


'''

class Solution:
    def translateNum(self, num: int) -> int:
        #dp
        num=str(num)
        dp=[0]*len(num)
        dp[0]=1
        for i in range(1,len(num)):
            if i==1:
                #考虑00
                if int(num[:2])<26:
                    if int(num[0])==0:
                        dp[1]=1
                    else:
                        dp[1]=2
                else:
                    dp[1]=1
            else:
                #判断num[i-1:i+1]
                add=0
                if int(num[i-1:i+1])<26:
                    if int(num[i-1])==0:
                        add=1
                    else:
                        add=2
                else:
                    add=1
                dp[i]=dp[i-1]if add==1 else dp[i-1]+dp[i-2]
        return dp[-1]
