'''
题目描述:
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

解题思路：
DP dp[i][j]表示掷i个骰子后，总点数为j的次数 （手动写几个样例推一下！）

'''

class Solution:
    def twoSum(self, n: int) -> List[float]:
        #dp dp[i][j]表示掷i个骰子后，总点数为j的次数
        dp=[[0 for _ in range(n*6+1)] for _ in range (n+1)]
        for j in range(7):
            dp[1][j]=1
        dp[1][0]=0
        for i in range(2,n+1):
            for j in range(i*1,i*6+1):
                dp[i][j]=sum(dp[i-1][j-6 if j-6>0 else 0 :j])
        final_res=dp[-1][n:]
        all_sum=sum(final_res)
        res=[]
        for isum in final_res:
            res.append(isum/all_sum)
        return res
