'''
题目描述：
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36


解题思路：

方法1:dp会溢出，但思路比较好
方法2:总结规律（不是很容易理解）

'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        #dp 会溢出！！！！！
        
        dp=[1]*(n+1)
        dp[1]=1
        dp[2]=1
        if n<=2:return dp[n]
        for i in range(3,n+1):
            max_res=-1
            for j in range(1,i):
                #关键点
                max_res=max(max_res,max(j,dp[j])*max(i-j,dp[i-j]))
                if i>100:
                    print(max_res)
                #max_res=max(max_res,dp[j]*dp[i-j])
            dp[i]=max_res
        return int(dp[n]%(1e9+7))